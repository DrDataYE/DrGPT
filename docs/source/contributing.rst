Contributing to DrGPT
====================

Thank you for considering contributing to DrGPT! This guide will help you get started with contributing to the project.

Ways to Contribute
------------------

There are many ways to contribute to DrGPT:

* **Report bugs** and suggest features
* **Improve documentation** and examples
* **Add new AI providers** or enhance existing ones
* **Implement new features** and modes
* **Optimize performance** and fix bugs
* **Create tests** and improve code coverage
* **Share use cases** and tutorials

Getting Started
---------------

Development Environment Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Clone the repository
   git clone https://github.com/DrDataYE/drgpt.git
   cd drgpt
   
   # Create virtual environment
   python -m venv dev-env
   source dev-env/bin/activate  # Linux/macOS
   dev-env\Scripts\activate     # Windows
   
   # Install in development mode with test dependencies
   pip install -e ".[dev]"
   
   # Run tests to verify setup
   python tests/test_basic.py

Project Structure
~~~~~~~~~~~~~~~~~

Understanding the codebase structure:

.. code-block:: text

   drgpt/
   ├── drgpt/                  # Main package
   │   ├── core/              # Core functionality
   │   │   ├── config.py      # Configuration management
   │   │   ├── ai_interface.py # AI provider interface
   │   │   └── manager.py     # Main manager class
   │   ├── cli/               # Command-line interface
   │   │   └── main.py        # CLI implementation
   │   └── __init__.py        # Package initialization
   ├── tests/                 # Test suite
   ├── docs/                  # Documentation (Sphinx)
   ├── examples/              # Example scripts and use cases
   ├── scripts/               # Development and build scripts
   └── README.md              # Main documentation

Development Workflow
--------------------

1. **Fork and Clone**
   
   .. code-block:: bash
   
      # Fork on GitHub, then clone your fork
      git clone https://github.com/DrDataYE/drgpt.git

2. **Create Feature Branch**
   
   .. code-block:: bash
   
      git checkout -b feature/main

3. **Make Changes**
   
   * Follow coding standards (see below)
   * Add tests for new functionality
   * Update documentation

4. **Test Your Changes**
   
   .. code-block:: bash
   
      # Run existing tests
      python tests/test_basic.py
      
      # Test manually
      python -m drgpt "test question"

5. **Submit Pull Request**
   
   * Create PR against main branch
   * Include clear description of changes
   * Reference any related issues

Coding Standards
----------------

Python Style Guide
~~~~~~~~~~~~~~~~~~

DrGPT follows PEP 8 with some additional conventions:

.. code-block:: python

   # Use type hints
   def process_response(response: str, format_markdown: bool = True) -> str:
       """Process AI response with optional formatting.
       
       Args:
           response: Raw response from AI provider
           format_markdown: Whether to format as markdown
           
       Returns:
           Processed response string
       """
       pass

   # Use descriptive variable names
   api_response = provider.get_response(user_prompt)
   formatted_output = format_response(api_response)

   # Use f-strings for string formatting
   error_message = f"Provider {provider_name} returned error: {error_code}"

Code Organization
~~~~~~~~~~~~~~~~~

* **Keep functions focused**: Single responsibility principle
* **Use meaningful names**: Functions and variables should be self-documenting
* **Add docstrings**: All public functions need documentation
* **Handle errors gracefully**: Use try/except with specific error messages

.. code-block:: python

   def validate_api_key(api_key: str, provider: str) -> bool:
       """Validate API key format for specific provider.
       
       Args:
           api_key: API key to validate
           provider: Provider name (openai, anthropic, google)
           
       Returns:
           True if key format is valid
           
       Raises:
           ValueError: If provider is not supported
       """
       if provider not in SUPPORTED_PROVIDERS:
           raise ValueError(f"Unsupported provider: {provider}")
       
       # Validation logic here
       return True

Testing Guidelines
------------------

Writing Tests
~~~~~~~~~~~~~

DrGPT uses unittest for testing:

.. code-block:: python

   import unittest
   from drgpt.core.config import Config

   class TestConfig(unittest.TestCase):
       
       def setUp(self):
           """Set up test fixtures before each test method."""
           self.config = Config()
       
       def test_default_provider(self):
           """Test default provider configuration."""
           self.assertEqual(self.config.default_provider, "openai")
       
       def test_api_key_validation(self):
           """Test API key validation."""
           # Test valid key
           self.assertTrue(self.config.validate_api_key("sk-test", "openai"))
           
           # Test invalid key
           self.assertFalse(self.config.validate_api_key("invalid", "openai"))

Running Tests
~~~~~~~~~~~~~

.. code-block:: bash

   # Run all tests
   python -m pytest tests/
   
   # Run specific test file
   python tests/test_config.py
   
   # Run with coverage
   python -m pytest tests/ --cov=drgpt

Test Coverage
~~~~~~~~~~~~~

Aim for high test coverage, especially for:

* Core functionality (config, AI interface, manager)
* CLI argument parsing
* Error handling
* Provider integrations

Documentation Guidelines
------------------------

Documentation Structure
~~~~~~~~~~~~~~~~~~~~~~~

DrGPT uses Sphinx for documentation:

* **Narrative documentation**: Guides and tutorials
* **Reference documentation**: API and CLI reference
* **Examples**: Real-world use cases

