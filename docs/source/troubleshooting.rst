Troubleshooting
===============

Common issues and solutions for DrGPT installation, configuration, and usage.

Installation Issues
-------------------

Package Installation Problems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Issue**: ``pip install drgpt`` fails with permission errors

**Solutions**:

.. code-block:: bash

   # Option 1: Use --user flag
   pip install --user drgpt
   
   # Option 2: Use virtual environment
   python -m venv drgpt-env
   source drgpt-env/bin/activate  # Linux/macOS
   drgpt-env\Scripts\activate     # Windows
   pip install drgpt
   
   # Option 3: Use sudo (Linux/macOS only, not recommended)
   sudo pip install drgpt

**Issue**: ``drgpt`` command not found after installation

**Solutions**:

.. code-block:: bash

   # Check if installed with --user
   echo $PATH | grep -o ~/.local/bin  # Linux/macOS
   
   # Add to PATH if needed
   export PATH="$HOME/.local/bin:$PATH"  # Linux/macOS
   
   # Or use full path
   ~/.local/bin/drgpt "Your question"
   
   # Windows: Check user installation directory
   pip show drgpt

**Issue**: Python version compatibility errors

**Solutions**:

.. code-block:: bash

   # Check Python version
   python --version
   
   # DrGPT requires Python 3.8+
   # Update Python or use pyenv/conda for version management
   
   # Install specific Python version with pyenv
   pyenv install 3.10.0
   pyenv local 3.10.0

Dependency Issues
~~~~~~~~~~~~~~~~~

**Issue**: Conflicting package versions

**Solutions**:

.. code-block:: bash

   # Create clean virtual environment
   python -m venv fresh-env
   source fresh-env/bin/activate
   pip install drgpt
   
   # Or update pip first
   pip install --upgrade pip
   pip install drgpt

**Issue**: SSL certificate errors during installation

**Solutions**:

.. code-block:: bash

   # Update certificates
   pip install --trusted-host pypi.org --trusted-host pypi.python.org drgpt
   
   # Or upgrade pip and certificates
   pip install --upgrade pip certifi

Configuration Issues
--------------------

API Key Problems
~~~~~~~~~~~~~~~~

**Issue**: "API key not found" or "Invalid API key" errors

**Solutions**:

.. code-block:: bash

   # Verify environment variable is set
   echo $OPENAI_API_KEY
   echo $ANTHROPIC_API_KEY
   echo $GOOGLE_API_KEY
   
   # Set API key for current session
   export OPENAI_API_KEY="sk-your-key-here"
   
   # For persistent setup, add to shell profile
   echo 'export OPENAI_API_KEY="sk-your-key-here"' >> ~/.bashrc
   source ~/.bashrc
   
   # Test API key
   drgpt --provider openai "test"

**Issue**: API key works in terminal but not in scripts

**Solutions**:

.. code-block:: bash

   # Make sure environment variables are available to scripts
   #!/bin/bash
   source ~/.bashrc  # or ~/.zshrc
   drgpt "Your question"
   
   # Or set variables in script
   #!/bin/bash
   export OPENAI_API_KEY="sk-your-key"
   drgpt "Your question"

**Issue**: Wrong API key format

**Solutions**:

.. code-block:: bash

   # OpenAI keys start with "sk-"
   # Anthropic keys start with "sk-ant-"
   # Google keys are typically alphanumeric
   
   # Verify key format
   drgpt --provider openai --api-key "sk-your-correct-key" "test"

Provider Configuration Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Issue**: Provider not available or not found

**Solutions**:

.. code-block:: bash

   # List available providers
   drgpt --list-providers
   
   # Check current configuration
   drgpt --status
   
   # Set provider explicitly
   drgpt --provider openai "Your question"

**Issue**: Model not available for provider

**Solutions**:

.. code-block:: bash

   # List models for specific provider
   drgpt --provider openai --list-models
   
   # Use default model
   drgpt --provider openai "Your question"
   
   # Specify valid model
   drgpt --provider openai --model gpt-4o-mini "Your question"

**Issue**: Configuration file errors

**Solutions**:

.. code-block:: bash

   # Check configuration file location
   # Linux/macOS: ~/.config/drgpt/config
   # Windows: %APPDATA%\drgpt\config
   
   # Reset configuration
   rm ~/.config/drgpt/config
   drgpt --status  # Will recreate with defaults
   
   # Use custom configuration
   drgpt --config /path/to/custom/config "Your question"

Network and API Issues
----------------------

Connection Problems
~~~~~~~~~~~~~~~~~~~

**Issue**: Network timeout or connection refused

**Solutions**:

.. code-block:: bash

   # Check internet connection
   ping google.com
   
   # Use longer timeout
   drgpt --timeout 60 "Your question"
   
   # Check if behind proxy
   export HTTP_PROXY=http://proxy.company.com:8080
   export HTTPS_PROXY=http://proxy.company.com:8080
   
   # Test with debug mode
   drgpt --debug "Your question"

