vi Editor Integration
====================

DrGPT's ``--editor`` option opens the vi text editor for composing complex prompts before processing them with AI. This is particularly useful for longer queries, detailed requirements, or when you need to carefully craft your input.

Overview
--------

The editor integration provides:

* **vi text editor** for all platforms (consistent experience)
* **Template structure** with helpful comments
* **Comment filtering** (lines starting with # are ignored)
* **Temporary file management** with automatic cleanup
* **Cross-platform compatibility** (Windows, macOS, Linux)

Basic Usage
-----------

Starting the Editor
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Open vi editor for input composition
   drgpt --editor

When you run this command:

1. **vi opens** with a template file
2. **Write your prompt** in the editor
3. **Save and exit** (`:wq` in vi)
4. **DrGPT processes** your input with AI

Editor Template
~~~~~~~~~~~~~~~

When vi opens, you'll see this template:

.. code-block:: text

   # Write your prompt here
   # Lines starting with # will be ignored
   
   [Your cursor starts here]

You can:

* **Write your prompt** after the comments
* **Add your own comments** using # at the start of lines
* **Use multiple lines** for complex requests
* **Structure your content** however you prefer

vi Editor Basics
-----------------

Essential vi Commands
~~~~~~~~~~~~~~~~~~~~~

If you're new to vi, here are the essential commands:

**Entering Insert Mode**:

.. code-block:: text

   i    - Insert before cursor
   a    - Insert after cursor  
   o    - Open new line below
   O    - Open new line above

**Navigation**:

.. code-block:: text

   h    - Move left
   j    - Move down
   k    - Move up
   l    - Move right
   
   w    - Move to next word
   b    - Move to previous word
   0    - Move to beginning of line
   $    - Move to end of line

**Saving and Exiting**:

.. code-block:: text

   :w   - Save file
   :q   - Quit vi
   :wq  - Save and quit
   :q!  - Quit without saving

**Editing**:

.. code-block:: text

   x    - Delete character
   dd   - Delete entire line
   yy   - Copy (yank) line
   p    - Paste after cursor
   u    - Undo last change

Basic Workflow
~~~~~~~~~~~~~~

1. **Start editing**: Press ``i`` to enter insert mode
2. **Write your prompt**: Type your question or request
3. **Add structure**: Use multiple lines and comments as needed
4. **Save and exit**: Press ``Esc``, then type ``:wq`` and press Enter

Example Session
---------------

Let's walk through a complete example:

Starting the Editor
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   $ drgpt --editor

vi opens with the template. Press ``i`` to start writing:

Writing Your Prompt
~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   # Write your prompt here
   # Lines starting with # will be ignored
   
   # I want to create a web application for task management
   # Requirements:
   # - User authentication
   # - Task CRUD operations
   # - Due date tracking
   # - Team collaboration features
   
   Create a comprehensive development plan for a task management web application.
   Include:
   
   1. Technology stack recommendations
   2. Database schema design
   3. API endpoint structure
   4. Frontend component architecture
   5. Authentication and authorization strategy
   
   The application should support:
   - Individual and team workspaces
   - Real-time collaboration
   - Mobile responsiveness
   - Scalability for 1000+ users

Saving and Processing
~~~~~~~~~~~~~~~~~~~~

1. Press ``Esc`` to exit insert mode
2. Type ``:wq`` and press Enter to save and quit
3. DrGPT processes your prompt:

.. code-block:: bash

   Processing your input...
   
   # Task Management Web Application Development Plan
   
   ## Technology Stack Recommendations
   
   ### Backend
   * **Framework**: FastAPI (Python) or Node.js with Express
   * **Database**: PostgreSQL for relational data, Redis for caching
   * **Authentication**: JWT tokens with refresh mechanism
   
   [Detailed response continues...]

Use Cases
---------

Complex Requirements
~~~~~~~~~~~~~~~~~~~

Perfect for detailed specifications:

.. code-block:: text

   # API Design Request
   # Need a comprehensive REST API for e-commerce
   
   Design a REST API for an e-commerce platform with the following requirements:
   
   ## Core Entities
   - Users (customers, admins, vendors)
   - Products (with variants, inventory)
   - Orders (with line items, status tracking)
   - Categories (hierarchical structure)
   
   ## Authentication Requirements
   - Role-based access control
   - OAuth2 integration
   - Session management
   
   ## Business Logic
   - Shopping cart functionality
   - Payment processing workflow
   - Inventory management
   - Order fulfillment tracking

Multi-Part Questions
~~~~~~~~~~~~~~~~~~~~

Break down complex topics:

.. code-block:: text

   # Learning Path for Machine Learning
   # I'm a software developer wanting to transition to ML
   
   I have 5 years of Python experience and want to learn machine learning.
   
   Create a structured learning path that covers:
   
   ## Foundation Knowledge
   - Mathematical prerequisites
   - Statistics and probability
   - Linear algebra essentials
   
   ## Practical Skills
   - Data manipulation with pandas
   - Visualization with matplotlib/seaborn
   - ML algorithms implementation
   
   ## Advanced Topics
   - Deep learning frameworks
   - MLOps and deployment
   - Real-world project ideas
   
   Please provide specific resources, timelines, and hands-on exercises.

Code Review Requests
~~~~~~~~~~~~~~~~~~~

Detailed code analysis:

.. code-block:: text

   # Code Review Request
   # Please review this Python class for improvements
   
   class UserManager:
       def __init__(self):
           self.users = {}
           self.active_sessions = {}
       
       def create_user(self, username, password, email):
           if username in self.users:
               return False
           self.users[username] = {
               'password': password,
               'email': email,
               'created_at': datetime.now()
           }
           return True
   
   # Review focus areas:
   # 1. Security considerations
   # 2. Code structure and design patterns
   # 3. Error handling
   # 4. Performance optimizations
   # 5. Best practices compliance

Documentation Requests
~~~~~~~~~~~~~~~~~~~~~~

Comprehensive documentation generation:

.. code-block:: text

   # Documentation Generation
   # Need complete API documentation for my Flask app
   
   Generate comprehensive API documentation for the following Flask routes:
   
   @app.route('/api/users', methods=['POST'])
   def create_user():
       # Creates a new user account
       pass
   
   @app.route('/api/users/<int:user_id>', methods=['GET'])
   def get_user(user_id):
       # Retrieves user information
       pass
   
   # Documentation should include:
   # - Request/response schemas
   # - Authentication requirements
   # - Error codes and messages
   # - Example requests/responses
   # - Rate limiting information

Advanced Features
-----------------

Comment Structure
~~~~~~~~~~~~~~~~~

Use comments to organize your thoughts:

.. code-block:: text

   # Main Question
   Explain microservices architecture
   
   # Specific Focus Areas
   # - Service communication patterns
   # - Data consistency challenges  
   # - Deployment strategies
   # - Monitoring and observability
   
   # Context
   # I'm migrating from a monolithic architecture
   # Current system handles 10k+ daily users
   # Team size: 6 developers
   
   # Expected Output Format
   # Please structure the response with:
   # 1. Overview and benefits
   # 2. Implementation strategy
   # 3. Common pitfalls to avoid
   # 4. Specific tools and technologies

Multi-Language Content
~~~~~~~~~~~~~~~~~~~~~

Mix languages in your prompts:

.. code-block:: text

   # Multilingual Code Example
   # Need code examples in multiple languages
   
   Create a simple HTTP client that makes GET requests to an API.
   
   Provide implementations in:
   - Python (using requests library)
   - JavaScript (using fetch API)
   - Go (using net/http package)
   - Java (using HttpClient)
   
   Each example should include:
   - Error handling
   - Timeout configuration
   - JSON response parsing

Integration with Other Modes
----------------------------

Editor + Code Mode
~~~~~~~~~~~~~~~~~~

Combine editor with code generation:

.. code-block:: bash

   # First, plan with editor
   drgpt --editor
   # [Write detailed requirements in vi]
   
   # Then generate specific code
   drgpt --code "Implement the user authentication system described"

Editor + Shell Mode
~~~~~~~~~~~~~~~~~~~

Plan then execute:

.. code-block:: bash

   # Plan deployment with editor
   drgpt --editor
   # [Write deployment requirements in vi]
   
   # Generate deployment commands
   drgpt --shell "Create deployment commands for the system described"

Editor + Interactive Mode
~~~~~~~~~~~~~~~~~~~~~~~~~

Start interactive sessions with complex context:

.. code-block:: bash

   # Set complex context with editor
   drgpt --editor
   # [Write detailed project context in vi]
   
   # Continue with interactive mode
   drgpt --interface
   > ! Based on the previous context, what should I implement first?

Best Practices
--------------

Effective Prompt Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Start with context**: Explain your situation
2. **Define requirements**: Be specific about what you need
3. **Specify format**: How you want the response structured
4. **Add constraints**: Any limitations or preferences

Example structure:

.. code-block:: text

   # Context
   [Your current situation and background]
   
   # Requirements
   [What you need to accomplish]
   
   # Specific Questions
   [Detailed questions or requests]
   
   # Output Format
   [How you want the response structured]
   
   # Additional Notes
   [Any other relevant information]

Using Comments Effectively
~~~~~~~~~~~~~~~~~~~~~~~~~~

Comments help organize your thoughts:

.. code-block:: text

   # TODO: Research these topics first
   # IMPORTANT: Focus on security aspects
   # NOTE: This is for a production system
   # DEADLINE: Need this by end of week

Iterative Refinement
~~~~~~~~~~~~~~~~~~~~

Use the editor to refine your prompts:

1. **Write initial version**
2. **Review and improve** clarity
3. **Add missing details**
4. **Restructure** for better flow

Tips and Tricks
---------------

Saving Prompts for Reuse
~~~~~~~~~~~~~~~~~~~~~~~~

Before vi processes the file, you can save it:

.. code-block:: bash

   # In vi, save to a different file first
   :w my_prompt.txt
   # Then save and quit to process
   :wq

Template Creation
~~~~~~~~~~~~~~~~~

Create your own templates:

.. code-block:: bash

   # Create a template file
   cat > ~/.drgpt_template.txt << 'EOF'
   # Project Context
   # - Technology stack:
   # - Team size:
   # - Timeline:
   
   # Requirements
   # 1. 
   # 2. 
   # 3. 
   
   # Question
   
   EOF

Quick Editing Tips
~~~~~~~~~~~~~~~~~~

For faster editing in vi:

.. code-block:: text

   # Navigate quickly
   gg    - Go to top of file
   G     - Go to bottom of file
   /text - Search for "text"
   
   # Edit efficiently
   cw    - Change word
   C     - Change to end of line
   D     - Delete to end of line

Troubleshooting
---------------

vi Not Found (Windows)
~~~~~~~~~~~~~~~~~~~~~~

On Windows, if vi is not available:

1. **Install Git for Windows** (includes vi)
2. **Use Windows Subsystem for Linux** (WSL)
3. **Install vim** via package manager

Editor Crashes
~~~~~~~~~~~~~~

If vi crashes or becomes unresponsive:

1. **Press Ctrl+C** to interrupt
2. **Restart the command**: ``drgpt --editor``
3. **Check terminal settings** if problems persist

File Not Saved
~~~~~~~~~~~~~~

If you exit without saving:

.. code-block:: bash

   # vi warns about unsaved changes
   # Choose one option:
   :q!   # Quit without saving (loses your work)
   :w    # Save first, then :q to quit

Large Files
~~~~~~~~~~~

For very large prompts:

1. **Consider breaking into parts**
2. **Use multiple DrGPT calls**
3. **Save intermediate results**

Next Steps
----------

* :doc:`../examples/use_cases` - See editor integration examples
* :doc:`../modes/code` - Combine with code generation
* :doc:`../modes/shell` - Use with system administration
* :doc:`../api/cli_reference` - Complete command reference
