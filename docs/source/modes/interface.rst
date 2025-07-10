Interactive Mode
================

Interactive mode (``--interface`` or ``-i``) provides a conversational AI experience with persistent context, special commands, and enhanced features for extended sessions.

Overview
--------

Interactive mode offers:

* **Persistent conversation** context across multiple queries
* **Special command system** with built-in utilities
* **Mixed mode operations** (standard, code, and shell in one session)
* **Session management** and history
* **Rich interactive interface** with panels and formatting

Start interactive mode with:

.. code-block:: bash

   drgpt --interface
   drgpt -i  # Short form

Basic Usage
-----------

Starting a Session
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   $ drgpt --interface
   
   ╭─ DrGPT Interactive Mode ─╮
   │ Type ! before questions  │
   │ Use 'help' for commands  │
   │ Use 'exit' to quit       │
   ╰─────────────────────────╯

Interactive Prompt
~~~~~~~~~~~~~~~~~~

All AI queries must start with ``!``:

.. code-block:: bash

   > ! What is machine learning?
   > ! Explain Python decorators
   > ! How do I optimize database queries?

This design prevents accidental AI calls and clearly separates commands from AI queries.

Special Commands
----------------

Built-in Commands
~~~~~~~~~~~~~~~~~

Interactive mode includes several built-in commands:

**help**
  Show available commands and usage information

.. code-block:: bash

   > help
   
   DrGPT Interactive Commands:
   • help     - Show this help message
   • status   - Show current configuration
   • providers - List available AI providers
   • clear    - Clear the screen
   • exit     - Exit interactive mode

**status**
  Display current configuration and session information

.. code-block:: bash

   > status
   
   ╭─ DrGPT Status ─╮
   │ Provider: openai     │
   │ Model: gpt-4o-mini   │
   │ Session: Active      │
   │ Messages: 5          │
   ╰─────────────────────╯

**providers**
  List all available AI providers and models

.. code-block:: bash

   > providers
   
   Available Providers:
   • OpenAI
     - gpt-4
     - gpt-4o-mini
     - gpt-3.5-turbo
   • Anthropic
     - claude-3-opus-20240229
     - claude-3-sonnet-20240229

**clear**
  Clear the screen for better readability

.. code-block:: bash

   > clear
   [Screen cleared]

**exit/quit**
  End the interactive session

.. code-block:: bash

   > exit
   Goodbye! Session ended.

Mixed Mode Operations
---------------------

One of the most powerful features of interactive mode is the ability to use all DrGPT modes within a single session.

Code Mode in Interactive
~~~~~~~~~~~~~~~~~~~~~~~~

Use ``code:`` prefix for pure code generation:

.. code-block:: bash

   > code: Create a Python function to calculate fibonacci numbers
   
   ```python
   def fibonacci(n):
       if n <= 1:
           return n
       return fibonacci(n-1) + fibonacci(n-2)
   ```

Shell Mode in Interactive
~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``shell:`` prefix for system commands with execution options:

.. code-block:: bash

   > shell: Find all Python files larger than 1MB
   
   Generated Command:
   find . -name "*.py" -size +1M -exec ls -lh {} \;
   
   [E]xecute, [D]escribe, [A]bort (e/d/a):

Standard Mode (Default)
~~~~~~~~~~~~~~~~~~~~~~~

Regular ``!`` prefix for standard AI assistance:

.. code-block:: bash

   > ! Explain the difference between lists and tuples in Python
   
   # Lists vs Tuples in Python
   
   Lists and tuples are both sequence types in Python, but they have key differences:
   
   ## Lists
   * Mutable (can be changed after creation)
   * Use square brackets: [1, 2, 3]
   * Dynamic size
   
   ## Tuples  
   * Immutable (cannot be changed after creation)
   * Use parentheses: (1, 2, 3)
   * Fixed size

Session Management
------------------

Context Preservation
~~~~~~~~~~~~~~~~~~~

Interactive mode maintains conversation context throughout the session:

.. code-block:: bash

   > ! What is machine learning?
   [AI explains machine learning]
   
   > ! Can you give me an example?
   [AI provides example, understanding "example" refers to machine learning]
   
   > ! What about deep learning?
   [AI explains deep learning in context of previous ML discussion]

Session Information
~~~~~~~~~~~~~~~~~~~

Track your session progress:

.. code-block:: bash

   > status
   
   ╭─ Session Status ─╮
   │ Duration: 15m 32s    │
   │ Messages: 12         │
   │ Provider: openai     │
   │ Context: Maintained  │
   ╰─────────────────────╯

Advanced Features
-----------------

Provider Switching
~~~~~~~~~~~~~~~~~~

Switch AI providers during a session:

.. code-block:: bash

   > ! What is quantum computing?
   [Response from current provider]
   
   > providers
   [Shows available providers]
   
   # (Note: Provider switching requires restarting interactive mode currently)

Multi-Step Workflows
~~~~~~~~~~~~~~~~~~~

Combine different modes for complex workflows:

.. code-block:: bash

   # Step 1: Research
   > ! How do I implement user authentication in Flask?
   
   # Step 2: Generate code
   > code: Create a Flask route for user login with JWT
   
   # Step 3: Test setup
   > shell: Install required packages for Flask JWT
   
   # Step 4: Follow-up questions
   > ! How do I handle token expiration?

Use Cases
---------

Learning Sessions
~~~~~~~~~~~~~~~~~