**Issue**: SSL certificate verification errors

**Solutions**:

.. code-block:: bash

   # Update certificates
   pip install --upgrade certifi
   
   # Check system time (SSL depends on correct time)
   date
   
   # For corporate networks, you may need custom certificates
   export SSL_CERT_FILE=/path/to/company/cert.pem

Rate Limiting and Quota Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Issue**: "Rate limit exceeded" errors

**Solutions**:

.. code-block:: bash

   # Wait and retry
   sleep 60
   drgpt "Your question"
   
   # Use different provider
   drgpt --provider anthropic "Your question"
   
   # Use lower-tier model
   drgpt --provider openai --model gpt-3.5-turbo "Your question"

**Issue**: Quota exceeded or billing issues

**Solutions**:

.. code-block:: bash

   # Check account usage at provider's website
   # OpenAI: https://platform.openai.com/usage
   # Anthropic: https://console.anthropic.com/
   
   # Use alternative provider
   drgpt --provider google "Your question"

Mode-Specific Issues
--------------------

Code Mode Problems
~~~~~~~~~~~~~~~~~~

**Issue**: Code mode returns explanations instead of just code

**Solutions**:

.. code-block:: bash

   # Make sure to use --code flag
   drgpt --code "Create a function"  # Correct
   
   # Not this:
   drgpt "Create a function"  # This is standard mode

**Issue**: Generated code has syntax errors

**Solutions**:

.. code-block:: bash

   # Be more specific about language and requirements
   drgpt --code "Create a Python function with error handling to read CSV files"
   
   # Request specific coding style
   drgpt --code "Create a JavaScript function using ES6 syntax for API calls"

Shell Mode Problems
~~~~~~~~~~~~~~~~~~~

**Issue**: Shell commands not working on my system

**Solutions**:

.. code-block:: bash

   # Specify your operating system
   drgpt --shell "Install Docker on Ubuntu 20.04"
   drgpt --shell "Windows PowerShell command to list services"
   
   # Use describe option to understand commands
   drgpt --shell "Complex system command"
   # Choose [D]escribe to understand before executing

**Issue**: Permission denied when executing commands

**Solutions**:

.. code-block:: bash

   # Request commands with proper permissions
   drgpt --shell "Install software with sudo on Linux"
   
   # Or run generated commands manually with appropriate permissions
   sudo [generated_command]

Editor Mode Problems
~~~~~~~~~~~~~~~~~~~

**Issue**: vi editor not found or won't open

**Solutions**:

.. code-block:: bash

   # Check if vi is installed
   which vi
   
   # Install vi/vim if missing
   # Ubuntu/Debian:
   sudo apt-get install vim
   
   # CentOS/RHEL:
   sudo yum install vim
   
   # macOS (should be pre-installed):
   # Install Xcode command line tools
   xcode-select --install
   
   # Windows:
   # Install Git for Windows (includes vim)
   # Or use WSL

**Issue**: Don't know how to use vi

**Solutions**:

.. code-block:: bash

   # Basic vi commands:
   # i = insert mode
   # Esc = command mode
   # :wq = save and quit
   # :q! = quit without saving
   
   # Alternative: Set EDITOR environment variable to preferred editor
   export EDITOR=nano  # Use nano instead
   drgpt --editor

Interface Mode Problems
~~~~~~~~~~~~~~~~~~~~~~

**Issue**: Interactive mode commands not recognized

**Solutions**:

.. code-block:: bash

   # Make sure to use ! before AI queries
   > ! Your question    # Correct
   > Your question      # Wrong - will show "Unknown command"
   
   # Use built-in commands without !
   > help              # Show available commands
   > status            # Show current status

**Issue**: Session loses context

**Solutions**:

.. code-block:: bash

   # Context is maintained within single session
   # Start fresh session for new topics
   > exit
   drgpt --interface
   
   # Use specific questions to rebuild context
   > ! Continuing from our previous discussion about Docker...

Performance Issues
------------------

Slow Response Times
~~~~~~~~~~~~~~~~~~~

**Issue**: DrGPT responses are very slow

**Solutions**:

.. code-block:: bash

   # Use faster models
   drgpt --provider openai --model gpt-4o-mini "Your question"
   
   # Disable streaming for perceived faster completion
   drgpt --no-streaming "Your question"
   
   # Use shorter prompts
   drgpt "Brief explanation of X"
   
   # Check network connection
   drgpt --debug "Your question"  # Shows timing information

**Issue**: High memory usage

**Solutions**:

.. code-block:: bash

   # Restart interactive sessions periodically
   drgpt --interface
   > exit
   drgpt --interface
   
   # Use shorter context windows
   drgpt --max-tokens 500 "Your question"

