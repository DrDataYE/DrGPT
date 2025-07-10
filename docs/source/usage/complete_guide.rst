Usage Guide
===========

This comprehensive guide covers all DrGPT features, modes, and command-line options.

Basic Syntax
------------

.. code-block:: bash

   drgpt [OPTIONS] "your prompt here"

Essential Options
-----------------

Mode Selection
~~~~~~~~~~~~~~

.. list-table:: Available Modes
   :widths: 30 15 55
   :header-rows: 1

   * - Long Option
     - Short
     - Description
   * - Default (no flag)
     - 
     - Standard AI assistant for general questions
   * - ``--code``
     - ``-c``
     - Generate code only (no explanations)
   * - ``--shell``
     - ``-s``
     - Generate shell commands with execution options
   * - ``--interface``
     - ``-i``
     - Start interactive AI interface
   * - ``--chat SESSION_ID``
     - ``-ch``
     - Start or continue a chat session
   * - ``--editor``
     - ``-e``
     - Open text editor for input composition

Output Options
~~~~~~~~~~~~~~

.. list-table:: Output Control
   :widths: 30 15 55
   :header-rows: 1

   * - Long Option
     - Short
     - Description
   * - ``--output FILE``
     - ``-o``
     - Save response to file
   * - ``--no-markdown``
     - 
     - Disable markdown rendering (plain text only)
   * - ``--no-streaming``
     - 
     - Disable streaming output
   * - ``--streaming``
     - 
     - Enable streaming output (default)

Provider Options
~~~~~~~~~~~~~~~~

.. code-block:: bash

   --provider PROVIDER     # Choose AI provider (openai, anthropic, google)
   --model MODEL          # Specify model to use
   --api-key KEY          # Set API key for provider
   --list-providers       # Show all available providers
   --list-models PROVIDER # Show models for specific provider

AI Parameters
~~~~~~~~~~~~~

.. code-block:: bash

   --temperature TEMP     # Set creativity level (0.0-2.0)
   --max-tokens TOKENS    # Limit response length

Detailed Examples
-----------------

Standard Mode (Default)
~~~~~~~~~~~~~~~~~~~~~~~

Best for general questions, explanations, and discussions:

.. code-block:: bash

   # General questions
   drgpt "What is machine learning?"
   
   # Technical explanations
   drgpt "Explain how Docker containers work"
   
   # Writing assistance
   drgpt "Help me write a professional email about project delays"

Code Mode (-c/--code)
~~~~~~~~~~~~~~~~~~~~~

Pure code generation without explanations:

.. code-block:: bash

   # Python functions
   drgpt -c "Create a function to validate email addresses"
   
   # Web development
   drgpt -c "Create a responsive CSS grid layout"
   
   # Database queries
   drgpt -c "Write SQL to find duplicate records in users table"
   
   # Save code to file
   drgpt -c -o utils.py "Create utility functions for file handling"

Shell Mode (-s/--shell)
~~~~~~~~~~~~~~~~~~~~~~~

System administration and command generation:

.. code-block:: bash

   # File operations
   drgpt -s "Find all log files older than 30 days"
   
   # System monitoring
   drgpt -s "Show memory usage by process"
   
   # Package management
   drgpt -s "Install Python development tools on Ubuntu"
   
   # Network diagnostics
   drgpt -s "Test connection to multiple servers"

Interactive Mode (-i/--interface)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Continuous conversation with special commands:

.. code-block:: bash

   # Start interactive session
   drgpt -i
   
   # Inside interactive mode:
   > !What is Kubernetes?
   > code: Create a Kubernetes deployment YAML
   > shell: Install kubectl on my system
   > help
   > exit

Editor Mode (-e/--editor)
~~~~~~~~~~~~~~~~~~~~~~~~~

Compose complex prompts in your preferred text editor:

.. code-block:: bash

   # Open editor for input
   drgpt -e
   
   # Combine with other modes
   drgpt -e -c  # Editor + code mode
   drgpt -e -s  # Editor + shell mode

Chat Sessions (-ch/--chat)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Persistent conversations with context:

.. code-block:: bash

   # Start new chat session
   drgpt -ch project_planning "Let's plan a web application"
   
   # Continue existing session
   drgpt -ch project_planning "Now let's discuss the database design"
   
   # List active sessions
   drgpt --list-sessions

Advanced Usage
--------------

Combining Options
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Code generation with custom parameters
   drgpt -c --temperature 0.2 "Create a secure password generator"
   
   # Shell commands with output saving
   drgpt -s -o backup_script.sh "Create automated backup script"
   
   # Interactive mode with specific provider
   drgpt -i --provider anthropic --model claude-3-sonnet
   
   # Non-streaming output to file
   drgpt --no-streaming -o analysis.md "Analyze current AI trends"

