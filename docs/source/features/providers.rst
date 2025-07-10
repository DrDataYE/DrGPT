AI Providers
============

DrGPT supports multiple AI providers, each with different strengths, capabilities, and pricing models. This guide helps you choose and configure the right provider for your needs.

Supported Providers
-------------------

OpenAI
~~~~~~

**Models Available**:

* ``gpt-4`` - Most capable model, best for complex reasoning
* ``gpt-4o-mini`` - Fast and cost-effective (default)
* ``gpt-3.5-turbo`` - Good balance of speed and capability

**Strengths**:

* Excellent general knowledge and reasoning
* Strong code generation capabilities
* Fast response times
* Consistent API reliability

**Best For**: General AI assistance, code generation, complex problem solving

Anthropic (Claude)
~~~~~~~~~~~~~~~~~~

**Models Available**:

* ``claude-3-opus-20240229`` - Highest capability model
* ``claude-3-sonnet-20240229`` - Balanced performance and speed
* ``claude-3-haiku-20240307`` - Fast and efficient

**Strengths**:

* Thoughtful and nuanced responses
* Strong analytical capabilities
* Excellent for writing and editing
* Good safety considerations

**Best For**: Analysis, writing assistance, ethical reasoning, detailed explanations

Google AI (Gemini)
~~~~~~~~~~~~~~~~~~

**Models Available**:

* ``gemini-pro`` - Advanced reasoning and multimodal capabilities
* ``gemini-pro-vision`` - Image understanding (future support)

**Strengths**:

* Latest information access
* Strong factual accuracy
* Good performance on technical topics
* Competitive pricing

**Best For**: Research, factual queries, technical documentation

Provider Configuration
----------------------

Setting API Keys
~~~~~~~~~~~~~~~~

Each provider requires an API key:

**OpenAI**:

.. code-block:: bash

   # Get key from: https://platform.openai.com/api-keys
   export OPENAI_API_KEY="sk-your-openai-key-here"

**Anthropic**:

.. code-block:: bash

   # Get key from: https://console.anthropic.com/
   export ANTHROPIC_API_KEY="sk-ant-your-anthropic-key-here"

**Google AI**:

.. code-block:: bash

   # Get key from: https://aistudio.google.com/app/apikey
   export GOOGLE_API_KEY="your-google-api-key-here"

Default Provider Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set your preferred default provider:

.. code-block:: bash

   # Set default provider and model
   export DRGPT_DEFAULT_PROVIDER="openai"
   export DRGPT_DEFAULT_MODEL="gpt-4o-mini"

Using Providers
---------------

Specifying Provider Per Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Use OpenAI
   drgpt --provider openai "Explain quantum computing"
   
   # Use Anthropic
   drgpt --provider anthropic "Analyze this philosophical argument"
   
   # Use Google AI
   drgpt --provider google "What are the latest developments in AI?"

Specifying Models
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # OpenAI with specific model
   drgpt --provider openai --model gpt-4 "Complex reasoning task"
   
   # Anthropic with specific model
   drgpt --provider anthropic --model claude-3-opus-20240229 "Detailed analysis"

Listing Available Options
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # List all providers and models
   drgpt --list-providers
   
   # Check current configuration
   drgpt --status

Provider Characteristics
------------------------

Response Quality
~~~~~~~~~~~~~~~~

**OpenAI GPT-4**:
- Excellent for complex reasoning
- Strong mathematical capabilities
- Good code generation
- Balanced and comprehensive responses

**Anthropic Claude**:
- Thoughtful and nuanced analysis
- Strong ethical reasoning
- Excellent writing quality
- Detailed explanations

**Google Gemini**:
- Fast and accurate responses
- Good technical knowledge
- Strong factual accuracy
- Latest information access

Speed and Performance
~~~~~~~~~~~~~~~~~~~~~

**Fastest**: ``gpt-4o-mini``, ``claude-3-haiku-20240307``

**Balanced**: ``gpt-3.5-turbo``, ``claude-3-sonnet-20240229``, ``gemini-pro``

**Highest Quality**: ``gpt-4``, ``claude-3-opus-20240229``

Cost Considerations
~~~~~~~~~~~~~~~~~~~

**Most Cost-Effective**:
- ``gpt-4o-mini`` (OpenAI)
- ``claude-3-haiku-20240307`` (Anthropic)

**Premium Options**:
- ``gpt-4`` (OpenAI)
- ``claude-3-opus-20240229`` (Anthropic)

Use Case Recommendations
------------------------

Code Generation
~~~~~~~~~~~~~~~

**Best Providers**:

1. **OpenAI** (``gpt-4``, ``gpt-4o-mini``)
   - Excellent code quality
   - Multiple language support
   - Good debugging assistance

.. code-block:: bash

   # Code generation with OpenAI
   drgpt --provider openai --code "Create a REST API with authentication"

2. **Anthropic** (``claude-3-sonnet-20240229``)
   - Clean, well-structured code
   - Good documentation generation
   - Thoughtful architecture decisions

.. code-block:: bash

   # Code with Anthropic
   drgpt --provider anthropic --code "Design a scalable database schema"

Writing and Analysis
~~~~~~~~~~~~~~~~~~~~

**Best Provider**: **Anthropic Claude**

- Superior writing quality
- Detailed analysis capabilities
- Nuanced understanding of complex topics

.. code-block:: bash

   # Writing assistance with Claude
   drgpt --provider anthropic "Improve this technical documentation"

Research and Factual Queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Best Provider**: **Google Gemini**

- Access to recent information
- Strong factual accuracy
- Good for technical research

.. code-block:: bash

   # Research with Gemini
   drgpt --provider google "Latest developments in renewable energy"

System Administration
~~~~~~~~~~~~~~~~~~~~~

**Best Providers**:

1. **OpenAI** for general commands
2. **Google Gemini** for system-specific information

.. code-block:: bash

   # System commands with OpenAI
   drgpt --provider openai --shell "Optimize PostgreSQL performance"

General Problem Solving
~~~~~~~~~~~~~~~~~~~~~~~~

**Best Provider**: **OpenAI GPT-4**

- Excellent reasoning capabilities
- Balanced responses
- Good at breaking down complex problems

.. code-block:: bash

   # Problem solving with GPT-4
   drgpt --provider openai --model gpt-4 "How do I scale my web application?"

Provider Switching Strategies
-----------------------------

Task-Based Switching
~~~~~~~~~~~~~~~~~~~~

Use different providers for different types of tasks:

.. code-block:: bash

   # Research phase - use Gemini
   drgpt --provider google "Research microservices architecture patterns"
   
   # Analysis phase - use Claude
   drgpt --provider anthropic "Analyze pros and cons of microservices"
   
   # Implementation phase - use OpenAI
   drgpt --provider openai --code "Create microservice template"

Quality vs Speed Trade-offs
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Quick questions - fast models
   drgpt --provider openai --model gpt-4o-mini "Brief explanation of Docker"
   
   # Complex analysis - premium models
   drgpt --provider anthropic --model claude-3-opus-20240229 "Comprehensive analysis of market trends"

Cost Optimization
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Daily work - cost-effective models
   drgpt --provider openai --model gpt-4o-mini "Code review suggestions"
   
   # Important decisions - premium models
   drgpt --provider openai --model gpt-4 "Architecture decision for critical system"

Advanced Configuration
----------------------

Custom API Endpoints
~~~~~~~~~~~~~~~~~~~~~

For self-hosted or custom API endpoints:

.. code-block:: bash

   # Custom OpenAI-compatible endpoint
   export OPENAI_API_BASE="http://localhost:8000/v1"
   export OPENAI_API_KEY="your-custom-key"

Provider-Specific Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure provider-specific parameters:

.. code-block:: bash

   # Higher creativity for writing tasks
   drgpt --provider anthropic --temperature 0.9 "Write a creative story"
   
   # More focused responses for technical tasks
   drgpt --provider openai --temperature 0.1 "Explain sorting algorithms"

Rate Limiting and Quotas
~~~~~~~~~~~~~~~~~~~~~~~~

Manage API usage across providers:

.. code-block:: bash

   # Check current usage (if supported by provider)
   drgpt --provider openai --usage
   
   # Set conservative limits
   export DRGPT_MAX_TOKENS=1000
   export DRGPT_REQUESTS_PER_MINUTE=10

Provider Status and Monitoring
------------------------------

Checking Provider Health
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Test all providers
   drgpt --test-providers
   
   # Test specific provider
   drgpt --provider openai --test

Monitoring Usage
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Show current configuration
   drgpt --status
   
   # Show provider-specific information
   drgpt --provider openai --info

Error Handling and Fallbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DrGPT can automatically fall back to alternative providers:

.. code-block:: bash

   # Set fallback provider
   export DRGPT_FALLBACK_PROVIDER="anthropic"
   
   # Enable automatic retries
   export DRGPT_RETRY_COUNT=3

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**API Key Not Working**:

.. code-block:: bash

   # Verify API key is set
   echo $OPENAI_API_KEY
   
   # Test with simple query
   drgpt --provider openai "test"

**Provider Not Available**:

.. code-block:: bash

   # List available providers
   drgpt --list-providers
   
   # Check provider status
   drgpt --provider openai --status

**Rate Limits Exceeded**:

.. code-block:: bash

   # Switch to different provider
   drgpt --provider anthropic "your question"
   
   # Use lower-tier model
   drgpt --provider openai --model gpt-3.5-turbo "your question"

Best Practices
--------------

API Key Security
~~~~~~~~~~~~~~~~

1. **Never commit API keys** to version control
2. **Use environment variables** for API keys
3. **Rotate keys regularly**
4. **Use least-privilege keys** when possible

Provider Selection Guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Start with cost-effective models** for testing
2. **Use premium models** for important tasks
3. **Match provider strengths** to your use case
4. **Test different providers** for your specific needs

Cost Management
~~~~~~~~~~~~~~~

1. **Monitor usage** across providers
2. **Set spending limits** where available
3. **Use cheaper models** for routine tasks
4. **Cache responses** for repeated queries

Future Providers
----------------

DrGPT is designed to easily support new AI providers. Planned additions include:

* **Azure OpenAI Service**
* **AWS Bedrock**
* **Cohere**
* **Local AI models** (Ollama, LocalAI)

Contributing new provider support is welcome - see our contributing guide for details.

Next Steps
----------

* :doc:`models` - Detailed model comparison and selection
* :doc:`../configuration` - Advanced configuration options
* :doc:`../examples/use_cases` - Provider-specific examples
* :doc:`../troubleshooting` - Detailed troubleshooting guide
