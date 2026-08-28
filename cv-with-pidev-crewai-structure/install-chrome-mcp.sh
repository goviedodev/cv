#!/bin/bash
set -euo pipefail
# Installer for the Chrome DevTools MCP server for Claude Code.
# This script is idempotent: running it multiple times will update to latest.

REPO="https://github.com/haasonsaas/claude-code-browser-mcp-setup"
INSTALL_DIR="$HOME/.claude/mcp/chrome-devtools-mcp"
CONFIG_FILE="$HOME/.claude/mcp/chrome-devtools-mcp.json"

echo "Installing Chrome DevTools MCP to $INSTALL_DIR"
mkdir -p "$INSTALL_DIR"
cd "$INSTALL_DIR"

if command -v npm &> /dev/null; then
  echo "npm detected. Installing via npm..."
  npm install chrome-devtools-mcp@latest
elif command -v yarn &> /dev/null; then
  echo "yarn detected. Installing via yarn..."
  yarn add chrome-devtools-mcp@latest
else
  echo "Neither npm nor yarn found. Please install Node.js and npm/yarn."
  exit 1
fi

echo "Creating MCP config file at $CONFIG_FILE"
cat > "$CONFIG_FILE" << "INNER_EOF"
{
  "name": "claude-in-chrome",
  "blurb": "Control Chrome browser for web automation tasks (Claude-in-Chrome)",
  "url": "https://github.com/haasonsaas/claude-code-browser-mcp-setup",
  "setup": "Run the install script, then restart Jcode Desktop.",
  "mcp": {
    "command": "node",
    "args": ["/home/goviedo/.claude/mcp/chrome-devtools-mcp/node_modules/.bin/chrome-devtools-mcp"]
  }
}
INNER_EOF

echo ""
echo "Done. Restart Jcode to activate Chrome MCP."
echo "You should see a browser tools indicator in the Jcode interface."
