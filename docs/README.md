# DrGPT Documentation

This directory contains the complete Sphinx documentation for DrGPT.

## Building the Documentation

### Prerequisites

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Build HTML Documentation

```bash
# Build the documentation
sphinx-build -b html source build

# Or use make (if available)
make html
```

### Build with Auto-reload

For development, you can use sphinx-autobuild to automatically rebuild when files change:

```bash
sphinx-autobuild source build
```

This will start a local server at http://localhost:8000 that automatically refreshes when you make changes.

### Viewing the Documentation

After building, open `build/index.html` in your web browser to view the documentation.

## Documentation Structure

- **source/**: Source files for the documentation
  - **modes/**: Documentation for DrGPT's four modes (standard, code, shell, interface)
  - **features/**: Advanced features (providers, models, vi editor integration)
  - **api/**: CLI reference and API documentation
  - **examples/**: Real-world use cases and workflow examples
  - **_static/**: Static files (CSS, images, etc.)
- **build/**: Generated HTML documentation (created after building)
- **requirements.txt**: Python dependencies for building documentation

## Contributing to Documentation

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
