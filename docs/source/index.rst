.. raw:: html

   <div align="center">
     <img src="../logo.svg" alt="DrGPT Logo" width="200" height="200">
   </div>

DrGPT Documentation
===================

**DrGPT** is a powerful, cross-platform command-line interface for interacting with multiple AI providers including OpenAI, Anthropic, and Google's AI services. It offers four specialized modes for different use cases, from simple queries to complex code generation and system administration.

Key Features
------------

* **Multi-Provider Support**: OpenAI (GPT-4, GPT-3.5), Anthropic (Claude), Google AI (Gemini)
* **Four Specialized Modes**: Standard, Code, Shell, and Interactive
* **Rich Output**: Beautiful markdown rendering and syntax highlighting
* **Cross-Platform**: Full support for Windows, macOS, and Linux
* **Configuration Management**: Easy provider and model configuration
* **Interactive Interface**: Advanced AI chat with special commands

Quick Start
-----------

Install DrGPT:

.. code-block:: bash

   pip install drgpt

Set up your API keys:

.. code-block:: bash

   export OPENAI_API_KEY="your-key-here"
   export ANTHROPIC_API_KEY="your-key-here"
   export GOOGLE_API_KEY="your-key-here"

Basic usage:

.. code-block:: bash

   # Standard AI assistant
   drgpt "Explain quantum computing"
   
   # Code generation mode
   drgpt --code "Create a Python function to sort a list"
   
   # Shell command mode
   drgpt --shell "Find all Python files larger than 1MB"
   
   # Interactive mode
   drgpt --interface

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   installation
   quick_start
   configuration

.. toctree::
   :maxdepth: 2
   :caption: Usage Modes

   modes/standard
   modes/code
   modes/shell
   modes/interface

.. toctree::
   :maxdepth: 2
   :caption: Advanced Features

   features/providers
   features/models
   features/editor

.. toctree::
   :maxdepth: 2
   :caption: Reference

   api/cli_reference
   examples/use_cases
   troubleshooting

.. toctree::
   :maxdepth: 1
   :caption: Development

   contributing
   changelog

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

