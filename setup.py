from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = []
    for line in fh:
        line = line.strip()
        if line and not line.startswith("#"):
            # Extract package name without version specifiers and comments
            package = line.split(">=")[0].split("==")[0].split("<")[0].strip()
            if package:
                requirements.append(line)

setup(
    name="drgpt",
    version="1.0.0",
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
        "License :: OSI Approved :: MIT License",
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
    install_requires=[
        "requests>=2.28.0",
        "rich>=13.0.0"
    ],
    extras_require={
        "openai": ["openai>=1.0.0"],
        "anthropic": ["anthropic>=0.25.0"],
        "all": ["openai>=1.0.0", "anthropic>=0.25.0"],
        "dev": ["pytest>=7.0.0", "black>=22.0.0", "flake8>=5.0.0"]
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
