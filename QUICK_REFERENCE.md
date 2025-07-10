# DrGPT Quick Reference

## Installation
```bash
pip install drgpt
```

## Setup
```bash
# Set API key
drgpt --provider openai --api-key YOUR_KEY

# Or use environment variable
export OPENAI_API_KEY="your-key"
```

## Basic Usage

| Command | Description |
|---------|-------------|
| `drgpt "question"` | General AI assistance |
| `drgpt -c "task"` | Code generation only |
| `drgpt -s "task"` | Shell commands with execution |
| `drgpt -e` | Text editor for complex prompts |
| `drgpt -i` | Interactive chat mode |

## Quick Commands

| Short | Long | Purpose |
|-------|------|---------|
| `-c` | `--code` | Generate code without explanations |
| `-s` | `--shell` | Interactive shell commands |
| `-e` | `--editor` | Open text editor for input |
| `-i` | `--interface` | Start interactive chat |
| `-o` | `--output` | Save to file |
| `--update` | Update DrGPT to latest version |

## Configuration

| Command | Description |
|---------|-------------|
| `drgpt --status` | Show current configuration |
| `drgpt --version` | Show version information |
| `drgpt --update` | Update to latest version |
| `drgpt --list-providers` | List available AI providers |
| `drgpt --provider PROVIDER` | Switch AI provider |

## Examples

```bash
# Generate Python function
drgpt -c "fibonacci calculator"

# Safe shell command execution
drgpt -s "install docker"

# Interactive session
drgpt -i

# Save response to file
drgpt -o response.md "explain machine learning"
```

For complete documentation: https://drgpt.readthedocs.io
