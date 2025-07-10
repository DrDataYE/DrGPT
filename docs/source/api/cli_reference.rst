CLI Reference
=============

Complete command-line interface reference for DrGPT with all options, flags, and usage patterns.

Synopsis
--------

.. code-block:: bash

   drgpt [OPTIONS] [PROMPT]

Basic Usage
-----------

.. code-block:: bash

   # Simple query
   drgpt "Your question here"
   
   # Use specific mode
   drgpt --code "Generate code"
   drgpt --shell "System command"
   drgpt --interface
   drgpt --editor

Positional Arguments
--------------------

``PROMPT``
~~~~~~~~~~

The question or request to send to the AI.

* **Type**: String
* **Required**: No (unless using standard mode)
* **Default**: None

.. code-block:: bash

   # Basic prompt
   drgpt "Explain machine learning"
   
   # Multi-word prompts (quotes recommended)
   drgpt "How do I optimize database queries for large datasets?"

Mode Options
------------

``--code``
~~~~~~~~~~

Generate pure code without explanations.

* **Type**: Flag (no arguments)
* **Default**: False

.. code-block:: bash

   # Generate Python function
   drgpt --code "Create a function to sort a list"
   
   # Generate with specific language
   drgpt --code "Create a React component for user authentication"

``--shell``
~~~~~~~~~~~

Generate system administration commands with interactive execution.

* **Type**: Flag (no arguments)
* **Default**: False

.. code-block:: bash

   # Generate system command
   drgpt --shell "Find all Python files larger than 1MB"
   
   # Package management
   drgpt --shell "Install Docker on Ubuntu"

``--interface``
~~~~~~~~~~~~~~~

Start interactive AI chat mode.

* **Type**: Flag (no arguments)
* **Default**: False

.. code-block:: bash

   # Start interactive session
   drgpt --interface

``--editor``
~~~~~~~~~~~~

Open vi text editor for prompt composition.

* **Type**: Flag (no arguments)
* **Default**: False

.. code-block:: bash

   # Open editor for complex prompts
   drgpt --editor

Provider Options
----------------

``--provider PROVIDER``
~~~~~~~~~~~~~~~~~~~~~~~

Specify AI provider to use.

* **Type**: String
* **Choices**: ``openai``, ``anthropic``, ``google``
* **Default**: From configuration or ``openai``

.. code-block:: bash

   # Use OpenAI
   drgpt --provider openai "Your question"
   
   # Use Anthropic
   drgpt --provider anthropic "Your question"
   
   # Use Google AI
   drgpt --provider google "Your question"

``--model MODEL``
~~~~~~~~~~~~~~~~~

Specify AI model to use.

* **Type**: String
* **Default**: Provider-specific default

**OpenAI Models**:
- ``gpt-4``
- ``gpt-4o-mini`` (default)
- ``gpt-3.5-turbo``

**Anthropic Models**:
- ``claude-3-opus-20240229``
- ``claude-3-sonnet-20240229`` (default)
- ``claude-3-haiku-20240307``

**Google Models**:
- ``gemini-pro`` (default)

.. code-block:: bash

   # Specific model
   drgpt --provider openai --model gpt-4 "Complex reasoning task"
   
   # Cost-effective model
   drgpt --provider openai --model gpt-4o-mini "Simple question"

``--list-providers``
~~~~~~~~~~~~~~~~~~~~

List all available providers and models.

* **Type**: Flag (no arguments)

.. code-block:: bash

   # Show all providers and models
   drgpt --list-providers

``--api-key API_KEY``
~~~~~~~~~~~~~~~~~~~~~

Set API key for the current provider.

* **Type**: String
* **Security**: Key is stored securely in configuration

.. code-block:: bash

   # Set OpenAI key
   drgpt --provider openai --api-key "sk-your-key-here"
   
   # Set Anthropic key
   drgpt --provider anthropic --api-key "sk-ant-your-key-here"

Output Options
--------------

``--output FILE``
~~~~~~~~~~~~~~~~~

Save response to file.

* **Type**: String (file path)
* **Default**: None (output to terminal)

.. code-block:: bash

   # Save to file
   drgpt --output response.md "Explain Docker architecture"
   
   # Save with specific format
   drgpt --code --output code.py "Create a web scraper"

``--no-streaming``
~~~~~~~~~~~~~~~~~~

