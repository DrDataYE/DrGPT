Standard Mode
=============

Standard mode is the default DrGPT mode for general AI assistance, questions, explanations, and discussions. It provides rich, detailed responses with beautiful markdown formatting.

Overview
--------

Standard mode is designed for:

* General questions and explanations
* Learning and research
* Problem-solving discussions
* Text analysis and writing assistance
* Conversational AI interaction

When you run DrGPT without any special flags, you're using standard mode.

Basic Usage
-----------

.. code-block:: bash

   # Basic query
   drgpt "What is machine learning?"
   
   # Complex question
   drgpt "Explain the differences between React and Vue.js frameworks"
   
   # Problem-solving
   drgpt "How do I optimize database queries for large datasets?"

Features
--------

Rich Markdown Output
~~~~~~~~~~~~~~~~~~~~

Standard mode provides beautifully formatted responses with:

* **Headers and subheaders** for organization
* **Code blocks** with syntax highlighting
* **Lists and bullet points** for clarity
* **Tables** for structured data
* **Links and references** when relevant

Example output:

.. code-block:: bash

   drgpt "Explain Python data types"

.. code-block:: markdown

   # Python Data Types
   
   Python provides several built-in data types:
   
   ## Numeric Types
   
   * **int**: Integer numbers (e.g., 42, -17)
   * **float**: Decimal numbers (e.g., 3.14, -2.5)
   * **complex**: Complex numbers (e.g., 1+2j)
   
   ## Sequence Types
   
   * **str**: Text strings
   * **list**: Ordered, mutable collections
   * **tuple**: Ordered, immutable collections
   
   ## Example Code
   
   ```python
   # Creating different data types
   number = 42          # int
   price = 19.99        # float
   name = "Alice"       # str
   items = [1, 2, 3]    # list
   coordinates = (10, 20)  # tuple
   ```

Streaming Responses
~~~~~~~~~~~~~~~~~~~

By default, standard mode streams responses in real-time:

.. code-block:: bash

   drgpt "Write a detailed explanation of quantum computing"

You'll see the response appear progressively as it's generated, followed by a formatted preview.

**Disable streaming** for immediate formatted output:

.. code-block:: bash

   drgpt --no-streaming "Your question"

Provider Selection
~~~~~~~~~~~~~~~~~~

Choose specific AI providers for different strengths:

.. code-block:: bash

   # OpenAI GPT-4 for general intelligence
   drgpt --provider openai --model gpt-4 "Complex reasoning task"
   
   # Anthropic Claude for thoughtful analysis
   drgpt --provider anthropic "Analyze this philosophical argument"
   
   # Google Gemini for factual information
   drgpt --provider google "Latest information about space exploration"

Advanced Options
----------------

Custom Parameters
~~~~~~~~~~~~~~~~~

Fine-tune response characteristics:

.. code-block:: bash

   # Shorter, more focused responses
   drgpt --max-tokens 500 "Brief summary of blockchain technology"
   
   # More creative responses
   drgpt --temperature 0.9 "Write a creative story about time travel"
   
   # More factual, consistent responses
   drgpt --temperature 0.1 "Explain the scientific method"

Output Control
~~~~~~~~~~~~~~

Control how responses are displayed:

.. code-block:: bash

   # Save response to file
   drgpt --output analysis.md "Analyze current AI trends"
   
   # Plain text output (no formatting)
   drgpt --no-markdown "Simple explanation without formatting"
   
   # Debug mode (show request details)
   drgpt --debug "Your question"

Use Cases
---------

Learning and Education
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Concept explanations
   drgpt "Explain the concept of inheritance in object-oriented programming"
   
   # Historical information
   drgpt "What were the main causes of World War I?"
   
   # Scientific concepts
   drgpt "How does photosynthesis work at the molecular level?"

Research and Analysis
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Technology comparisons
   drgpt "Compare NoSQL vs SQL databases for web applications"
   
   # Market analysis
   drgpt "What are the current trends in renewable energy technology?"
   
   # Literature analysis
   drgpt "Analyze the themes in George Orwell's 1984"

Problem Solving
~~~~~~~~~~~~~~~

.. code-block:: bash

   # Technical problems
   drgpt "My React app is rendering slowly. What could be the causes?"
   
   # Business problems
   drgpt "How can a small business improve customer retention?"
   
   # Personal problems
   drgpt "What are effective time management strategies for students?"

Writing Assistance
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Content improvement
   drgpt "Improve this email: [your email text]"
   
   # Writing guidance
   drgpt "How do I write an effective research proposal?"
   
   # Creative writing
   drgpt "Help me develop a character for my novel"

Best Practices
--------------

Effective Prompting
~~~~~~~~~~~~~~~~~~~

For best results in standard mode:

1. **Be specific**: "Explain async/await in JavaScript" vs "Explain JavaScript"
2. **Provide context**: "As a beginner programmer, explain..."
3. **Ask follow-up questions**: Build on previous responses
4. **Use examples**: "Show me an example of..."

.. code-block:: bash

   # Good prompt
   drgpt "As a web developer, explain how to implement JWT authentication in a Node.js API with practical examples"
   
   # Less effective prompt
   drgpt "Explain JWT"

Managing Long Responses
~~~~~~~~~~~~~~~~~~~~~~~

For complex topics requiring detailed responses:

.. code-block:: bash

   # Request structured output
   drgpt "Explain machine learning algorithms with the following structure: 1) Definition 2) Types 3) Use cases 4) Examples"
   
   # Break into parts
   drgpt "Explain supervised learning algorithms in machine learning"
   drgpt "Now explain unsupervised learning algorithms"

Combining with Other Modes
~~~~~~~~~~~~~~~~~~~~~~~~~~

Use standard mode in combination with other DrGPT modes:

.. code-block:: bash

   # Standard mode for explanation
   drgpt "Explain how to sort a list in Python"
   
   # Then code mode for implementation
   drgpt --code "Create a Python function that sorts a list using quicksort"
   
   # Then shell mode for testing
   drgpt --shell "Run Python unit tests"

Output Examples
---------------

Here are examples of typical standard mode output:

**Question**: "What is Docker?"

**Response Structure**:

.. code-block:: markdown

   # Docker: Containerization Platform
   
   Docker is a containerization platform that allows developers to package applications
   and their dependencies into lightweight, portable containers.
   
   ## Key Concepts
   
   * **Containers**: Lightweight, standalone packages containing everything needed to run an application
   * **Images**: Read-only templates used to create containers
   * **Dockerfile**: Text file with instructions to build Docker images
   
   ## Benefits
   
   * **Consistency**: "Works on my machine" problem solved
   * **Portability**: Run anywhere Docker is installed
   * **Efficiency**: Share OS kernel, use fewer resources than VMs
   
   ## Common Commands
   
   ```bash
   # Build an image
   docker build -t myapp .
   
   # Run a container
   docker run -p 3000:3000 myapp
   
   # List running containers
   docker ps
   ```

Integration Tips
----------------

Environment Integration
~~~~~~~~~~~~~~~~~~~~~~~

Standard mode works well with various environments:

.. code-block:: bash

   # In scripts
   RESPONSE=$(drgpt --no-markdown "Brief explanation of $TOPIC")
   echo "$RESPONSE"
   
   # With pipes
   echo "Explain this code:" | cat - myfile.py | drgpt
   
   # From files
   drgpt "Analyze this log file: $(cat error.log)"

IDE Integration
~~~~~~~~~~~~~~~

Many editors can integrate with DrGPT:

.. code-block:: bash

   # VS Code terminal
   drgpt "Explain this error: $ERROR_MESSAGE"
   
   # Vim command mode
   :!drgpt "Explain CSS flexbox"

Next Steps
----------

* :doc:`code` - Learn about pure code generation
* :doc:`shell` - Master system administration commands
* :doc:`interface` - Explore interactive conversations
* :doc:`../features/providers` - Configure different AI providers