Writing Documentation
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: rst

   Function Documentation
   ======================
   
   Clear and concise explanations with examples.
   
   Basic Usage
   -----------
   
   .. code-block:: bash
   
      # Example command
      drgpt --provider openai "Your question"
   
   Advanced Options
   ----------------
   
   Detailed explanation of advanced features.

Building Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Install documentation dependencies
   pip install -e ".[docs]"
   
   # Build documentation
   cd docs/
   make html
   
   # View documentation
   open build/html/index.html

Adding New Features
-------------------

New AI Providers
~~~~~~~~~~~~~~~~

To add a new AI provider:

1. **Create provider class** in ``drgpt/core/ai_interface.py``

.. code-block:: python

   class NewProvider(AIProvider):
       """Implementation for New AI Provider."""
       
       def __init__(self, api_key: str, model: str = "default-model"):
           self.api_key = api_key
           self.model = model
       
       def get_response(self, prompt: str, **kwargs) -> str:
           """Get response from New Provider API."""
           # Implementation here
           pass

2. **Add to configuration** in ``drgpt/core/config.py``

.. code-block:: python

   SUPPORTED_PROVIDERS = {
       "openai": OpenAIProvider,
       "anthropic": AnthropicProvider,
       "google": GoogleProvider,
       "newprovider": NewProvider,  # Add here
   }

3. **Add tests** for the new provider

4. **Update documentation** with provider information

New CLI Features
~~~~~~~~~~~~~~~~

To add new CLI options:

1. **Update argument parser** in ``drgpt/cli/main.py``

.. code-block:: python

   parser.add_argument(
       "--new-option",
       action="store_true",
       help="Description of new option"
   )

2. **Implement functionality** in the appropriate module

3. **Add tests** for the new feature

4. **Update CLI reference** documentation

New Modes
~~~~~~~~~

To add a new mode (like --code, --shell):

1. **Add CLI option** for the mode
2. **Implement mode logic** in manager or CLI
3. **Add AI role/prompt** modifications if needed
4. **Create comprehensive tests**
5. **Add mode documentation** with examples

Bug Fixes
----------

Bug Report Process
~~~~~~~~~~~~~~~~~~

When fixing bugs:

1. **Create test that reproduces the bug**
2. **Fix the bug**
3. **Verify test passes**
4. **Add regression test if needed**

Example bug fix workflow:

.. code-block:: python

   def test_bug_reproduction(self):
       """Test that reproduces the reported bug."""
       # This should initially fail
       result = function_with_bug("problematic input")
       self.assertEqual(result, "expected output")
   
   # After fixing the bug, this test should pass

Code Review Process
-------------------

All contributions go through code review:

Pull Request Guidelines
~~~~~~~~~~~~~~~~~~~~~~

* **Clear title and description**: Explain what and why
* **Reference issues**: Link related issues
* **Small, focused changes**: Easier to review
* **Include tests**: For new features and bug fixes
* **Update documentation**: Keep docs current

Review Checklist
~~~~~~~~~~~~~~~~

Reviewers check for:

* **Functionality**: Does it work as intended?
* **Code quality**: Follows coding standards?
* **Tests**: Adequate test coverage?
* **Documentation**: Updated appropriately?
* **Backward compatibility**: No breaking changes?

Release Process
---------------

Version Management
~~~~~~~~~~~~~~~~~~

DrGPT uses semantic versioning (MAJOR.MINOR.PATCH):

* **MAJOR**: Breaking changes
* **MINOR**: New features, backward compatible
* **PATCH**: Bug fixes, backward compatible

Changelog Maintenance
~~~~~~~~~~~~~~~~~~~~

All changes should be documented in ``CHANGELOG.md``:

.. code-block:: markdown

   ## [Unreleased]
   
   ### Added
   - New provider support for XYZ AI
   - Interactive mode improvements
   
   ### Fixed
   - Configuration file parsing bug
   - Memory leak in streaming mode

Community Guidelines
--------------------

Code of Conduct
~~~~~~~~~~~~~~~

* **Be respectful**: Treat all contributors with respect
* **Be constructive**: Provide helpful feedback
* **Be patient**: Remember that everyone is learning
* **Be inclusive**: Welcome contributors of all backgrounds

Communication
~~~~~~~~~~~~~

* **GitHub Issues**: Bug reports and feature requests
* **Pull Requests**: Code contributions and discussions
* **Discussions**: General questions and ideas

Recognition
-----------

Contributors are recognized in:

* **CONTRIBUTORS.md**: All contributors listed
* **Release notes**: Major contributions highlighted
* **Documentation**: Attribution for significant additions

Getting Help
------------

If you need help contributing:

* **Check existing issues**: Similar problems might be discussed
* **Read documentation**: Comprehensive guides available
* **Ask questions**: Create discussion or issue for help
* **Start small**: Begin with documentation or small bug fixes

Development Resources
--------------------

Useful commands for development:

.. code-block:: bash

   # Code formatting
   black drgpt/ tests/
   
   # Linting
   flake8 drgpt/ tests/
   
   # Type checking
   mypy drgpt/
   
   # Security check
   bandit -r drgpt/
   
   # Dependency check
   pip-audit

Development Tools Setup
~~~~~~~~~~~~~~~~~~~~~~

Recommended tools for DrGPT development:

.. code-block:: bash

   # Install development tools
   pip install black flake8 mypy bandit pip-audit pre-commit
   
   # Setup pre-commit hooks
   pre-commit install

Thank You!
----------

Your contributions make DrGPT better for everyone. Whether you're fixing a typo, adding a feature, or improving documentation, every contribution is valuable and appreciated!
