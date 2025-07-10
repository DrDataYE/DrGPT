Code Mode
=========

Code mode (``--code`` or ``-c``) is designed for pure code generation without explanations or commentary. It produces clean, ready-to-use code in markdown format, perfect for copying directly into your projects.

Overview
--------

Code mode is optimized for:

* **Pure code generation** without explanations
* **Multiple programming languages** support
* **Ready-to-use snippets** that can be copied directly
* **Consistent markdown formatting** for easy parsing
* **No verbose descriptions** or tutorials

The key difference from standard mode is that code mode focuses exclusively on generating functional code with minimal or no explanatory text.

Basic Usage
-----------

.. code-block:: bash

   # Generate a Python function
   drgpt --code "Create a function to calculate factorial"
   drgpt -c "Create a function to calculate factorial"  # Short form
   
   # Generate JavaScript code
   drgpt --code "Create a React component for a todo list"
   drgpt -c "Create a React component for a todo list"  # Short form
   
   # Generate SQL query
   drgpt --code "Write a query to find top 10 customers by sales"

Output Format
-------------

Code mode always returns responses in this format:

.. code-block:: markdown

   ```language
   // Brief comment if necessary
   actual_code_here()
   ```

**Example output** for "Create a Python function to calculate factorial":

.. code-block:: markdown

   ```python
   def factorial(n):
       if n < 0:
           raise ValueError("Factorial is not defined for negative numbers")
       if n == 0 or n == 1:
           return 1
       return n * factorial(n - 1)
   ```

Supported Languages
-------------------

Code mode supports all major programming languages:

Programming Languages
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Python
   drgpt --code "Create a REST API endpoint using Flask"
   
   # JavaScript/Node.js
   drgpt --code "Create an Express middleware for authentication"
   
   # Java
   drgpt --code "Create a class for handling HTTP requests"
   
   # C++
   drgpt --code "Implement a binary search algorithm"
   
   # Go
   drgpt --code "Create a web server with routing"
   
   # Rust
   drgpt --code "Implement a thread-safe counter"

Web Technologies
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # HTML
   drgpt --code "Create a responsive navigation bar"
   
   # CSS
   drgpt --code "Create a flexbox layout for a dashboard"
   
   # React
   drgpt --code "Create a hook for form validation"
   
   # Vue.js
   drgpt --code "Create a component for data tables"

Database and Query Languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # SQL
   drgpt --code "Create a query with joins for user orders"
   
   # MongoDB
   drgpt --code "Create an aggregation pipeline for analytics"
   
   # GraphQL
   drgpt --code "Create a schema for user management"

Configuration and Scripts
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Docker
   drgpt --code "Create a Dockerfile for a Node.js app"
   
   # Bash
   drgpt --code "Create a script to backup databases"
   
   # PowerShell
   drgpt --code "Create a script to manage Windows services"
   
   # YAML
   drgpt --code "Create a CI/CD pipeline for GitHub Actions"

Use Cases
---------

Function and Class Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Utility functions
   drgpt --code "Create a function to debounce user input in JavaScript"
   
   # Class implementations
   drgpt --code "Create a Python class for handling file operations"
   
   # Algorithm implementations
   drgpt --code "Implement quicksort in C++"

API Development
~~~~~~~~~~~~~~~

.. code-block:: bash

   # REST endpoints
   drgpt --code "Create a FastAPI endpoint for user registration"
   
   # Middleware
   drgpt --code "Create Express middleware for CORS handling"
   
   # Authentication
   drgpt --code "Implement JWT token validation in Python"

Frontend Components
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # React components
   drgpt --code "Create a React component for file upload with progress"
   
   # Vue components
   drgpt --code "Create a Vue component for dynamic forms"
   
   # Pure CSS
   drgpt --code "Create CSS for a loading spinner animation"

Database Operations
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Complex queries
   drgpt --code "Create a SQL query for monthly sales report with aggregations"
   
   # Database schemas
   drgpt --code "Create database tables for e-commerce system"
   
   # ORM models
   drgpt --code "Create SQLAlchemy models for user and orders"

Configuration Files
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Docker configurations
   drgpt --code "Create a docker-compose.yml for web app with database"
   
   # CI/CD pipelines
   drgpt --code "Create a Jenkins pipeline for Python project"
   
   # Infrastructure as code
   drgpt --code "Create Terraform configuration for AWS Lambda"

Advanced Features
-----------------

Multi-Language Projects
~~~~~~~~~~~~~~~~~~~~~~~

Generate code for projects using multiple languages:

.. code-block:: bash

   # Frontend + Backend
   drgpt --code "Create a React component that calls a Python Flask API"
   
   # Database + Application
   drgpt --code "Create a Node.js function that queries PostgreSQL"

