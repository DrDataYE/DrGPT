# DrGPT Documentation

This directory contains the complete Sphinx documentation for DrGPT.

## Quick Links

- **[Installation & Quick Start](../README.md#quick-start)** - Get started in 5 minutes
- **[Online Documentation](https://drgpt.readthedocs.io)** - Full documentation
- **[GitHub Repository](https://github.com/DrDataYE/drgpt)** - Source code

## Building Locally

```bash
# Install dependencies
pip install -e ".[docs]"

# Build documentation
make html

# View documentation
open _build/html/index.html
```

## Structure

- `source/` - Sphinx source files
- `examples/` - Usage examples
- `requirements.txt` - Build dependencies

For complete information, see the main [README](../README.md).

1. Edit the `.rst` files in the `source/` directory
2. Build the documentation to test your changes
3. Ensure all cross-references work correctly
4. Submit a pull request with your improvements

## Documentation Guidelines

- Use clear, concise language
- Include practical examples for all features
- Maintain consistent formatting and structure
- Test all code examples
- Keep cross-references up to date
