#!/usr/bin/env python3
import argparse
import os
import sys
from datetime import datetime, timezone, timedelta
from typing import Any

try:
    import requests
except ImportError:
    print("Error: 'requests' library required. Install with: pip install requests")
    sys.exit(1)

try:
    from pydantic import BaseModel, Field
except ImportError:
    print("Error: 'pydantic' library required. Install with: pip install pydantic")
    sys.exit(1)

BASE_URL = "https://claude.ai"

HEADERS: dict[str, str] = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json",
    "anthropic-client-platform": "web_claude_ai",
    "anthropic-client-version": "1.0.0",
    "Origin": "https://claude.ai",
    "Referer": "https://claude.ai/settings/usage",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
}


class UsageLimit(BaseModel):
    utilization: float
    resets_at: str
    time_until_reset: str


class AgentUsage(BaseModel):
    five_hour: UsageLimit
    seven_day: UsageLimit
    extra: dict[str, Any] = Field(default_factory=dict)


class Organization(BaseModel):
    id: str
    name: str


class UsageData(BaseModel):
    organization: Organization
    agents: dict[str, AgentUsage] = Field(default_factory=dict)

    @classmethod
    def from_claude_api(
        cls, session_key: str, org_id: str | None = None
    ) -> "UsageData":
        orgs = get_organizations(session_key)
        if not orgs:
            raise ValueError("No organizations found")

        oid = org_id or orgs[0]["uuid"]
        org_name = next((o["name"] for o in orgs if o["uuid"] == oid), oid)

        raw_usage = get_usage(session_key, oid)
        now = datetime.now(timezone.utc)

        extra: dict[str, Any] = {}
        five_hour: UsageLimit | None = None
        seven_day: UsageLimit | None = None

        for api_key, label in [
            ("five_hour", "five_hour"),
            ("seven_day", "seven_day"),
        ]:
            if raw_usage.get(api_key):
                data = raw_usage[api_key]
                resets_at = parse_resets_at(data.get("resets_at"))
                td = resets_at - now if resets_at else None

                limit = UsageLimit(
                    utilization=data.get("utilization", 0),
                    resets_at=data.get("resets_at", ""),
                    time_until_reset=format_timedelta(td)
                    if td and td.total_seconds() > 0
                    else "reset pending",
                )

                if api_key == "five_hour":
                    five_hour = limit
                else:
                    seven_day = limit
            elif api_key == "five_hour":
                five_hour = UsageLimit(
                    utilization=0, resets_at="", time_until_reset="N/A"
                )
            elif api_key == "seven_day":
                seven_day = UsageLimit(
                    utilization=0, resets_at="", time_until_reset="N/A"
                )

        for key, value in raw_usage.items():
            if key not in ("five_hour", "seven_day") and value is not None:
                extra[key] = value

        return cls(
            organization=Organization(id=oid, name=org_name),
            agents={
                "claude_code": AgentUsage(
                    five_hour=five_hour
                    or UsageLimit(utilization=0, resets_at="", time_until_reset="N/A"),
                    seven_day=seven_day
                    or UsageLimit(utilization=0, resets_at="", time_until_reset="N/A"),
                    extra=extra,
                )
            },
        )


def get_session_key() -> str | None:
    env_key = os.environ.get("ANTHROPIC_SESSION_KEY")
    if env_key:
        return extract_session_key(env_key)

    env_file = os.path.join(os.path.dirname(__file__), "..", ".env")
    if os.path.exists(env_file):
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line.startswith("sessionKey="):
                    return extract_session_key(line.split("=", 1)[1])
    return None


def extract_session_key(value: str) -> str:
    if value.startswith("sk-ant-"):
        return value
    return value.split(";")[0]


def parse_resets_at(resets_at: str | None) -> datetime | None:
    if not resets_at:
        return None
    return datetime.fromisoformat(resets_at.replace("Z", "+00:00"))


def format_timedelta(td: timedelta) -> str:
    total_seconds = int(td.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours > 0:
        return f"{hours}h {minutes}m"
    return f"{minutes}m {seconds}s"


def get_organizations(session_key: str) -> list[dict[str, Any]]:
    resp = requests.get(
        f"{BASE_URL}/api/organizations",
        headers={**HEADERS, "Cookie": f"sessionKey={session_key}"},
    )
    resp.raise_for_status()
    return resp.json()


def get_usage(session_key: str, org_id: str) -> dict[str, Any]:
    resp = requests.get(
        f"{BASE_URL}/api/organizations/{org_id}/usage",
        headers={**HEADERS, "Cookie": f"sessionKey={session_key}"},
    )
    resp.raise_for_status()
    return resp.json()


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch Claude API usage data")
    parser.add_argument(
        "--org", help="Organization ID (optional, uses first if omitted)"
    )
    parser.add_argument(
        "--key", help="Session key (or set ANTHROPIC_SESSION_KEY env var)"
    )
    parser.add_argument("--output", "-o", help="Output JSON file")
    args = parser.parse_args()

    session_key = args.key or get_session_key()
    if not session_key:
        print("Error: Session key required. Pass --key or set ANTHROPIC_SESSION_KEY")
        sys.exit(1)

    data = UsageData.from_claude_api(session_key, args.org)

    json_str = data.model_dump_json(indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(json_str)
        print(f"Written to {args.output}")
    else:
        print(json_str)


if __name__ == "__main__":
    main()
