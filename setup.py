from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Define dependencies directly instead of reading from requirements.txt
core_requirements = [
    "requests>=2.28.0",
    "rich>=13.0.0",
    "packaging>=21.0"
]

setup(
    name="drgpt",
    version="2.7.2",
    author="DrGPT Contributors",
    author_email="drdataye@gmail.com",
    description="Multi-Provider AI Assistant for developers and power users",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DrDataYE/drgpt",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Shells",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires=">=3.8",
    install_requires=core_requirements,
    extras_require={
        "openai": ["openai>=1.0.0"],
        "anthropic": ["anthropic>=0.25.0"],
        "all": ["openai>=1.0.0", "anthropic>=0.25.0"],
        "dev": ["pytest>=7.0.0", "black>=22.0.0", "flake8>=5.0.0"],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0",
            "sphinx-autodoc-typehints>=1.12.0",
            "myst-parser>=0.18.0",
            "sphinx-copybutton>=0.5.0",
            "sphinxcontrib-mermaid>=0.7.1",
            "furo>=2021.11.16"
        ]
    },
    entry_points={
        "console_scripts": [
            "drgpt=drgpt.cli.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "drgpt": ["*.md", "*.txt", "*.json"],
    },
    keywords=[
        "ai", "gpt", "openai", "anthropic", "claude", 
        "terminal", "cli", "assistant", "chatgpt",
        "artificial-intelligence", "command-line",
        "developer-tools", "productivity"
    ],
    project_urls={
        "Bug Reports": "https://github.com/DrDataYE/drgpt/issues",
        "Source": "https://github.com/DrDataYE/drgpt",
        "Documentation": "https://github.com/DrDataYE/drgpt/blob/main/README.md",
        "Changelog": "https://github.com/DrDataYE/drgpt/blob/main/CHANGELOG.md",
    },
)
