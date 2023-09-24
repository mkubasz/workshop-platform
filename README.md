# Workshop platform


## Table of Contents

- [Workshop platform](#workshop-platform)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Adding a New Package](#adding-a-new-package)
  - [Adding a Development Package](#adding-a-development-package)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python (>= 3.11)
- Poetry (for managing dependencies and building the project)

## Installation

To install the project and its dependencies, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-project.git
   cd your-project
   ```
2. Install Poetry (if not already installed):
    ```bash
    pip install poetry  
    ```
    Set up the project using Poetry: 
    ```bash
    poetry install  
    ```
    This will create a virtual environment and install all the required dependencies.

## Adding a New Package

1. Open a terminal and navigate to your project's root directory, where your pyproject.toml file is located.
2. Use Poetry's add command to add a new package as a runtime dependency. Replace package-name with the name of the package you want to add:
    ```bash
    poetry add package-name
    ```

## Adding a Development Package

Development packages are dependencies that are only required during development, such as testing libraries or code formatting tools. Here's how to add a development package:\
1. Open a terminal and navigate to your project's root directory, where your pyproject.toml file is located.
2. Use Poetry's add command with the --dev flag to add a package as a development dependency. Replace dev-package-name with the name of the development package you want to add:
    ```bash
    poetry add --dev dev-package-name
    ```
3. To install all development dependencies (useful for continuous integration or other developers working on your project), you can run:
   ```bash
   poetry install --no-root
   ```