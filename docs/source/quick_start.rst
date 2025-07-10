Quick Start
===========

This guide will get you up and running with DrGPT in just a few minutes.

Prerequisites
-------------

Before starting, make sure you have:

1. Python 3.8+ installed
2. DrGPT installed (``pip install drgpt``)
3. At least one AI provider API key configured

Your First Query
----------------

Once you have DrGPT installed and API keys configured, try your first query:

.. code-block:: bash

   drgpt "What is artificial intelligence?"

You should see a beautifully formatted response with markdown rendering.

Choosing a Provider
-------------------

DrGPT supports multiple AI providers. You can specify which one to use:

.. code-block:: bash

   # Use OpenAI GPT-4
   drgpt --provider openai --model gpt-4 "Explain quantum computing"
   
   # Use Anthropic Claude
   drgpt --provider anthropic --model claude-3-sonnet-20240229 "Write a poem"
   
   # Use Google Gemini
   drgpt --provider google --model gemini-pro "Solve this math problem"

List available providers and models:

.. code-block:: bash

   drgpt --list-providers

The Four Modes
--------------

DrGPT offers four specialized modes for different use cases:

1. **Standard Mode** (default)
   General AI assistant for questions, explanations, and discussions:

   .. code-block:: bash

      drgpt "Explain how photosynthesis works"

2. **Code Mode** (``--code`` or ``-c``)
   Pure code generation with no explanations:

   .. code-block:: bash

      drgpt --code "Create a Python function to calculate fibonacci numbers"
      drgpt -c "Create a Python function to calculate fibonacci numbers"  # Short form

3. **Shell Mode** (``--shell`` or ``-s``)
   System administration and command generation:

   .. code-block:: bash

      drgpt --shell "Find all files larger than 100MB"
      drgpt -s "Find all files larger than 100MB"  # Short form

4. **Interactive Mode** (``--interface`` or ``-i``)
   Conversational AI interface with special commands:

   .. code-block:: bash

      drgpt --interface
      drgpt -i  # Short form

Configuration
-------------

CLI Shortcuts
~~~~~~~~~~~~~~

DrGPT provides convenient shortcuts for frequently used options:

.. list-table:: Available Shortcuts
   :widths: 25 15 60
   :header-rows: 1

   * - Long Option
     - Short
     - Description
   * - ``--code``
     - ``-c``
     - Generate code only (no explanations)
   * - ``--shell``
     - ``-s``
     - Generate shell commands with execution options
   * - ``--editor``
     - ``-e``
     - Open text editor for input composition
   * - ``--interface``
     - ``-i``
     - Start interactive AI interface
   * - ``--chat``
     - ``-ch``
     - Start or continue a chat session
   * - ``--output``
     - ``-o``
     - Save response to file

**Examples with shortcuts:**

.. code-block:: bash

   # Code generation
   drgpt -c "Create a Python function"
   
   # Shell commands
   drgpt -s "List all processes"
   
   # Editor mode
   drgpt -e
   
   # Interactive mode
   drgpt -i
   
   # Save output
   drgpt -o result.md "Explain AI"
   
   # Combine shortcuts
   drgpt -c -o code.py "Create a web scraper"

Configuration
-------------

DrGPT automatically uses sensible defaults, but you can customize its behavior:

**Default Provider**: Set your preferred provider and model:

.. code-block:: bash

   # Always use these settings unless overridden
   export DRGPT_DEFAULT_PROVIDER="openai"
   export DRGPT_DEFAULT_MODEL="gpt-4"

**Debug Mode**: See detailed information about requests:

.. code-block:: bash

   drgpt --debug "Your question here"

Common Use Cases
----------------

Here are some common ways to use DrGPT:

**Learning and Research**:

.. code-block:: bash

   drgpt "Explain the difference between REST and GraphQL APIs"
   drgpt "What are the benefits of using Docker containers?"

**Code Generation**:

.. code-block:: bash

   drgpt --code "Create a REST API endpoint in Flask for user authentication"
   drgpt -c "Create a REST API endpoint in Flask for user authentication"  # Short form
   drgpt --code "Write a JavaScript function to debounce user input"
   drgpt -c "Write a JavaScript function to debounce user input"  # Short form

**System Administration**:

.. code-block:: bash

   drgpt --shell "Show disk usage by directory"
   drgpt -s "Show disk usage by directory"  # Short form
   drgpt --shell "Kill all processes using port 8080"
   drgpt -s "Kill all processes using port 8080"  # Short form
   drgpt --shell "Create a backup of my home directory"
   drgpt -s "Create a backup of my home directory"  # Short form

**Writing and Editing**:

.. code-block:: bash

   drgpt --editor  # Opens vi editor for longer prompts
   drgpt -e       # Short form
   drgpt "Improve this text: [your text here]"

**Interactive Sessions**:

.. code-block:: bash

   drgpt --interface
   drgpt -i  # Short form
   # Then use ! before questions in the interactive mode
   > !What is machine learning?
   > code: Create a neural network in PyTorch
   > shell: Show system information

Next Steps
----------

Now that you're familiar with the basics:

1. :doc:`modes/standard` - Learn about standard mode features
2. :doc:`modes/code` - Master code generation
3. :doc:`modes/shell` - Become a shell command expert  
4. :doc:`modes/interface` - Explore interactive features
5. :doc:`features/providers` - Configure different AI providers
6. :doc:`examples/use_cases` - See real-world examples

Getting Help
------------

If you need help:

.. code-block:: bash

   # Built-in help
   drgpt --help
   
   # Interactive mode help
   drgpt --interface
   > help

For more detailed information, continue reading the documentation sections.
