Changelog
=========

All notable changes to DrGPT are documented here.

[2.2.1] - 2025-07-10
---------------------

📚 Complete Documentation Overhaul

Added
~~~~~

* **Comprehensive Sphinx Documentation**: Complete rewrite of all documentation

  * Professional Sphinx-based documentation with modern Furo theme
  * Detailed installation, configuration, and usage guides
  * Full CLI reference with all options and examples
  * Extensive use cases and real-world workflow examples
  * Advanced troubleshooting guide

* **Structured Documentation**: New organized structure with dedicated sections

  * **Modes**: Detailed guides for Standard, Code, Shell, and Interface modes
  * **Features**: In-depth coverage of providers, models, and vi editor integration
  * **API Reference**: Complete CLI command reference
  * **Examples**: Real-world use cases and workflow patterns
  * **Contributing**: Developer guidelines and contribution process

* **Enhanced Editor Integration**: vi editor now consistently used across all platforms

  * Removed OS-specific editor detection
  * Standardized on vi for consistent cross-platform experience
  * Updated help text and documentation to reflect vi usage

Fixed
~~~~~

* **Documentation Build**: Resolved Sphinx build warnings and errors
* **Cross-References**: Fixed all broken internal documentation links
* **Missing Files**: Created required static directories and placeholder files

[2.7.1] - 2025-01-10
---------------------

🚀 Advanced CLI Features & Interactive Modes

Added
~~~~~

* **Enhanced Code Mode** (``--code``): Generate pure code without explanations in markdown format
* **Interactive Shell Mode** (``--shell``): Generate shell commands with interactive execution options

  * Execute commands with user confirmation
  * Describe commands before execution
  * Abort option for safety
  * 5-minute timeout protection
  * Cross-platform command generation

