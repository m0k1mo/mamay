#!/bin/bash
# Mamay Native — turn this Mac into a background CI builder (GitHub self-hosted runner, label "artem-mac").
# Usage (one line in Terminal):  curl -fsSL https://raw.githubusercontent.com/m0k1mo/mamay/main/scripts/mac-runner.sh | bash -s <TOKEN>
# <TOKEN> = the token from github.com/m0k1mo/mamay/settings/actions/runners/new (valid 1 hour).
# Runs as your user (no sudo), lives in ~/mamay-runner, starts by itself at login (launchd). Remove: ~/mamay-runner/svc.sh uninstall.
# Only push/dispatch workflows of m0k1mo/mamay run here (no pull_request triggers), so nobody else's code can run on this Mac.
set -euo pipefail
TOKEN="${1:-}"
[ -n "$TOKEN" ] || { echo "Потрібен токен: bash -s <TOKEN>"; exit 1; }
[ "$(uname -m)" = arm64 ] || { echo "Потрібен Mac з Apple Silicon"; exit 1; }
xcodebuild -version >/dev/null 2>&1 || { echo "Xcode не знайдено. Відкрий Xcode один раз і прийми ліцензію."; exit 1; }

D="$HOME/mamay-runner"; mkdir -p "$D/bin"; cd "$D"
echo "▸ Завантажую GitHub runner…"
V=$(curl -fsSL https://api.github.com/repos/actions/runner/releases/latest | sed -n 's/.*"tag_name": *"v\([^"]*\)".*/\1/p' | head -1)
[ -n "$V" ] || V=2.329.0
[ -x ./config.sh ] || curl -fsSL "https://github.com/actions/runner/releases/download/v$V/actions-runner-osx-arm64-$V.tar.gz" | tar xz

echo "▸ Ставлю xcodegen…"
if ! command -v xcodegen >/dev/null && [ ! -x bin/xcodegen ]; then
  curl -fsSL -o /tmp/xcodegen.zip https://github.com/yonaskolb/XcodeGen/releases/latest/download/xcodegen.zip
  rm -rf /tmp/xcodegen && unzip -q /tmp/xcodegen.zip -d /tmp/xcodegen
  cp -R /tmp/xcodegen/xcodegen/bin/xcodegen bin/ && mkdir -p share && cp -R /tmp/xcodegen/xcodegen/share/xcodegen share/ 2>/dev/null || true
fi
echo "PATH=$D/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin" > .path

echo "▸ Підключаю до github.com/m0k1mo/mamay…"
./config.sh --unattended --replace --url https://github.com/m0k1mo/mamay --token "$TOKEN" \
  --name "artem-mac" --labels "artem-mac" --work "_work"
./svc.sh install >/dev/null && ./svc.sh start >/dev/null

# keep the Mac awake while on the charger (screen may still turn off); removed with: launchctl unload ~/Library/LaunchAgents/ua.mamay.awake.plist
A="$HOME/Library/LaunchAgents/ua.mamay.awake.plist"
cat > "$A" <<P
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict><key>Label</key><string>ua.mamay.awake</string>
<key>ProgramArguments</key><array><string>/usr/bin/caffeinate</string><string>-s</string></array>
<key>RunAtLoad</key><true/><key>KeepAlive</key><true/></dict></plist>
P
launchctl unload "$A" 2>/dev/null || true; launchctl load "$A"
echo
echo "✅ Готово. Збирач працює на фоні й сам запускається після входу в систему."
echo "   На зарядці Мак не засинатиме (екран гасне як завжди). Кришку не закривай."
