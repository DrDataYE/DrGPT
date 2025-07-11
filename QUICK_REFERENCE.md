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
| `drgpt -i` | Terminal aliases setup |

## Quick Commands

| Short | Long | Purpose |
|-------|------|---------|
| `-c` | `--code` | Generate code without explanations |
| `-s` | `--shell` | Interactive shell commands |
| `-e` | `--editor` | Open text editor for input |
| `-i` | `--interface` | Setup terminal aliases |
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

# Setup terminal aliases (one-time)
drgpt -i

# After setup, use aliases directly:
: "What is AI?"              # Chat
s: "find Python files"       # Shell commands
c: "create sorting function"  # Code only
e:                           # Editor

# Save response to file
drgpt -o response.md "explain machine learning"
```

## Terminal Aliases (after `drgpt -i`)

| Alias | Equivalent | Purpose |
|-------|------------|---------|
| `!` | `drgpt` | Chat with AI |
| `s:` | `drgpt -s` | Shell commands |
| `c:` | `drgpt -c` | Code generation |
| `e:` | `drgpt -e` | Open editor |

For complete documentation: https://drgpt.readthedocs.io
