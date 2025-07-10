CLI Reference
=============

Quick reference for all DrGPT command-line options and shortcuts.

Command Syntax
--------------

.. code-block:: bash

   drgpt [OPTIONS] "prompt"

Essential Shortcuts
-------------------

.. list-table:: Most Used Options
   :widths: 20 10 15 55
   :header-rows: 1

   * - Option
     - Short
     - Type
     - Description
   * - ``--code``
     - ``-c``
     - Mode
     - Generate code only (no explanations)
   * - ``--shell``
     - ``-s``
     - Mode
     - Interactive shell command generation
   * - ``--interface``
     - ``-i``
     - Mode
     - Start interactive AI interface
   * - ``--editor``
     - ``-e``
     - Input
     - Open text editor for prompt composition
   * - ``--chat``
     - ``-ch``
     - Mode
     - Start/continue chat session
   * - ``--output``
     - ``-o``
     - Output
     - Save response to file

Quick Examples
--------------

Basic Usage
~~~~~~~~~~~

.. code-block:: bash

   # Standard query
   drgpt "Explain quantum computing"
   
   # Code generation
   drgpt -c "Create a Python class for user management"
   
   # Shell commands
   drgpt -s "Find large files in current directory"
   
   # Interactive mode
   drgpt -i
   
   # Editor mode
   drgpt -e
   
   # Save output
   drgpt -o result.md "Explain machine learning"

Combined Options
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Code to file
   drgpt -c -o script.py "Create a web scraper"
   
   # Shell with editor
   drgpt -e -s  # Compose complex shell task in editor
   
   # Chat with specific provider
   drgpt -ch session1 --provider anthropic "Discuss AI ethics"

All Command Options
-------------------

Modes
~~~~~

.. code-block:: bash

   # Default mode (no flag needed)
   drgpt "Your question"
   
   # Code generation mode
   --code, -c
   
   # Shell command mode  
   --shell, -s
   
   # Interactive interface
   --interface, -i
   
   # Text editor input
   --editor, -e
   
   # Chat sessions
   --chat SESSION_ID, -ch SESSION_ID

Input/Output
~~~~~~~~~~~~

.. code-block:: bash

   # Save response to file
   --output FILE, -o FILE
   
   # Disable markdown rendering
   --no-markdown
   
   # Control streaming
   --streaming (default)
   --no-streaming

Provider Management
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Select provider
   --provider PROVIDER
   
   # Select model
   --model MODEL
   
   # Set API key
   --api-key KEY
   
   # List providers
   --list-providers
   
   # List models for provider
   --list-models PROVIDER

AI Parameters
~~~~~~~~~~~~~

.. code-block:: bash

   # Set creativity (0.0-2.0)
   --temperature FLOAT
   
   # Limit response length
   --max-tokens INTEGER

Utility
~~~~~~~

.. code-block:: bash

   # Show help
   --help, -h
   
   # Show version
   --version
   
   # Show current configuration
   --status

Common Combinations
-------------------

Development Workflow
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Generate code and save
   drgpt -c -o utils.py "Create utility functions"
   
   # Edit complex prompt, generate code
   drgpt -e -c "Complex coding task"
   
   # Interactive development session
   drgpt -i
   > code: Create main application structure
   > code: Add error handling
   > shell: Set up virtual environment

System Administration
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Generate system commands
   drgpt -s "Monitor system performance"
   
   # Complex system tasks with editor
   drgpt -e -s  # Compose multi-step task
   
   # Save automation scripts
   drgpt -s -o backup.sh "Create backup script"

Content Creation
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Long-form content with editor
   drgpt -e "Write documentation"
   
   # Save content to file
   drgpt -o article.md "Write about AI trends"
   
   # Plain text output
   drgpt --no-markdown -o notes.txt "Meeting notes"

Environment Variables
---------------------

API Keys
~~~~~~~~

.. code-block:: bash

   # Windows PowerShell
   $env:OPENAI_API_KEY = "your-key"
   $env:ANTHROPIC_API_KEY = "your-key"
   $env:GOOGLE_API_KEY = "your-key"
   
   # Linux/macOS Bash/Zsh
   export OPENAI_API_KEY="your-key"
   export ANTHROPIC_API_KEY="your-key"
   export GOOGLE_API_KEY="your-key"

Configuration
~~~~~~~~~~~~~

.. code-block:: bash

   # Default provider
   export DRGPT_DEFAULT_PROVIDER="openai"
   export DRGPT_DEFAULT_MODEL="gpt-4"
   
   # Editor preference
   export EDITOR="code"
   export VISUAL="code --wait"

Exit Codes
----------

.. list-table:: Exit Status Codes
   :widths: 20 80
   :header-rows: 1

   * - Code
     - Meaning
   * - 0
     - Success
   * - 1
     - General error (invalid arguments, API error)
   * - 2
     - Invalid configuration
   * - 130
     - Interrupted by user (Ctrl+C)

Shell Integration
-----------------

Bash/Zsh Aliases
~~~~~~~~~~~~~~~~

Add to your ``.bashrc`` or ``.zshrc``:

.. code-block:: bash

   # Common shortcuts
   alias ask="drgpt"
   alias code="drgpt -c"
   alias cmd="drgpt -s"
   alias ai="drgpt -i"
   
   # Save to files
   alias gencode="drgpt -c -o"
   alias gencmd="drgpt -s -o"

PowerShell Aliases
~~~~~~~~~~~~~~~~~~

Add to your PowerShell profile:

.. code-block:: powershell

   # Common shortcuts
   Set-Alias ask drgpt
   Set-Alias ai drgpt
   
   # Functions for complex aliases
   function code { drgpt -c $args }
   function cmd { drgpt -s $args }
   function aichat { drgpt -i }

File Extensions
---------------

Recommended file extensions when saving output:

.. code-block:: bash

   # Code files
   drgpt -c -o script.py "Python code"
   drgpt -c -o component.jsx "React component"
   drgpt -c -o styles.css "CSS styling"
   drgpt -c -o query.sql "Database query"
   
   # Shell scripts
   drgpt -s -o backup.sh "Backup script"
   drgpt -s -o deploy.ps1 "PowerShell deployment"
   
   # Documentation
   drgpt -o README.md "Project documentation"
   drgpt -o notes.txt "Plain text notes"
   drgpt --no-markdown -o data.csv "CSV data"

Performance Notes
-----------------

Response Speed
~~~~~~~~~~~~~~

.. code-block:: bash

   # Faster for simple tasks
   --model gpt-3.5-turbo
   
   # Better for complex tasks
   --model gpt-4
   
   # Immediate output (no streaming)
   --no-streaming

Resource Usage
~~~~~~~~~~~~~~

.. code-block:: bash

   # Limit response length
   --max-tokens 500
   
   # More focused responses
   --temperature 0.1
   
   # More creative responses
   --temperature 0.8
