# Changelog

All notable changes to DrGPT will be documented in this file.

## [2.2.0] - 2025-01-10

### 🚀 Advanced CLI Features & Interactive Modes

### Added
- **Enhanced Code Mode** (`--code`): Generate code only in markdown format without explanations
- **Interactive Shell Mode** (`--shell`): Generate shell commands with interactive execution options
  - Execute commands with confirmation
  - Get detailed command descriptions
  - Abort option for safety
- **Text Editor Integration** (`--editor`): Open system text editor for input composition
  - Cross-platform editor detection (Windows: notepad/VS Code, macOS/Linux: nano/vim/VS Code)
  - Support for EDITOR and VISUAL environment variables
  - Automatic comment filtering
- **Interactive AI Interface** (`--interface`): Continuous chat mode with special commands
  - Real-time AI interaction with `!` prompt
  - Built-in commands: help, status, providers, clear, exit
  - Special modes: `code:` and `shell:` prefixes
  - Session management and context preservation

### Improved
- **Code Generation**: Now returns pure code without explanations when using `--code`
- **Shell Commands**: Enhanced safety with confirmation dialogs and command descriptions
- **Cross-Platform Compatibility**: Full support for Windows, macOS, and Linux
- **User Experience**: Interactive prompts with rich formatting and user-friendly interfaces
- **Error Handling**: Better error messages and graceful failure handling

### Technical
- **Enhanced AI Roles**: Updated system prompts for code-only and shell-only responses
- **Command Execution**: Safe subprocess execution with timeouts and error handling
- **Editor Detection**: Smart detection of available text editors per platform
- **Interactive Prompts**: Rich console prompts with choice validation

### Security
- **Safe Command Execution**: Confirmation required before executing shell commands
- **Timeout Protection**: 5-minute timeout for command execution
- **User Confirmation**: Interactive confirmation for potentially dangerous operations

## [2.1.0] - 2025-01-10

### ✨ Enhanced CLI Output with Rich Markdown Rendering

### Added
- **Rich Markdown Rendering**: Beautiful markdown formatting for AI responses with proper headers, code blocks, and bullet points
- **Animated Loading Indicators**: Elegant spinners during response generation in non-streaming mode
- **Formatted Status Panels**: Beautiful panels for status, provider lists, and version information
- **Colorized CLI Output**: Color-coded success, error, and informational messages
- **Flexible Output Options**: New `--no-markdown` flag for plain text output when needed
- **Enhanced Streaming**: Real-time streaming with optional formatted preview after completion

### Improved
- **User Experience**: More professional and visually appealing terminal interface
- **Code Highlighting**: Syntax-highlighted code blocks in responses
- **Status Display**: Rich panels with proper formatting for configuration status
- **Error Messages**: Color-coded error messages for better visibility
- **Provider Lists**: Beautifully formatted provider and model lists with bullet points

### Technical
- **Rich Integration**: Full integration with the `rich` library for terminal formatting
- **Backward Compatibility**: All existing functionality preserved with enhanced visuals
- **Performance**: No impact on response generation speed, only improved display

## [1.0.0] - 2025-01-10

### 🎉 Major Release - Complete Restructure

This is a complete rewrite of DrGPT with professional architecture and improved functionality.

### ✨ Added
- **New Architecture**: Modular design with core, cli, and provider modules
- **Multi-Provider Support**: OpenAI, Anthropic, Google, and custom APIs
- **Professional CLI**: Rich argument parsing with comprehensive help
- **Configuration Management**: Secure API key storage and provider switching
- **Cost Optimization**: Default to gpt-4o-mini (33x cheaper than GPT-4)
- **Rich Output**: Beautiful terminal output with syntax highlighting
- **Streaming Support**: Real-time response streaming
- **Chat Sessions**: Persistent conversation support
- **Code Generation**: Specialized code and shell command generation
- **Status Commands**: View current configuration and provider status
- **Test Suite**: Comprehensive testing framework
- **Documentation**: Professional README and developer guides

### 🔧 Changed
- **Project Structure**: Moved from `src/` to `drgpt/` package structure
- **Entry Points**: New CLI interface with `drgpt` command
- **Configuration**: Moved from `~/.config/dr_gpt/` to `~/.config/drgpt/`
- **Dependencies**: Reduced to core dependencies (requests, rich)
- **API Interface**: Unified interface for all AI providers
- **Error Handling**: Improved error messages and fallback mechanisms

### 🗑️ Removed
- Legacy `src/` directory structure
- Experimental plugin system (will be reimplemented)
- Old shell scripts and test files
- Arabic comments (now using English for international development)
- Unused dependencies (click, typer, distro)

### 🔒 Security
- Secure API key storage with environment variable support
- Safe shell command execution with user confirmation
- No data logging or transmission beyond chosen AI provider

### 📋 Migration Guide

For users upgrading from 1.x:

1. **Backup Configuration**: Your old config is in `~/.config/dr_gpt/`
2. **Reinstall**: `pip uninstall drgpt && pip install drgpt`
3. **Reconfigure**: Run `drgpt --provider openai --api-key YOUR_KEY`
4. **New Commands**: Use `drgpt` instead of `python main.py`

### 🐛 Bug Fixes
- Fixed import issues with relative imports
- Resolved configuration loading problems
- Fixed streaming output formatting
- Corrected provider initialization errors

### 🚀 Performance
- Faster startup time with lazy loading
- Reduced memory footprint
- Optimized API calls with better error handling
- Improved response streaming

## [1.x] - Previous Versions

Previous versions were development releases with experimental features.
See git history for detailed changes in the development phase.