Perfect for educational conversations:

.. code-block:: bash

   > ! What is Docker?
   [Explanation of Docker]
   
   > ! Show me a simple Dockerfile example
   [Basic Dockerfile explanation]
   
   > code: Create a Dockerfile for a Python Flask app
   [Actual Dockerfile code]
   
   > shell: Build and run this Docker container
   [Docker commands with execution options]

Development Workflows
~~~~~~~~~~~~~~~~~~~~~

Ideal for development tasks:

.. code-block:: bash

   > ! I need to create a REST API. What should I consider?
   [API design discussion]
   
   > code: Create a FastAPI endpoint for user registration
   [FastAPI code]
   
   > code: Create Pydantic models for user data
   [Pydantic models]
   
   > shell: Install FastAPI and start development server
   [Installation and run commands]

Problem Solving
~~~~~~~~~~~~~~~

Extended troubleshooting sessions:

.. code-block:: bash

   > ! My web application is running slowly. How do I debug this?
   [Performance debugging advice]
   
   > shell: Show processes using high CPU
   [System monitoring commands]
   
   > ! What are common database performance issues?
   [Database optimization discussion]
   
   > code: Create a function to log database query performance
   [Monitoring code]

Research and Analysis
~~~~~~~~~~~~~~~~~~~~~

Deep-dive research sessions:

.. code-block:: bash

   > ! Compare microservices vs monolithic architecture
   [Architecture comparison]
   
   > ! What are the specific challenges with microservices?
   [Challenges discussion]
   
   > ! Show me how to implement service discovery
   [Service discovery explanation]
   
   > code: Create a simple service registry in Python
   [Service registry implementation]

Best Practices
--------------

Session Organization
~~~~~~~~~~~~~~~~~~~

1. **Start with broad questions**, then get specific
2. **Use status command** to track session progress  
3. **Clear screen periodically** for better readability
4. **Plan your workflow** before starting complex tasks

Effective Conversation Flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Good flow: Topic progression
   > ! What is containerization?
   > ! How does Docker work?
   > code: Show me a simple Docker example
   > shell: Install Docker on my system
   
   # Less effective: Random topic jumping
   > ! What is Python?
   > shell: Install nginx
   > ! Explain quantum physics

Context Management
~~~~~~~~~~~~~~~~~~

1. **Build on previous responses** for better context
2. **Reference earlier parts** of the conversation
3. **Use follow-up questions** rather than repeating context
4. **Start new sessions** for completely different topics

Command Usage Tips
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Use specific prefixes for clarity
   > code: [for pure code generation]
   > shell: [for system commands]
   > ! [for general AI assistance]
   
   # Combine modes in logical order
   > ! [understand the concept]
   > code: [implement the solution]
   > shell: [deploy or test]

Integration with Development
----------------------------

IDE Integration
~~~~~~~~~~~~~~~

Interactive mode works well alongside development environments:

.. code-block:: bash

   # Terminal split in VS Code
   # Left: Code editor
   # Right: DrGPT interactive mode
   
   > ! How do I implement OAuth in my app?
   > code: Create OAuth middleware for Express
   [Copy code to editor]
   
   > shell: Install required OAuth packages
   [Execute in terminal]

Documentation Workflow
~~~~~~~~~~~~~~~~~~~~~~

Use interactive mode for documentation:

.. code-block:: bash

   > ! Explain this code pattern for my documentation
   > ! What are the best practices for API documentation?
   > code: Create example API calls for documentation

Project Planning
~~~~~~~~~~~~~~~~

Plan development projects interactively:

.. code-block:: bash

   > ! I want to build a task management app. What components do I need?
   > ! What database schema would work best?
   > code: Create database models for tasks and users
   > ! What about the frontend architecture?

Customization
-------------

Session Startup
~~~~~~~~~~~~~~~

Customize interactive mode startup:

.. code-block:: bash

   # Set default provider for session
   drgpt --interface --provider anthropic
   
   # Start with specific model
   drgpt --interface --provider openai --model gpt-4

Output Preferences
~~~~~~~~~~~~~~~~~~

Configure output formatting:

.. code-block:: bash

   # Disable streaming in interactive mode
   drgpt --interface --no-streaming
   
   # Plain text mode (less formatting)
   drgpt --interface --no-markdown

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Forgetting the ! prefix**:

.. code-block:: bash

   > What is Python?
   Unknown command. Use '!' before AI queries.
   
   > ! What is Python?
   [Correct usage]

**Context getting too long**:

Interactive sessions maintain context, which can become unwieldy. Start a new session for different topics.

**Commands not working**:

.. code-block:: bash

   > help
   [Shows all available commands]
   
   > status
   [Check session status]

Session Recovery
~~~~~~~~~~~~~~~~

If interactive mode becomes unresponsive:

1. **Ctrl+C** to interrupt current operation
2. **exit** to end session gracefully
3. **Restart** with ``drgpt --interface``

Performance Tips
~~~~~~~~~~~~~~~~

For better performance in long sessions:

1. **Clear screen regularly** with ``clear``
2. **Start new sessions** for different topics
3. **Use specific queries** rather than very broad questions

Next Steps
----------

* :doc:`../features/editor` - Learn about vi editor integration
* :doc:`../examples/use_cases` - See real-world interactive workflows  
* :doc:`../configuration` - Customize your interactive experience
* :doc:`../api/cli_reference` - Complete command reference
