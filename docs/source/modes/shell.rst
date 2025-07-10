Shell Mode
==========

Shell mode (``--shell`` or ``-s``) generates system administration commands and provides interactive execution with safety features. It's designed for DevOps, system administration, and command-line operations.

Overview
--------

Shell mode is optimized for:

* **System administration** tasks
* **DevOps operations** and automation
* **File and directory management**
* **Package management** and software installation
* **Process monitoring** and control
* **Network operations** and diagnostics

The key feature is interactive command execution with three safety options: **Execute**, **Describe**, and **Abort**.

Basic Usage
-----------

.. code-block:: bash

   # Generate system commands
   drgpt --shell "Find all Python files larger than 1MB"
   drgpt -s "Find all Python files larger than 1MB"  # Short form
   
   # Package management
   drgpt --shell "Install Docker on Ubuntu"
   drgpt -s "Install Docker on Ubuntu"  # Short form
   
   # System monitoring
   drgpt --shell "Show disk usage by directory"

Interactive Execution Flow
--------------------------

When you use shell mode, DrGPT follows this workflow:

1. **Generate Command**: AI creates the appropriate shell command
2. **Present Options**: Shows three choices for the generated command
3. **User Decision**: You choose how to proceed

Example interaction:

.. code-block:: bash

   $ drgpt --shell "Find all files larger than 100MB"
   
   Generated Command:
   find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
   
   [E]xecute, [D]escribe, [A]bort (e/d/a):

Execution Options
-----------------

Execute [E]
~~~~~~~~~~~

Runs the command immediately with confirmation:

.. code-block:: bash

   [E]xecute, [D]escribe, [A]bort (e/d/a): e
   
   About to execute: find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
   Continue? [y/N]: y
   
   Executing command...
   -rw-r--r-- 1 user user 150M Oct 15 10:30 /home/user/large_file.zip
   -rw-r--r-- 1 user user 200M Oct 14 09:15 /var/log/system.log

**Safety Features**:

* **Confirmation required** before execution
* **5-minute timeout** protection
* **Error handling** with clear output
* **Process interruption** support (Ctrl+C)

Describe [D]
~~~~~~~~~~~~

Provides detailed explanation of the command:

.. code-block:: bash

   [E]xecute, [D]escribe, [A]bort (e/d/a): d
   
   Command Explanation:
   
   find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
   
   • find / : Search starting from root directory
   • -type f : Only find regular files (not directories)
   • -size +100M : Files larger than 100 megabytes
   • -exec ls -lh {} \; : Execute 'ls -lh' on each found file
   • 2>/dev/null : Suppress permission denied errors

After description, you can still choose to execute or abort.

Abort [A]
~~~~~~~~~

Safely cancels the operation:

.. code-block:: bash

   [E]xecute, [D]escribe, [A]bort (e/d/a): a
   
   Operation aborted. No command was executed.

System Administration Use Cases
-------------------------------

File and Directory Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Find and manage files
   drgpt --shell "Find all log files older than 30 days"
   drgpt --shell "Create a backup of my home directory"
   drgpt --shell "Remove all temporary files in /tmp"
   
   # Directory analysis
   drgpt --shell "Show directory sizes sorted by largest"
   drgpt --shell "Find directories using more than 1GB"

Process Management
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Process monitoring
   drgpt --shell "Show processes using the most CPU"
   drgpt --shell "Find processes listening on port 8080"
   drgpt --shell "Kill all Python processes"
   
   # Service management
   drgpt --shell "Restart the web server service"
   drgpt --shell "Check status of all running services"

Package Management
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Ubuntu/Debian
   drgpt --shell "Install Node.js and npm on Ubuntu"
   drgpt --shell "Update all packages on Ubuntu"
   
   # CentOS/RHEL
   drgpt --shell "Install Docker on CentOS"
   
   # macOS
   drgpt --shell "Install Python 3.9 using Homebrew"

System Monitoring
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Resource monitoring
   drgpt --shell "Show memory usage by process"
   drgpt --shell "Monitor disk I/O in real-time"
   drgpt --shell "Show network connections"
   
   # Log analysis
   drgpt --shell "Show last 100 error messages in system logs"
   drgpt --shell "Monitor access log for 404 errors"

Network Operations
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Network diagnostics
   drgpt --shell "Test connectivity to google.com"
   drgpt --shell "Show all open network ports"
   drgpt --shell "Display routing table"
   
   # Security analysis
   drgpt --shell "Show failed login attempts"
   drgpt --shell "Check for unusual network activity"

DevOps and Development
----------------------

Docker Operations
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Container management
   drgpt --shell "List all Docker containers with their status"
   drgpt --shell "Remove all stopped Docker containers"
   drgpt --shell "Show Docker container resource usage"
   
   # Image management
   drgpt --shell "Remove unused Docker images"
   drgpt --shell "Pull latest version of nginx image"

Git Operations
~~~~~~~~~~~~~~

.. code-block:: bash

   # Repository management
   drgpt --shell "Show git status for all subdirectories"
   drgpt --shell "Find all git repositories in home directory"
   drgpt --shell "Clean up git repository and remove untracked files"

Database Operations
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # MySQL operations
   drgpt --shell "Create a backup of MySQL database"
   drgpt --shell "Show MySQL process list"
   
   # PostgreSQL operations
   drgpt --shell "Connect to PostgreSQL and show all databases"

