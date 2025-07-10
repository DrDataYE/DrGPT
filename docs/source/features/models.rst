Models and Selection Guide
============================

Comprehensive guide to choosing the right AI model for your specific needs and use cases.

Model Overview
--------------

Different AI providers offer various models with different capabilities, speeds, and costs. This guide helps you select the optimal model for your specific requirements.

OpenAI Models
-------------

gpt-4o-mini (Recommended Default)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Best For**: General use, cost-effective AI assistance

* **Speed**: Fast (⚡⚡⚡⚡)
* **Quality**: Good (⭐⭐⭐)
* **Cost**: Very Low (💰)
* **Context**: 128k tokens

**Use Cases**:

.. code-block:: bash

   # Daily development tasks
   drgpt --provider openai --model gpt-4o-mini "Explain this error message"
   
   # Quick code generation
   drgpt --provider openai --model gpt-4o-mini --code "Create a simple Python function"
   
   # Basic system administration
   drgpt --provider openai --model gpt-4o-mini --shell "Show disk usage"

gpt-4
~~~~~

**Best For**: Complex reasoning, important decisions, detailed analysis

* **Speed**: Moderate (⚡⚡)
* **Quality**: Excellent (⭐⭐⭐⭐⭐)
* **Cost**: High (💰💰💰💰)
* **Context**: 128k tokens

**Use Cases**:

.. code-block:: bash

   # Complex architecture decisions
   drgpt --provider openai --model gpt-4 "Design microservices architecture for high-traffic e-commerce"
   
   # Advanced code generation
   drgpt --provider openai --model gpt-4 --code "Create comprehensive error handling system"
   
   # Critical system commands
   drgpt --provider openai --model gpt-4 --shell "Design disaster recovery procedure"

gpt-3.5-turbo
~~~~~~~~~~~~~

**Best For**: Balanced performance and cost

* **Speed**: Fast (⚡⚡⚡)
* **Quality**: Good (⭐⭐⭐)
* **Cost**: Low (💰💰)
* **Context**: 16k tokens

**Use Cases**:

.. code-block:: bash

   # General programming help
   drgpt --provider openai --model gpt-3.5-turbo "How do I implement authentication?"
   
   # Standard code tasks
   drgpt --provider openai --model gpt-3.5-turbo --code "Create API endpoint"

Anthropic Models
----------------

claude-3-opus-20240229
~~~~~~~~~~~~~~~~~~~~~~

**Best For**: Highest quality analysis, complex reasoning, nuanced understanding

* **Speed**: Slow (⚡)
* **Quality**: Exceptional (⭐⭐⭐⭐⭐)
* **Cost**: Very High (💰💰💰💰💰)
* **Context**: 200k tokens

**Use Cases**:

.. code-block:: bash

   # Deep analysis and research
   drgpt --provider anthropic --model claude-3-opus-20240229 "Analyze the long-term implications of this architectural decision"
   
   # High-quality writing
   drgpt --provider anthropic --model claude-3-opus-20240229 "Write comprehensive technical documentation"

claude-3-sonnet-20240229 (Anthropic Default)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Best For**: Balanced quality and speed, thoughtful responses

* **Speed**: Moderate (⚡⚡⚡)
* **Quality**: Very Good (⭐⭐⭐⭐)
* **Cost**: Moderate (💰💰💰)
* **Context**: 200k tokens

**Use Cases**:

.. code-block:: bash

   # Code review and analysis
   drgpt --provider anthropic --model claude-3-sonnet-20240229 "Review this code for potential issues"
   
   # Technical writing
   drgpt --provider anthropic --model claude-3-sonnet-20240229 "Explain this concept clearly"

claude-3-haiku-20240307
~~~~~~~~~~~~~~~~~~~~~~~

**Best For**: Fast responses, simple tasks, cost-effective

* **Speed**: Very Fast (⚡⚡⚡⚡⚡)
* **Quality**: Good (⭐⭐⭐)
* **Cost**: Low (💰💰)
* **Context**: 200k tokens

**Use Cases**:

.. code-block:: bash

   # Quick questions
   drgpt --provider anthropic --model claude-3-haiku-20240307 "What is the syntax for this command?"
   
   # Fast code generation
   drgpt --provider anthropic --model claude-3-haiku-20240307 --code "Simple utility function"

Google AI Models
----------------

gemini-pro
~~~~~~~~~~

**Best For**: Latest information, factual accuracy, technical queries

* **Speed**: Fast (⚡⚡⚡⚡)
* **Quality**: Very Good (⭐⭐⭐⭐)
* **Cost**: Moderate (💰💰💰)
* **Context**: 32k tokens

**Use Cases**:

.. code-block:: bash

   # Research and factual queries
   drgpt --provider google --model gemini-pro "Latest developments in cloud computing"
   
   # Technical documentation
   drgpt --provider google --model gemini-pro "Explain current best practices for API security"

Model Selection by Use Case
---------------------------

Code Generation
~~~~~~~~~~~~~~~

**Best Models**:

1. **OpenAI GPT-4** - Highest quality code, complex algorithms
2. **OpenAI GPT-4o-mini** - Fast, cost-effective for simple code
3. **Anthropic Claude-3-Sonnet** - Clean, well-structured code

.. code-block:: bash

   # Complex algorithms
   drgpt --provider openai --model gpt-4 --code "Implement A* pathfinding algorithm"
   
   # Simple utilities
   drgpt --provider openai --model gpt-4o-mini --code "Create file validation function"
   
   # Clean architecture
   drgpt --provider anthropic --model claude-3-sonnet-20240229 --code "Design class hierarchy"

Shell Commands and System Administration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Best Models**:

1. **OpenAI GPT-4o-mini** - Fast, accurate system commands
2. **Google Gemini Pro** - Good for platform-specific commands
3. **OpenAI GPT-4** - Complex system architecture

.. code-block:: bash

   # Standard system tasks
   drgpt --provider openai --model gpt-4o-mini --shell "Monitor system performance"
   
   # Platform-specific commands
   drgpt --provider google --model gemini-pro --shell "Windows PowerShell commands for IIS"
   
   # Complex infrastructure
   drgpt --provider openai --model gpt-4 --shell "Design backup strategy for distributed system"

Research and Analysis
~~~~~~~~~~~~~~~~~~~~~

**Best Models**:

1. **Anthropic Claude-3-Opus** - Deep, nuanced analysis
2. **Google Gemini Pro** - Latest information and facts
3. **OpenAI GPT-4** - Comprehensive reasoning

.. code-block:: bash

   # Deep analysis
   drgpt --provider anthropic --model claude-3-opus-20240229 "Analyze the trade-offs between different database architectures"
   
   # Current information
   drgpt --provider google --model gemini-pro "Latest trends in machine learning"
   
   # Complex reasoning
   drgpt --provider openai --model gpt-4 "Evaluate the long-term implications of this technical decision"

Writing and Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~

**Best Models**:

1. **Anthropic Claude-3-Opus** - Highest quality writing
2. **Anthropic Claude-3-Sonnet** - Balanced quality and speed
3. **OpenAI GPT-4** - Comprehensive documentation

.. code-block:: bash

   # High-quality writing
   drgpt --provider anthropic --model claude-3-opus-20240229 "Write comprehensive API documentation"
   
   # Balanced writing tasks
   drgpt --provider anthropic --model claude-3-sonnet-20240229 "Explain technical concepts clearly"

Interactive Sessions
~~~~~~~~~~~~~~~~~~~~

**Best Models**:

1. **OpenAI GPT-4o-mini** - Fast responses, good context retention
2. **Anthropic Claude-3-Sonnet** - Thoughtful interactive responses
3. **Google Gemini Pro** - Good for factual interactive queries

.. code-block:: bash

   # Fast interactive sessions
   drgpt --provider openai --model gpt-4o-mini --interface
   
   # Thoughtful conversations
   drgpt --provider anthropic --model claude-3-sonnet-20240229 --interface

Cost Optimization Strategies
----------------------------

Daily Development Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~

Use cost-effective models for routine tasks:

.. code-block:: bash

   # Set cost-effective defaults
   export DRGPT_DEFAULT_PROVIDER="openai"
   export DRGPT_DEFAULT_MODEL="gpt-4o-mini"
   
   # Use for most tasks
   drgpt "Regular development questions"
   drgpt --code "Simple code generation"
   drgpt --shell "Standard system commands"