Output Issues
-------------

Formatting Problems
~~~~~~~~~~~~~~~~~~~

**Issue**: Markdown not rendering properly

**Solutions**:

.. code-block:: bash

   # Check if terminal supports colors
   echo $TERM
   
   # Use plain text mode
   drgpt --no-markdown "Your question"
   
   # Update rich library
   pip install --upgrade rich

**Issue**: Output too long or cluttered

**Solutions**:

.. code-block:: bash

   # Request shorter responses
   drgpt --max-tokens 500 "Brief explanation"
   
   # Use clear screen in interactive mode
   drgpt --interface
   > clear
   
   # Save long outputs to file
   drgpt --output result.md "Detailed analysis"

Character Encoding Issues
~~~~~~~~~~~~~~~~~~~~~~~~~

**Issue**: Special characters not displaying correctly

**Solutions**:

.. code-block:: bash

   # Set UTF-8 encoding
   export LANG=en_US.UTF-8
   export LC_ALL=en_US.UTF-8
   
   # Windows Command Prompt:
   chcp 65001
   
   # Use plain text mode if encoding issues persist
   drgpt --no-markdown "Your question"

Platform-Specific Issues
------------------------

Windows Issues
~~~~~~~~~~~~~~

**Issue**: PowerShell execution policy errors

**Solutions**:

.. code-block:: powershell

   # Check current policy
   Get-ExecutionPolicy
   
   # Allow script execution (as administrator)
   Set-ExecutionPolicy RemoteSigned
   
   # Or run with bypass
   powershell -ExecutionPolicy Bypass -Command "drgpt 'Your question'"

**Issue**: Path issues with Python/pip

**Solutions**:

.. code-block:: cmd

   # Check Python installation
   python --version
   py --version
   
   # Use Python launcher
   py -m pip install drgpt
   py -m drgpt "Your question"

macOS Issues
~~~~~~~~~~~~

**Issue**: Command not found after installation

**Solutions**:

.. code-block:: bash

   # Check PATH includes pip install location
   echo $PATH
   
   # Add to PATH in ~/.zshrc (macOS Catalina+)
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc

**Issue**: Permission denied for system directories

**Solutions**:

.. code-block:: bash

   # Use --user installation
   pip install --user drgpt
   
   # Or use Homebrew Python
   brew install python
   pip3 install drgpt

Linux Issues
~~~~~~~~~~~~

**Issue**: Missing system dependencies

**Solutions**:

.. code-block:: bash

   # Install required packages
   # Ubuntu/Debian:
   sudo apt-get update
   sudo apt-get install python3-pip python3-venv
   
   # CentOS/RHEL:
   sudo yum install python3-pip
   
   # Arch Linux:
   sudo pacman -S python-pip

Debug Mode and Logging
----------------------

Using Debug Mode
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Enable debug output
   drgpt --debug "Your question"
   
   # Shows:
   # - API request details
   # - Response timing
   # - Configuration used
   # - Error details

**Issue**: Need more detailed logging

**Solutions**:

.. code-block:: bash

   # Verbose mode
   drgpt --verbose "Your question"
   
   # Save debug output
   drgpt --debug "Your question" 2> debug.log
   
   # Check configuration
   drgpt --status

Common Error Messages
---------------------

"Command not found: drgpt"
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Cause**: DrGPT not installed or not in PATH

**Solution**: Follow installation troubleshooting above

"Invalid API key"
~~~~~~~~~~~~~~~~~

**Cause**: API key not set, wrong format, or expired

**Solution**: Verify and reset API key

"Provider not available"
~~~~~~~~~~~~~~~~~~~~~~~~

**Cause**: Invalid provider name or missing configuration

**Solution**: Use ``drgpt --list-providers`` to see available options

"Connection timeout"
~~~~~~~~~~~~~~~~~~~~

**Cause**: Network issues or API service problems

**Solution**: Check network, try different provider, or increase timeout

"Rate limit exceeded"
~~~~~~~~~~~~~~~~~~~~

**Cause**: Too many API requests in short time

**Solution**: Wait and retry, or use different provider/model

Getting Help
------------

If you continue having issues:

1. **Check GitHub Issues**: https://github.com/DrDataYE/drgpt/issues
2. **Use Debug Mode**: ``drgpt --debug "Your question"``
3. **Check Configuration**: ``drgpt --status``
4. **Create Issue**: Include debug output and system information

System Information for Bug Reports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When reporting issues, include:

.. code-block:: bash

   # System information
   python --version
   pip show drgpt
   drgpt --version
   echo $SHELL
   echo $OS # or uname -a on Linux/macOS
   
   # Configuration
   drgpt --status
   
   # Debug output
   drgpt --debug "test question" 2>&1

This information helps diagnose and resolve issues quickly.
