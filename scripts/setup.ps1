# DrGPT Setup Script for PowerShell
# This script sets up DrGPT configuration for Windows

# Define paths
$CONFIG_FOLDER = "$env:USERPROFILE\.config"
$DRGPT_CONFIG_FOLDER = "$CONFIG_FOLDER\dr_gpt"
$DRGPT_CONFIG_PATH = "$DRGPT_CONFIG_FOLDER\.drgptrc"
$ROLE_STORAGE_PATH = "$DRGPT_CONFIG_FOLDER\roles"
$CHAT_CACHE_PATH = "$env:TEMP\chats_cache"
$CACHE_PATH = "$env:TEMP\cache"

# Create configuration directory if it doesn't exist
if (!(Test-Path $DRGPT_CONFIG_FOLDER)) {
    New-Item -ItemType Directory -Path $DRGPT_CONFIG_FOLDER -Force
}

if (!(Test-Path $ROLE_STORAGE_PATH)) {
    New-Item -ItemType Directory -Path $ROLE_STORAGE_PATH -Force
}

# Create configuration file
$configContent = @"
# DrGPT Configuration
CHAT_CACHE_PATH=$CHAT_CACHE_PATH
CACHE_PATH=$CACHE_PATH
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
ROLE_STORAGE_PATH=$ROLE_STORAGE_PATH
DEFAULT_EXECUTE_SHELL_CMD=false
DISABLE_STREAMING=false
CODE_THEME=dracula

# Advanced AI Settings
TEMPERATURE=0.7
MAX_TOKENS=2048
TOP_P=1.0
"@

$configContent | Out-File -FilePath $DRGPT_CONFIG_PATH -Encoding UTF8

Write-Host "DrGPT configuration created successfully!" -ForegroundColor Green
Write-Host "Configuration file: $DRGPT_CONFIG_PATH" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Set your API key: python -m drgpt --provider openai --api-key YOUR_API_KEY" -ForegroundColor White
Write-Host "2. List available providers: python -m drgpt --list-providers" -ForegroundColor White
Write-Host "3. Test the installation: python -m drgpt 'Hello, how are you?'" -ForegroundColor White
