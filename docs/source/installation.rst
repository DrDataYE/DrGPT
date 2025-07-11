Installation
============

DrGPT can be installed using pip, or from source for development purposes.

Requirements
------------

* Python 3.8 or higher
* pip package manager
* API keys for desired AI providers

Installing with pip
--------------------

The easiest way to install DrGPT is using pip:

.. code-block:: bash

   pip install drgpt

This will install DrGPT and all its dependencies.

Installing from Source
-----------------------

For development or the latest features:

.. code-block:: bash

   git clone https://github.com/DrDataYE/drgpt.git
   cd drgpt
   pip install -e .

For development with testing dependencies:

.. code-block:: bash

   pip install -e ".[dev]"

Verifying Installation
----------------------

Verify that DrGPT is installed correctly:

.. code-block:: bash

   drgpt --version
   drgpt --help

You should see the version information and help text.

Setting up API Keys
--------------------

Before using DrGPT, you need to set up API keys for the providers you want to use:

OpenAI
~~~~~~

1. Get your API key from https://platform.openai.com/api-keys
2. Set the environment variable:

.. code-block:: bash

   # Linux/macOS
   export OPENAI_API_KEY="sk-your-key-here"
   
   # Windows (PowerShell)
   $env:OPENAI_API_KEY="sk-your-key-here"
   
   # Windows (Command Prompt)
   set OPENAI_API_KEY=sk-your-key-here

Anthropic Claude
~~~~~~~~~~~~~~~~~

1. Get your API key from https://console.anthropic.com/
2. Set the environment variable:

.. code-block:: bash

   # Linux/macOS
   export ANTHROPIC_API_KEY="sk-ant-your-key-here"
   
   # Windows (PowerShell)
   $env:ANTHROPIC_API_KEY="sk-ant-your-key-here"

Google AI (Gemini)
~~~~~~~~~~~~~~~~~~

1. Get your API key from https://aistudio.google.com/app/apikey
2. Set the environment variable:

.. code-block:: bash

   # Linux/macOS
   export GOOGLE_API_KEY="your-key-here"
   
   # Windows (PowerShell)
   $env:GOOGLE_API_KEY="your-key-here"

Persistent Configuration
~~~~~~~~~~~~~~~~~~~~~~~~

To make your API keys persistent, add them to your shell profile:

.. code-block:: bash

   # Linux/macOS (.bashrc, .zshrc, etc.)
   echo 'export OPENAI_API_KEY="sk-your-key-here"' >> ~/.bashrc
   echo 'export ANTHROPIC_API_KEY="sk-ant-your-key-here"' >> ~/.bashrc
   echo 'export GOOGLE_API_KEY="your-key-here"' >> ~/.bashrc

For Windows, use the System Properties > Environment Variables dialog.

Troubleshooting
---------------

Permission Errors
~~~~~~~~~~~~~~~~~~

If you get permission errors during installation:

.. code-block:: bash

   # Use --user flag
   pip install --user drgpt
   
   # Or use virtual environment
   python -m venv drgpt-env
   source drgpt-env/bin/activate  # Linux/macOS
   drgpt-env\Scripts\activate     # Windows
   pip install drgpt

Missing Dependencies
~~~~~~~~~~~~~~~~~~~~

If you encounter dependency issues:

.. code-block:: bash

   # Update pip first
   pip install --upgrade pip
   
   # Then install DrGPT
   pip install drgpt

API Key Issues
~~~~~~~~~~~~~~

If DrGPT can't find your API keys:

1. Verify the environment variable is set:

.. code-block:: bash

   # Linux/macOS/Windows (PowerShell)
   echo $env:OPENAI_API_KEY
   
   # Windows (Command Prompt)
   echo %OPENAI_API_KEY%

2. Restart your terminal after setting environment variables
3. Use the ``--list-providers`` option to check available providers