Provider Management
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Set default provider
   drgpt --provider openai --api-key YOUR_KEY --save-config
   
   # Use different provider for one query
   drgpt --provider anthropic "Explain quantum computing"
   
   # Check current configuration
   drgpt --status
   
   # List all providers and models
   drgpt --list-providers

Output Formats
~~~~~~~~~~~~~~

By default, DrGPT outputs responses in markdown format for better readability. You can control this behavior:

.. code-block:: bash

   # Default: Beautiful markdown formatting
   drgpt "Explain Python decorators"
   
   # Plain text output (no formatting)
   drgpt --no-markdown "Explain Python decorators"
   
   # Save formatted output to file
   drgpt -o explanation.md "Explain Python decorators"
   
   # Save plain text to file
   drgpt --no-markdown -o explanation.txt "Explain Python decorators"

Error Handling
--------------

Common Issues
~~~~~~~~~~~~~

**API Key Not Set:**

.. code-block:: bash

   # Set API key for provider
   drgpt --provider openai --api-key YOUR_OPENAI_KEY
   
   # Or use environment variable
   export OPENAI_API_KEY="your-key-here"

**Model Not Available:**

.. code-block:: bash

   # Check available models
   drgpt --list-models openai
   
   # Use specific model
   drgpt --provider openai --model gpt-4 "Your prompt"

**Command Execution (Shell Mode):**

.. code-block:: bash

   # If command seems unsafe, choose [D]escribe option
   drgpt -s "Delete all temporary files"
   # Output: [E]xecute, [D]escribe, [A]bort
   # Choose 'D' to understand what the command does

Environment Setup
-----------------

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Windows PowerShell
   $env:OPENAI_API_KEY = "your-api-key"
   $env:ANTHROPIC_API_KEY = "your-api-key"
   $env:GOOGLE_API_KEY = "your-api-key"
   
   # Linux/macOS
   export OPENAI_API_KEY="your-api-key"
   export ANTHROPIC_API_KEY="your-api-key"
   export GOOGLE_API_KEY="your-api-key"

Editor Configuration
~~~~~~~~~~~~~~~~~~~~

DrGPT respects standard editor environment variables:

.. code-block:: bash

   # Set preferred editor
   export EDITOR="code"        # VS Code
   export EDITOR="nano"        # nano
   export EDITOR="vim"         # vim
   export VISUAL="code --wait" # VS Code with wait

Configuration File
~~~~~~~~~~~~~~~~~~

DrGPT stores configuration in ``~/.config/drgpt/config``:

.. code-block:: ini

   [DEFAULT]
   provider = openai
   model = gpt-4
   temperature = 0.7
   max_tokens = 2000
   markdown = true
   streaming = true

Tips and Best Practices
-----------------------

Effective Prompting
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Be specific for better results
   drgpt -c "Create a Python function that validates email addresses using regex and handles common edge cases"
   
   # Use examples in your prompts
   drgpt "Explain list comprehensions in Python with 3 practical examples"
   
   # Ask for specific formats
   drgpt -c "Create a REST API endpoint that returns JSON with error handling"

Shell Mode Safety
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Always review commands before execution
   drgpt -s "Clean up Docker containers and images"
   # Choose [D]escribe first to understand the command
   
   # Use for learning system administration
   drgpt -s "Show me how to configure nginx with SSL"

Code Organization
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Generate and save related code files
   drgpt -c -o models.py "Create SQLAlchemy models for a blog"
   drgpt -c -o views.py "Create Flask views for the blog models"
   drgpt -c -o templates.html "Create HTML templates for the blog"

Interactive Workflows
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Use interactive mode for complex projects
   drgpt -i
   > !I'm building a Python web scraper
   > code: Create the main scraper class
   > shell: Install required dependencies
   > code: Add error handling and logging
   > exit

Troubleshooting
---------------

Getting Help
~~~~~~~~~~~~

.. code-block:: bash

   # Built-in help
   drgpt --help
   
   # Interactive mode help
   drgpt -i
   > help
   
   # Check current status
   drgpt --status
   
   # Version information
   drgpt --version

Performance Tips
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Use smaller models for simple tasks
   drgpt --model gpt-3.5-turbo "Simple question"
   
   # Disable streaming for faster processing
   drgpt --no-streaming "Quick code snippet"
   
   # Use appropriate temperature
   drgpt --temperature 0.1 -c "Precise code generation"
   drgpt --temperature 0.8 "Creative writing task"
