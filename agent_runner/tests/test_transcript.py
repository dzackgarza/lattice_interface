from agent_runner import transcript


def test_parse_last_message_falls_back():
    message = transcript.parse_last_message("claude", "", "hello\n\nworld", None)
    assert message == "world"


def test_parse_token_usage():
    text = "tokens used\n8,665"
    assert transcript.parse_token_usage(text) == 8665


def test_parse_gemini_json():
    payload = {
        "response": "Hello",
        "stats": {
            "models": {
                "gemini-3-pro-preview": {
                    "tokens": {"total": 42}
                }
            }
        },
    }
    import json

    stdout = json.dumps(payload)
    message, tokens = transcript.parse_gemini_json(stdout)
    assert message == "Hello"
    assert tokens == 42