Disable real-time response streaming.

* **Type**: Flag (no arguments)
* **Default**: False (streaming enabled)

.. code-block:: bash

   # Get complete response at once
   drgpt --no-streaming "Explain quantum computing"

``--no-markdown``
~~~~~~~~~~~~~~~~~

Disable markdown formatting in output.

* **Type**: Flag (no arguments)
* **Default**: False (markdown enabled)

.. code-block:: bash

   # Plain text output
   drgpt --no-markdown "Simple explanation"
   
   # Useful for scripts
   RESPONSE=$(drgpt --no-markdown "Brief answer")

Configuration Options
---------------------

``--status``
~~~~~~~~~~~~

Show current configuration and provider status.

* **Type**: Flag (no arguments)

.. code-block:: bash

   # Show current settings
   drgpt --status

``--set-default``
~~~~~~~~~~~~~~~~~

Set current provider and model as default.

* **Type**: Flag (no arguments)
* **Requires**: ``--provider`` and optionally ``--model``

.. code-block:: bash

   # Set OpenAI as default
   drgpt --provider openai --model gpt-4 --set-default

Advanced Options
----------------

``--temperature TEMP``
~~~~~~~~~~~~~~~~~~~~~~

Control response creativity and randomness.

* **Type**: Float
* **Range**: 0.0 to 1.0
* **Default**: 0.7

.. code-block:: bash

   # More focused responses
   drgpt --temperature 0.1 "Factual explanation"
   
   # More creative responses
   drgpt --temperature 0.9 "Creative writing task"

``--max-tokens TOKENS``
~~~~~~~~~~~~~~~~~~~~~~~

Maximum number of tokens in response.

* **Type**: Integer
* **Default**: Provider-specific default

.. code-block:: bash

   # Shorter responses
   drgpt --max-tokens 500 "Brief summary"
   
   # Longer responses
   drgpt --max-tokens 2000 "Detailed analysis"

``--timeout SECONDS``
~~~~~~~~~~~~~~~~~~~~~

Request timeout in seconds.

* **Type**: Integer
* **Default**: 30

.. code-block:: bash

   # Longer timeout for complex requests
   drgpt --timeout 60 "Complex analysis task"

Debug and Information Options
-----------------------------

``--debug``
~~~~~~~~~~~

Enable debug mode with detailed logging.

* **Type**: Flag (no arguments)
* **Default**: False

.. code-block:: bash

   # Show debug information
   drgpt --debug "Your question"

``--verbose``
~~~~~~~~~~~~~

Enable verbose output.

* **Type**: Flag (no arguments)
* **Default**: False

.. code-block:: bash

   # Verbose logging
   drgpt --verbose "Your question"

``--version``
~~~~~~~~~~~~~

Show DrGPT version information.

* **Type**: Flag (no arguments)

.. code-block:: bash

   # Show version
   drgpt --version

``--help``
~~~~~~~~~~

Show help message and usage information.

* **Type**: Flag (no arguments)

.. code-block:: bash

   # Show help
   drgpt --help

Configuration File Options
--------------------------

``--config CONFIG_FILE``
~~~~~~~~~~~~~~~~~~~~~~~~~

Use specific configuration file.

* **Type**: String (file path)
* **Default**: ``~/.config/drgpt/config``

.. code-block:: bash

   # Use custom config
   drgpt --config ~/my-drgpt-config "Your question"

``--no-config``
~~~~~~~~~~~~~~~

Ignore configuration file and use defaults.

* **Type**: Flag (no arguments)

.. code-block:: bash

   # Use only command-line options
   drgpt --no-config --provider openai "Your question"

Environment Variables
---------------------

DrGPT respects these environment variables:

API Keys
~~~~~~~~

.. code-block:: bash

   OPENAI_API_KEY        # OpenAI API key
   ANTHROPIC_API_KEY     # Anthropic API key
   GOOGLE_API_KEY        # Google AI API key

Default Settings
~~~~~~~~~~~~~~~~

.. code-block:: bash

   DRGPT_DEFAULT_PROVIDER    # Default provider
   DRGPT_DEFAULT_MODEL       # Default model
   DRGPT_NO_STREAMING        # Disable streaming (true/false)
   DRGPT_NO_MARKDOWN         # Disable markdown (true/false)

Advanced Settings
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   DRGPT_CONFIG_DIR          # Configuration directory
   DRGPT_TIMEOUT             # Default timeout
   DRGPT_MAX_TOKENS          # Default max tokens
   DRGPT_TEMPERATURE         # Default temperature

Exit Codes
----------

DrGPT uses these exit codes:

.. code-block:: bash

   0    # Success
   1    # General error
   2    # Configuration error
   3    # Network error
   4    # API error
   5    # User interruption (Ctrl+C)

Usage Examples
--------------

Basic Queries
~~~~~~~~~~~~~

.. code-block:: bash

   # Simple question
   drgpt "What is Docker?"
   
   # Complex question with context
   drgpt "How do I implement JWT authentication in a Node.js API with proper security practices?"

Provider and Model Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Use specific provider
   drgpt --provider anthropic "Analyze this philosophical argument"
   
   # Use specific model for complex task
   drgpt --provider openai --model gpt-4 "Design a distributed system architecture"
   
   # Cost-effective model for simple tasks
   drgpt --provider openai --model gpt-4o-mini "Explain basic concepts"

Mode-Specific Examples
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Code generation
   drgpt --code "Create a Python class for handling HTTP requests"
   
   # System administration
   drgpt --shell "Set up SSL certificate for nginx"
   
   # Complex prompt composition
   drgpt --editor
   
   # Interactive session
   drgpt --interface

Output Control
~~~~~~~~~~~~~~

.. code-block:: bash

   # Save to file
   drgpt --output analysis.md "Analyze current AI trends"
   
   # Plain text for scripting
   RESULT=$(drgpt --no-markdown "Brief answer")
   
   # Immediate formatted output
   drgpt --no-streaming "Detailed explanation"

Configuration Management
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Check current settings
   drgpt --status
   
   # Set new defaults
   drgpt --provider anthropic --model claude-3-sonnet-20240229 --set-default
   
   # Use custom configuration
   drgpt --config ~/.drgpt-work-config "Work-related question"

Troubleshooting Commands
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Debug mode
   drgpt --debug "Your question"
   
   # Test provider connectivity
   drgpt --provider openai --test
   
   # Verbose output
   drgpt --verbose "Your question"

Combining Options
-----------------

Multiple options can be combined:

.. code-block:: bash

   # Code generation with specific provider and output
   drgpt --provider anthropic --code --output webapp.py "Create a Flask web application"
   
   # Shell command with debug and custom timeout
   drgpt --shell --debug --timeout 60 "Complex system maintenance task"
   
   # Interactive mode with specific provider
   drgpt --interface --provider openai --model gpt-4

Option Precedence
-----------------

When the same setting is specified in multiple places, DrGPT uses this precedence order:

1. **Command-line options** (highest precedence)
2. **Environment variables**
3. **Configuration file**
4. **Built-in defaults** (lowest precedence)

Example:

.. code-block:: bash

   # Environment variable
   export DRGPT_DEFAULT_PROVIDER="anthropic"
   
   # Command-line override (takes precedence)
   drgpt --provider openai "Your question"  # Uses OpenAI, not Anthropic

Shell Integration
-----------------

DrGPT works well with shell features:

Pipes
~~~~~

.. code-block:: bash

   # Pipe file content
   cat error.log | drgpt "Analyze this error log"
   
   # Chain with other commands
   drgpt --no-markdown "Brief answer" | grep "keyword"

Command Substitution
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Use DrGPT output in variables
   EXPLANATION=$(drgpt --no-markdown "Explain $TERM")
   
   # Use in other commands
   echo "AI says: $(drgpt --no-markdown 'Brief answer')"

Scripting
~~~~~~~~~

.. code-block:: bash

   #!/bin/bash
   # Script example
   
   # Check if DrGPT is available
   if ! command -v drgpt &> /dev/null; then
       echo "DrGPT not found"
       exit 1
   fi
   
   # Get AI assistance
   ADVICE=$(drgpt --no-markdown --provider openai "How to optimize $1")
   echo "Optimization advice: $ADVICE"

See Also
--------

* :doc:`../configuration` - Configuration file format and options
* :doc:`../modes/standard` - Detailed mode documentation
* :doc:`../features/providers` - Provider-specific information
* :doc:`../troubleshooting` - Common issues and solutions