Framework-Specific Code
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Django
   drgpt --code "Create Django views for user authentication"
   
   # Spring Boot
   drgpt --code "Create a Spring Boot controller for REST API"
   
   # ASP.NET Core
   drgpt --code "Create a controller for file upload in ASP.NET Core"

Testing and Quality Assurance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Unit tests
   drgpt --code "Create pytest tests for a user registration function"
   
   # Integration tests
   drgpt --code "Create tests for API endpoints using pytest"
   
   # Mock data
   drgpt --code "Create mock data generators for testing"

Best Practices
--------------

Effective Prompting for Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Be specific about requirements**:

.. code-block:: bash

   # Good: Specific requirements
   drgpt --code "Create a Python function that validates email addresses using regex and returns True/False"
   
   # Less effective: Too vague
   drgpt --code "Create a validation function"

2. **Specify the technology stack**:

.. code-block:: bash

   # Good: Clear technology
   drgpt --code "Create a React hook using TypeScript for managing form state"
   
   # Less effective: Unclear technology
   drgpt --code "Create a form handler"

3. **Include important constraints**:

.. code-block:: bash

   # Good: With constraints
   drgpt --code "Create a Python function to sort a list without using built-in sort methods"
   
   # Basic: No constraints
   drgpt --code "Create a function to sort a list"

Working with Generated Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Copy and test immediately**: Code mode output is designed to be functional

2. **Modify as needed**: Use the generated code as a starting point

3. **Combine multiple snippets**: Generate different parts separately if needed

.. code-block:: bash

   # Generate model
   drgpt --code "Create a SQLAlchemy User model"
   
   # Generate API endpoint
   drgpt --code "Create a FastAPI endpoint to create users"
   
   # Generate tests
   drgpt --code "Create pytest tests for user creation endpoint"

Integration with Development Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Code mode integrates well with development tools:

.. code-block:: bash

   # Save to file
   drgpt --code "Create a Python class for database connection" > db_connection.py
   
   # Append to existing file
   drgpt --code "Create helper functions for string manipulation" >> utils.py
   
   # Use in scripts
   CODE=$(drgpt --code --no-markdown "Create a function to validate phone numbers")
   echo "$CODE" >> validators.py

Output Customization
--------------------

Provider Selection for Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Different providers excel at different types of code:

.. code-block:: bash

   # OpenAI GPT-4 for complex algorithms
   drgpt --provider openai --model gpt-4 --code "Implement A* pathfinding algorithm"
   
   # Claude for clean, well-structured code
   drgpt --provider anthropic --code "Create a comprehensive class for file operations"
   
   # Gemini for modern framework code
   drgpt --provider google --code "Create a modern React component with hooks"

Code Style and Conventions
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Specify coding style
   drgpt --code "Create a Python function following PEP 8 conventions for data validation"
   
   # Request specific patterns
   drgpt --code "Create a JavaScript function using async/await pattern for API calls"
   
   # Framework conventions
   drgpt --code "Create a Django model following Django best practices"

Common Patterns
---------------

CRUD Operations
~~~~~~~~~~~~~~~

.. code-block:: bash

   # Database CRUD
   drgpt --code "Create functions for CRUD operations on a User table using SQLAlchemy"
   
   # API CRUD
   drgpt --code "Create RESTful endpoints for managing products in FastAPI"

Authentication and Security
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # JWT handling
   drgpt --code "Create functions for generating and validating JWT tokens"
   
   # Password hashing
   drgpt --code "Create secure password hashing and verification functions"

Data Processing
~~~~~~~~~~~~~~~

.. code-block:: bash

   # File processing
   drgpt --code "Create a function to parse CSV files and return structured data"
   
   # API data transformation
   drgpt --code "Create a function to transform API response data for frontend consumption"

Error Handling
~~~~~~~~~~~~~~

.. code-block:: bash

   # Exception handling
   drgpt --code "Create a Python function with comprehensive error handling for file operations"
   
   # API error handling
   drgpt --code "Create Express middleware for centralized error handling"

Troubleshooting
---------------

Common Issues
~~~~~~~~~~~~~

**Too much explanation in output**:

Make sure you're using the ``--code`` flag:

.. code-block:: bash

   # Correct
   drgpt --code "Create a function"
   
   # Incorrect (will include explanations)
   drgpt "Create a function"

**Code not working as expected**:

1. Check for missing imports or dependencies
2. Verify the context matches your environment
3. Test with minimal examples first

**Wrong programming language**:

Be explicit about the language in your prompt:

.. code-block:: bash

   # Clear language specification
   drgpt --code "Create a Python function for sorting"
   drgpt --code "Create a JavaScript function for sorting"

Next Steps
----------

* :doc:`shell` - Learn about system administration commands
* :doc:`interface` - Explore interactive development workflows
* :doc:`../examples/use_cases` - See real-world coding examples
* :doc:`../features/providers` - Choose the best provider for your coding needs