* **vi Text Editor Integration** (``--editor``): Open vi editor for complex prompt composition

  * Consistent vi editor across all platforms (Windows, macOS, Linux)
  * Template structure with helpful comments
  * Comment filtering (lines starting with # are ignored)
  * Temporary file management with automatic cleanup

* **Interactive AI Interface** (``--interface``): Continuous chat mode with advanced features

  * Real-time AI interaction with ``!`` prompt prefix
  * Built-in commands: ``help``, ``status``, ``providers``, ``clear``, ``exit``
  * Special modes: ``code:`` and ``shell:`` prefixes for mode switching
  * Session management and context preservation
  * Rich interactive panels and formatting

Improved
~~~~~~~~

* **Code Generation**: ``--code`` mode now returns pure code without any explanations
* **Shell Commands**: Enhanced safety with confirmation dialogs and detailed command descriptions
* **Cross-Platform Compatibility**: Full support for Windows, macOS, and Linux across all modes
* **User Experience**: Interactive prompts with rich formatting and user-friendly interfaces
* **Error Handling**: Better error messages and graceful failure handling throughout all modes

Technical
~~~~~~~~~

* **Enhanced AI Roles**: Updated system prompts for code-only and shell-only responses
* **Safe Command Execution**: Subprocess execution with timeouts and comprehensive error handling
* **Editor Integration**: Consistent vi editor usage across all platforms
* **Interactive Prompts**: Rich console prompts with choice validation and help systems

Security
~~~~~~~~

* **Safe Command Execution**: User confirmation required before executing any shell commands
* **Timeout Protection**: 5-minute timeout prevents long-running or stuck commands
* **User Confirmation**: Interactive confirmation for potentially dangerous operations
* **Temporary File Security**: Secure handling and cleanup of temporary editor files

[2.1.0] - 2025-01-10
---------------------

✨ Enhanced CLI Output with Rich Markdown Rendering

Added
~~~~~

* **Rich Markdown Rendering**: Beautiful markdown formatting for AI responses

  * Proper headers, code blocks, and bullet points
  * Syntax-highlighted code blocks in responses
  * Formatted tables and lists
  * Rich text styling (bold, italic, etc.)

* **Animated Loading Indicators**: Elegant spinners during response generation in non-streaming mode
* **Formatted Status Panels**: Beautiful panels for status, provider lists, and version information
* **Colorized CLI Output**: Color-coded success, error, and informational messages
* **Flexible Output Options**: New ``--no-markdown`` flag for plain text output when needed
* **Enhanced Streaming**: Real-time streaming with optional formatted preview after completion

Improved
~~~~~~~~

* **User Experience**: More professional and visually appealing terminal interface
* **Code Highlighting**: Syntax-highlighted code blocks in responses for better readability
* **Status Display**: Rich panels with proper formatting for configuration status
* **Error Messages**: Color-coded error messages for better visibility and user experience
* **Provider Lists**: Beautifully formatted provider and model lists with bullet points

Technical
~~~~~~~~~

* **Rich Integration**: Full integration with the ``rich`` library for terminal formatting
* **Backward Compatibility**: All existing functionality preserved with enhanced visuals
* **Performance**: No impact on response generation speed, only improved display quality

[1.0.0] - 2025-01-10
---------------------

🎉 Major Release - Complete Restructure

This is a complete rewrite of DrGPT with professional architecture and improved functionality.

Added
~~~~~

* **New Architecture**: Modular design with ``core``, ``cli``, and provider modules
* **Multi-Provider Support**: OpenAI, Anthropic, Google AI, and extensible custom APIs
* **Professional CLI**: Rich argument parsing with comprehensive help and status commands
* **Configuration Management**: Secure API key storage, provider switching, and persistent settings
* **Cost Optimization**: Default to ``gpt-4o-mini`` (33x cheaper than GPT-4) for cost-effective AI assistance
* **Rich Output**: Beautiful terminal output with syntax highlighting and markdown rendering
* **Streaming Support**: Real-time response streaming for immediate feedback
* **Chat Sessions**: Persistent conversation support with context management
* **Code Generation**: Specialized code and shell command generation modes
* **Status Commands**: View current configuration, provider status, and available models
* **Test Suite**: Comprehensive testing framework for reliability
* **Documentation**: Professional README, developer guides, and comprehensive docs

Changed
~~~~~~~

* **Project Structure**: Moved from ``src/`` to ``drgpt/`` package structure for better organization
* **Entry Points**: New CLI interface with ``drgpt`` command and multiple execution methods
* **Configuration**: Moved from ``~/.config/dr_gpt/`` to ``~/.config/drgpt/`` for consistency
* **Dependencies**: Reduced to core dependencies (``requests``, ``rich``) with optional provider packages
* **API Interface**: Unified interface for all AI providers with consistent error handling
* **Error Handling**: Improved error messages and fallback mechanisms

Removed
~~~~~~~

* **Legacy Structure**: Old ``src/`` directory structure and outdated components
* **Experimental Features**: Removed incomplete plugin system (will be reimplemented in future)
* **Old Scripts**: Removed legacy shell scripts and outdated test files

Migration Guide
~~~~~~~~~~~~~~~

From DrGPT 1.x to 2.0:

.. code-block:: bash

   # Old configuration location
   ~/.config/dr_gpt/config
   
   # New configuration location  
   ~/.config/drgpt/config
   
   # Old command format
   dr-gpt "question"
   
   # New command format
   drgpt "question"

Breaking Changes
~~~~~~~~~~~~~~~~

* **Configuration Path**: Configuration moved to new location
* **Command Name**: Changed from ``dr-gpt`` to ``drgpt``
* **API**: Complete rewrite of internal APIs
* **Dependencies**: Some optional dependencies now require explicit installation

[1.x] - Legacy Versions
-----------------------

Previous versions of DrGPT (1.x series) were experimental and are no longer supported. Users should upgrade to 2.0+ for:

* Better stability and performance
* Professional-grade features
* Comprehensive documentation
* Active maintenance and support

Upgrade Instructions
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Uninstall old version
   pip uninstall dr-gpt
   
   # Install new version
   pip install drgpt
   
   # Reconfigure providers
   drgpt --provider openai --api-key "your-key"
   drgpt --status

Version Support Policy
----------------------

* **Current Version**: Full support with regular updates
* **Previous Minor**: Security fixes only
* **Older Versions**: No support, upgrade recommended

Security Updates
----------------

Security vulnerabilities are addressed in:

* **Current major version**: Immediate patches
* **Previous major version**: Critical security fixes for 6 months
* **Older versions**: No security support

Future Roadmap
--------------

Planned features for upcoming releases:

**v2.7.1** (Planned)
~~~~~~~~~~~~~~~~~~~~

* **Local AI Models**: Support for Ollama and LocalAI
* **Enhanced Editor**: Multiple editor support and customization
* **Plugin System**: Extensible plugin architecture
* **Batch Processing**: Process multiple queries efficiently

**v2.7.1** (Planned)
~~~~~~~~~~~~~~~~~~~~

* **Web Interface**: Optional web UI for DrGPT
* **Team Features**: Shared configurations and collaboration
* **Advanced Analytics**: Usage tracking and optimization suggestions
* **Integration APIs**: RESTful API for integration with other tools

**v3.0.0** (Future)
~~~~~~~~~~~~~~~~~~~

* **AI Agents**: Multi-step AI workflows and automation
* **Knowledge Base**: Personal knowledge management integration
* **Advanced Reasoning**: Enhanced reasoning capabilities
* **Enterprise Features**: Advanced security and management features

Contributing to Changelog
--------------------------

When contributing changes:

1. **Add entries to [Unreleased]** section
2. **Use conventional commit format** for consistency
3. **Categorize changes** appropriately (Added, Changed, Deprecated, Removed, Fixed, Security)
4. **Include migration notes** for breaking changes

Changelog Format
~~~~~~~~~~~~~~~~

This changelog follows `Keep a Changelog <https://keepachangelog.com/>`_ format:

* **Added**: New features
* **Changed**: Changes in existing functionality  
* **Deprecated**: Soon-to-be removed features
* **Removed**: Removed features
* **Fixed**: Bug fixes
* **Security**: Security improvements
