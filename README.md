# DrGPT :zap:

DrGPT is an interactive **Command-Line Interface (CLI) tool** that leverages the GPT model for various tasks such as answering questions, executing shell commands, and more.

## :package: Installation

### Linux

To install DrGPT on a Linux system, use the following commands:

```bash
# Download the .deb package
wget https://github.com/DrDataYE/DrGPT/releases/download/drgpt/drgpt_1.0_beta_all_linux.deb

# Install the package
sudo dpkg -i drgpt_1.0_beta_all_linux.deb
```

## :computer: Usage

After installation, `drgpt` can be used from the command line as follows:

- **Generate and Execute Shell Commands**:
  ```bash
  drgpt --shell "update me system"
  ```

- **Describe Shell Commands**:
  ```bash
  drgpt --describe-shell "ls -hl |grep drgpt"
  ```

- **Generate Code Only**:
  ```bash
  drgpt --code "give me example to use flask in python"
  ```

- **Open Text Editor for Prompt Input**:
  ```bash
  drgpt --editor
  ```

- **Show Version**:
  ```bash
  drgpt --version
  ```

- **Follow a Conversation by ID**:
  ```bash
  drgpt --chat <chat_id>
  ```

- **Save Output to File**:
  ```bash
  drgpt --output <file_path>
  ```

For more detailed information, run `drgpt --help`.

## :bulb: Examples

Here are some examples of how to use DrGPT:

1. **Shell Command Generation**:

   ![Shell Command Generation](images/shell_command_example.png)

   ```bash
   drgpt --shell "install metasploit framework in me system"
   ```

2. **Code Generation**:

   ![Code Generation](images/code_generation_example.png)

   ```bash
   drgpt --code "give me code python to reverse shell"
   ```

3. **Conversation Follow-up**:

   ![Conversation Follow-up](images/conversation_followup.png)

   ```bash
   drgpt "How's the weather today?"
   ```

## :memo: Notes

- Ensure Python 3 and other necessary dependencies are installed on your system.
- You may need root permissions to install the package.

## :scroll: License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---

*Enjoy using DrGPT!* :rocket:
