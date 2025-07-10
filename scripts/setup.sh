#!/bin/bash

# DrGPT Setup Script for Unix-like systems
# This script sets up DrGPT configuration

# Define path variables
CONFIG_FOLDER="$HOME/.config"
DRGPT_CONFIG_FOLDER="$CONFIG_FOLDER/dr_gpt"
DRGPT_CONFIG_PATH="$DRGPT_CONFIG_FOLDER/.drgptrc"
ROLE_STORAGE_PATH="$DRGPT_CONFIG_FOLDER/roles"
CHAT_CACHE_PATH="/tmp/chats_cache"
CACHE_PATH="/tmp/cache"

# Create configuration directory if it doesn't exist
mkdir -p "$DRGPT_CONFIG_FOLDER"
mkdir -p "$ROLE_STORAGE_PATH"

# Create configuration file
cat << EOF > "$DRGPT_CONFIG_PATH"
# DrGPT Configuration
CHAT_CACHE_PATH=${CHAT_CACHE_PATH}
CACHE_PATH=${CACHE_PATH}
CHAT_CACHE_LENGTH=100
CACHE_LENGTH=100
REQUEST_TIMEOUT=60

# Default AI Provider Settings
DEFAULT_PROVIDER=openai
DEFAULT_MODEL=gpt-4
API_BASE_URL=https://api.openai.com/v1

# API Keys (set these with your actual keys)
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
GOOGLE_API_KEY=
HUGGINGFACE_API_KEY=
CUSTOM_API_KEY=

# UI Settings
DEFAULT_COLOR=magenta
ROLE_STORAGE_PATH=${ROLE_STORAGE_PATH}
DEFAULT_EXECUTE_SHELL_CMD=false
DISABLE_STREAMING=false
CODE_THEME=dracula

# Advanced AI Settings
TEMPERATURE=0.7
MAX_TOKENS=2048
TOP_P=1.0
EOF

echo "DrGPT configuration created successfully!"
echo "Configuration file: $DRGPT_CONFIG_PATH"
echo ""
echo "Next steps:"
echo "1. Set your API key: python -m drgpt --provider openai --api-key YOUR_API_KEY"
echo "2. List available providers: python -m drgpt --list-providers"
echo "3. Test the installation: python -m drgpt 'Hello, how are you?'"
