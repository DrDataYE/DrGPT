# Contributing to DrGPT

We love your input! We want to make contributing to DrGPT as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

### Pull Requests

Pull requests are the best way to propose changes to the codebase. We actively welcome your pull requests:

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Setting up Development Environment

```bash
# Clone your fork
git clone https://github.com/DrDataYE/drgpt.git
cd drgpt

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests to ensure everything works
python tests/test_basic.py
```

## Code Style

We use several tools to maintain code quality:

- **Black** for code formatting
- **Flake8** for linting
- **pytest** for testing

### Running Code Quality Tools

```bash
# Format code
black drgpt/

# Lint code
flake8 drgpt/

# Run tests
python -m pytest tests/
```

### Pre-commit Setup

We recommend setting up pre-commit hooks:

```bash
pip install pre-commit
pre-commit install
```

## Project Structure

Understanding the project structure will help you contribute effectively:

```
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
├── docs/                  # Documentation
├── examples/              # Example scripts
└── scripts/               # Setup and utility scripts
```

## Testing

### Running Tests

```bash
# Run basic functionality tests
python tests/test_basic.py

# Run specific test modules (when available)
python -m pytest tests/test_config.py

# Run all tests with coverage
python -m pytest tests/ --cov=drgpt
```

### Writing Tests

When adding new features, please include tests:

```python
def test_new_feature():
    """Test description"""
    # Arrange
    # Act  
    # Assert
    pass
```

## Adding New AI Providers

To add support for a new AI provider:

1. **Create Provider Class**: Add a new provider class in `drgpt/core/ai_interface.py`
2. **Update Configuration**: Add provider config to `SUPPORTED_PROVIDERS` in `config.py`
3. **Add Tests**: Create tests for the new provider
4. **Update Documentation**: Add provider to README and docs

### Example Provider Implementation

```python
class NewProvider(AIProvider):
    """New AI Provider"""
    
    def _setup_headers(self):
        """Setup provider-specific headers"""
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })
    
    def generate_completion(self, messages, model, **kwargs):
        """Generate completion from provider"""
        # Implementation here
        pass
    
    def get_models(self):
        """Get available models"""
        return ["model1", "model2"]
```

## Documentation

### Updating Documentation

- Keep README.md up to date with new features
- Add docstrings to all new functions and classes
- Update CHANGELOG.md for significant changes
- Add examples for new functionality

### Documentation Style

We follow Google-style docstrings:

```python
def function_name(param1: str, param2: int) -> bool:
    """Brief description of function.
    
    Longer description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When something goes wrong
    """
    pass
```

## Issue Reporting

### Bug Reports

Great bug reports tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening)

### Feature Requests

Feature requests are welcome! Please provide:

- Clear description of the feature
- Use case and motivation
- Possible implementation approach
- Any breaking changes

## Coding Guidelines

### General Principles

- **Clarity over cleverness**: Write clear, readable code
- **Modularity**: Keep functions and classes focused and small
- **Error handling**: Handle errors gracefully with informative messages
- **Documentation**: Document public APIs and complex logic
- **Testing**: Test new features and bug fixes

### Python Style

- Follow PEP 8 (enforced by flake8)
- Use type hints where possible
- Prefer f-strings for string formatting
- Use meaningful variable and function names

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

Example:
```
Add support for new AI provider

- Implement XYZ provider class
- Add configuration options
- Update documentation
- Add tests

Fixes #123
```

## Community

### Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to uphold this code.

### Getting Help

- **GitHub Issues**: For bugs and feature requests
- **Discussions**: For questions and general discussion
- **Documentation**: Check README and docs first

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be recognized in:
- AUTHORS file
- Release notes
- README acknowledgments

Thank you for contributing to DrGPT! 🎉
