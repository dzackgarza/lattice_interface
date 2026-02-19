#!/usr/bin/env bash
set -euo pipefail

export GCR_ALLOW_AUTOSTART=0

# Stop systemd from respawning the daemon
systemctl --user mask gnome-keyring-daemon.socket 2>/dev/null || true
systemctl --user stop gnome-keyring-daemon.socket 2>/dev/null || true
systemctl --user stop gnome-keyring-daemon.service 2>/dev/null || true

# Kill any leftover gnome-keyring-daemon processes
for pid in $(pgrep -x gnome-keyring-daemon 2>/dev/null); do
  kill -9 "$pid" 2>/dev/null || true
done
# Remove the runtime socket dir so new daemon doesn't detect an old one
rm -rf "/run/user/$(id -u)/keyring"
sleep 0.5

# Unmask on exit
trap 'systemctl --user unmask gnome-keyring-daemon.socket 2>/dev/null' EXIT

mkdir -p ~/.cache
mkdir -p ~/.local/share/keyrings

dbus-run-session -- bash -c '
  eval "$(printf "\n" | gnome-keyring-daemon --unlock)"
  eval "$(printf "\n" | gnome-keyring-daemon --start)"
  coderabbit "$@"
' _ "$@"