Web Server Management
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Nginx operations
   drgpt --shell "Check nginx configuration syntax"
   drgpt --shell "Reload nginx configuration"
   
   # Apache operations
   drgpt --shell "Show Apache virtual hosts"
   drgpt --shell "Analyze Apache access logs for traffic patterns"

Cross-Platform Support
----------------------

DrGPT shell mode adapts commands to your operating system:

Linux Commands
~~~~~~~~~~~~~~

.. code-block:: bash

   drgpt --shell "Show system information on Linux"
   # Generates: uname -a && lsb_release -a && free -h && df -h

Windows Commands
~~~~~~~~~~~~~~~~

.. code-block:: bash

   drgpt --shell "Show system information on Windows"
   # Generates: systeminfo && Get-WmiObject -Class Win32_OperatingSystem

macOS Commands
~~~~~~~~~~~~~~

.. code-block:: bash

   drgpt --shell "Show system information on macOS"
   # Generates: system_profiler SPSoftwareDataType && sw_vers

Advanced Features
-----------------

Complex Command Chains
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Multi-step operations
   drgpt --shell "Create a complete backup script for web application"
   drgpt --shell "Setup a development environment for Python project"

Security Operations
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Security auditing
   drgpt --shell "Check for unusual file permissions in /etc"
   drgpt --shell "Show users with sudo privileges"
   drgpt --shell "Audit system for security vulnerabilities"

Performance Analysis
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # System performance
   drgpt --shell "Generate a comprehensive system performance report"
   drgpt --shell "Find bottlenecks in system performance"

Automation Scripts
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Script generation
   drgpt --shell "Create a backup script that runs daily"
   drgpt --shell "Generate a system health check script"

Safety Features
---------------

Command Validation
~~~~~~~~~~~~~~~~~~

Before execution, DrGPT validates commands for:

* **Destructive operations**: Extra confirmation for dangerous commands
* **Syntax errors**: Basic command syntax checking  
* **Permission requirements**: Warns about sudo/admin requirements

Timeout Protection
~~~~~~~~~~~~~~~~~~

All commands have built-in protection:

* **5-minute timeout**: Commands automatically terminate
* **Process monitoring**: Track command execution
* **Clean termination**: Proper cleanup on timeout

Error Handling
~~~~~~~~~~~~~~

Comprehensive error handling includes:

* **Command not found**: Clear error messages
* **Permission denied**: Helpful suggestions
* **Network timeouts**: Retry recommendations
* **Resource limits**: Resource usage warnings

Best Practices
--------------

Safe Command Usage
~~~~~~~~~~~~~~~~~~

1. **Always review generated commands** before execution
2. **Use Describe option** for unfamiliar commands
3. **Test on non-production systems** first
4. **Keep backups** before running destructive operations

Effective Prompting
~~~~~~~~~~~~~~~~~~~

Be specific about your environment and requirements:

.. code-block:: bash

   # Good: Specific environment
   drgpt --shell "Install Docker on Ubuntu 20.04 using apt"
   
   # Good: Clear objective
   drgpt --shell "Find all Python processes consuming more than 100MB memory"
   
   # Less effective: Too vague
   drgpt --shell "Fix my server"

Command Verification
~~~~~~~~~~~~~~~~~~~~

For critical operations:

1. Use **Describe** first to understand the command
2. **Test on a non-critical system** if possible
3. **Create backups** before destructive operations
4. **Run with limited scope** initially

Integration with Workflows
--------------------------

Automation Scripts
~~~~~~~~~~~~~~~~~~

Shell mode output can be integrated into automation:

.. code-block:: bash

   # Generate and save commands
   drgpt --shell --no-markdown "Create backup script" > backup.sh
   chmod +x backup.sh
   
   # Review and execute
   cat backup.sh
   ./backup.sh

Documentation
~~~~~~~~~~~~~

Use shell mode to document procedures:

.. code-block:: bash

   # Generate commands for documentation
   drgpt --shell "Show steps to setup PostgreSQL on Ubuntu" >> setup_docs.md

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Command not found**:

.. code-block:: bash

   # Specify the operating system
   drgpt --shell "Install git on Ubuntu Linux"

**Permission denied**:

.. code-block:: bash

   # Request commands with proper permissions
   drgpt --shell "Install software with sudo privileges on Linux"

**Command too complex**:

.. code-block:: bash

   # Break into simpler parts
   drgpt --shell "Step 1: Stop nginx service"
   drgpt --shell "Step 2: Update nginx configuration"
   drgpt --shell "Step 3: Start nginx service"

Platform-Specific Issues
~~~~~~~~~~~~~~~~~~~~~~~~~

**Windows PowerShell**:

.. code-block:: bash

   # Specify PowerShell explicitly
   drgpt --shell "PowerShell command to list services"

**macOS differences**:

.. code-block:: bash

   # Specify macOS for BSD-style commands
   drgpt --shell "macOS command to show disk usage"

Next Steps
----------

* :doc:`interface` - Learn about interactive AI sessions
* :doc:`../examples/use_cases` - See real-world system administration examples
* :doc:`../features/providers` - Choose providers optimized for system commands
* :doc:`../troubleshooting` - Solutions for common shell mode issues
