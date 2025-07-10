Configuration
=============

DrGPT offers flexible configuration options to customize its behavior for your needs.

Configuration File
------------------

DrGPT stores its configuration in a local file:

* **Linux/macOS**: ``~/.config/drgpt/config``
* **Windows**: ``%APPDATA%\drgpt\config``

The configuration file is created automatically when you first run DrGPT.

Environment Variables
---------------------

You can configure DrGPT using environment variables:

API Keys
~~~~~~~~

.. code-block:: bash

   # AI Provider API Keys
   export OPENAI_API_KEY="sk-your-openai-key"
   export ANTHROPIC_API_KEY="sk-ant-your-anthropic-key"
   export GOOGLE_API_KEY="your-google-key"

Default Settings
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Default provider and model
   export DRGPT_DEFAULT_PROVIDER="openai"
   export DRGPT_DEFAULT_MODEL="gpt-4o-mini"
   
   # Output preferences
   export DRGPT_NO_STREAMING="false"
   export DRGPT_NO_MARKDOWN="false"

Command Line Options
--------------------

All configuration can be overridden via command-line options:

Provider Configuration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Set provider and model
   drgpt --provider openai --model gpt-4 "Your question"
   
   # List available providers
   drgpt --list-providers
   
   # Show current configuration
   drgpt --status

Output Configuration
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Disable streaming for immediate formatted output
   drgpt --no-streaming "Your question"
   
   # Disable markdown formatting
   drgpt --no-markdown "Your question"
   
   # Save output to file
   drgpt --output response.md "Your question"

Debug and Verbose Options
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Enable debug mode
   drgpt --debug "Your question"
   
   # Verbose output
   drgpt --verbose "Your question"

Configuration Management
-------------------------

Viewing Current Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Show current settings
   drgpt --status

This displays:

* Current provider and model
* API key status (without revealing the keys)
* Configuration file location
* Available providers and models

Setting Default Provider
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Set OpenAI as default
   drgpt --provider openai --set-default
   
   # Set Anthropic as default
   drgpt --provider anthropic --model claude-3-sonnet-20240229 --set-default

Adding New API Keys
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Add OpenAI key
   drgpt --provider openai --api-key "sk-your-new-key"
   
   # Add Anthropic key
   drgpt --provider anthropic --api-key "sk-ant-your-new-key"

Provider-Specific Configuration
-------------------------------

OpenAI Configuration
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Available models
   drgpt --provider openai --list-models
   
   # Default model: gpt-4o-mini (cost-effective)
   drgpt --provider openai --model gpt-4o-mini "Your question"
   
   # High-quality model
   drgpt --provider openai --model gpt-4 "Complex reasoning task"

Anthropic Configuration
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Available models
   drgpt --provider anthropic --list-models
   
   # Claude 3 Sonnet (balanced)
   drgpt --provider anthropic --model claude-3-sonnet-20240229 "Your question"
   
   # Claude 3 Opus (highest quality)
   drgpt --provider anthropic --model claude-3-opus-20240229 "Complex task"

Google AI Configuration
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Available models
   drgpt --provider google --list-models
   
   # Gemini Pro
   drgpt --provider google --model gemini-pro "Your question"

Custom API Configuration
~~~~~~~~~~~~~~~~~~~~~~~~

For custom or self-hosted APIs:

.. code-block:: bash

   # Custom OpenAI-compatible API
   export OPENAI_API_BASE="http://localhost:8000/v1"
   export OPENAI_API_KEY="your-custom-key"
   
   drgpt --provider openai "Your question"

Advanced Configuration
----------------------

Response Length Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Shorter responses
   drgpt --max-tokens 500 "Brief explanation of quantum computing"
   
   # Longer responses
   drgpt --max-tokens 2000 "Detailed analysis of market trends"

Temperature and Creativity
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # More focused responses (lower temperature)
   drgpt --temperature 0.1 "Factual information about Python"
   
   # More creative responses (higher temperature)
   drgpt --temperature 0.9 "Write a creative story"

Configuration File Format
--------------------------

The configuration file uses a simple key-value format:

.. code-block:: ini

   [default]
   provider = openai
   model = gpt-4o-mini
   temperature = 0.7
   max_tokens = 1500
   
   [providers]
   openai_api_key = sk-your-key
   anthropic_api_key = sk-ant-your-key
   google_api_key = your-key
   
   [output]
   streaming = true
   markdown = true
   
   [advanced]
   timeout = 30
   retries = 3

Configuration Backup and Restore
---------------------------------

Backup Configuration
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Backup configuration
   cp ~/.config/drgpt/config ~/drgpt-config-backup.txt

Restore Configuration
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Restore configuration
   cp ~/drgpt-config-backup.txt ~/.config/drgpt/config

Reset Configuration
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Reset to defaults (removes config file)
   rm ~/.config/drgpt/config
   
   # DrGPT will recreate it with defaults on next run
   drgpt --status

Security Considerations
-----------------------

API Key Security
~~~~~~~~~~~~~~~~

1. **Never commit API keys to version control**
2. **Use environment variables for automation**
3. **Regularly rotate your API keys**
4. **Use least-privilege API keys when possible**

Configuration File Permissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The configuration file should be readable only by your user:

.. code-block:: bash

   chmod 600 ~/.config/drgpt/config

Troubleshooting Configuration
-----------------------------

Common Issues
~~~~~~~~~~~~~

**Config file not found**:

.. code-block:: bash

   # Create config directory
   mkdir -p ~/.config/drgpt
   
   # Let DrGPT recreate the config
   drgpt --status

**API key not recognized**:

.. code-block:: bash

   # Verify environment variable
   echo $OPENAI_API_KEY
   
   # Check provider configuration
   drgpt --provider openai --status

**Provider not available**:

.. code-block:: bash

   # List all providers
   drgpt --list-providers
   
   # Check specific provider
   drgpt --provider openai --list-models