Premium Tasks
~~~~~~~~~~~~~

Reserve expensive models for critical work:

.. code-block:: bash

   # Important architectural decisions
   drgpt --provider openai --model gpt-4 "Design system architecture"
   
   # Critical analysis
   drgpt --provider anthropic --model claude-3-opus-20240229 "Analyze security implications"

Hybrid Approach
~~~~~~~~~~~~~~~

Combine models strategically:

.. code-block:: bash

   # Start with fast model for initial exploration
   drgpt --provider openai --model gpt-4o-mini "What are the options for implementing authentication?"
   
   # Use premium model for detailed implementation
   drgpt --provider openai --model gpt-4 --code "Implement secure JWT authentication system"

Performance Considerations
--------------------------

Response Speed
~~~~~~~~~~~~~~

**Fastest Models**:
1. Anthropic Claude-3-Haiku
2. OpenAI GPT-4o-mini
3. Google Gemini Pro

**Use for**: Quick queries, interactive sessions, real-time assistance

Quality vs Speed Trade-offs
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # When speed matters most
   drgpt --provider anthropic --model claude-3-haiku-20240307 "Quick answer needed"
   
   # When quality matters most
   drgpt --provider anthropic --model claude-3-opus-20240229 "Detailed analysis required"
   
   # Balanced approach
   drgpt --provider anthropic --model claude-3-sonnet-20240229 "Good quality, reasonable speed"

Context Length Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Large Context Models** (for long inputs):
- Anthropic Claude-3 series (200k tokens)
- OpenAI GPT-4 (128k tokens)

**Standard Context** (for normal use):
- Google Gemini Pro (32k tokens)
- OpenAI GPT-3.5-turbo (16k tokens)

.. code-block:: bash

   # For large codebases or documents
   drgpt --provider anthropic --model claude-3-sonnet-20240229 "Analyze this entire codebase"
   
   # For normal queries
   drgpt --provider openai --model gpt-4o-mini "Standard question"

Model Selection Decision Tree
-----------------------------

Follow this decision tree to choose the right model:

.. code-block:: text

   1. What's your primary need?
      ├── Speed → GPT-4o-mini or Claude-3-Haiku
      ├── Cost → GPT-4o-mini or Claude-3-Haiku
      ├── Quality → GPT-4 or Claude-3-Opus
      └── Balance → Claude-3-Sonnet or Gemini Pro
   
   2. What type of task?
      ├── Code Generation → OpenAI models
      ├── Analysis/Writing → Anthropic models
      ├── Research/Facts → Google Gemini
      └── System Admin → OpenAI or Google
   
   3. How complex is the task?
      ├── Simple → Use default models
      ├── Moderate → Use balanced models
      └── Complex → Use premium models

Switching Models Mid-Session
----------------------------

Currently, model switching requires restarting DrGPT:

.. code-block:: bash

   # Start with fast model
   drgpt --provider openai --model gpt-4o-mini --interface
   > ! Initial exploration question
   > exit
   
   # Switch to premium model for detailed work
   drgpt --provider openai --model gpt-4 --interface
   > ! Detailed implementation question

Future versions will support dynamic model switching within sessions.

Best Practices
--------------

Model Selection Guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Start cheap**: Use cost-effective models first
2. **Upgrade when needed**: Switch to premium for complex tasks
3. **Match strengths**: Use provider/model strengths for specific tasks
4. **Monitor costs**: Track usage across different models

Prompt Optimization by Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Different models respond better to different prompt styles:

**OpenAI Models**: Direct, specific prompts
.. code-block:: bash

   drgpt --provider openai "Create a Python function that validates email addresses"

**Anthropic Models**: Conversational, detailed prompts
.. code-block:: bash

   drgpt --provider anthropic "I need help creating a function to validate email addresses. Please consider edge cases and provide clean, maintainable code."

**Google Models**: Factual, research-oriented prompts
.. code-block:: bash

   drgpt --provider google "What are the current best practices for email validation in 2024?"

Next Steps
----------

* :doc:`providers` - Learn about AI provider capabilities
* :doc:`../examples/use_cases` - See model selection in real scenarios
* :doc:`../api/cli_reference` - Complete model specification reference
* :doc:`../configuration` - Set up default models and providers
