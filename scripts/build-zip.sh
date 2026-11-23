#!/usr/bin/env bash
# Builds dist/devils-advocate.zip for uploading to Claude.ai (Settings → Capabilities → Skills).
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist
rm -f dist/devils-advocate.zip
(cd skills && zip -qr ../dist/devils-advocate.zip devils-advocate -x '*.DS_Store')
echo "Built dist/devils-advocate.zip"
