# Project Name

Best

## Table of Contents

- [Installation](#installation)
  - [1. Installing Hatch](#1-installing-hatch)
  - [2. Clone the Project](#2-clone-the-project)
- [Building the Project](#building-the-project)
- [Adding New Dependencies with Hatch](#adding-new-dependencies-with-hatch)

## Installation

### 1. Installing Hatch

Hatch is a Python package manager and project generator. You need to install Hatch on your machine to work with this project.

```bash
pip install hatch
```

You may want to consider using a virtual environment for your project before installing Hatch, as it's a good practice to isolate project dependencies. You can create a virtual environment using venv:

```bash
python -m venv venv
```
Activate the virtual environment:

On macOS and Linux:
```bash
source venv/bin/activate
```

### 2. Clone the Project

Clone this project repository to your local machine:
```bash
git clone https://github.com/your-username/your-project.git
cd your-project
```

### Building the Project

To build and set up the project, follow these steps:

Create a virtual environment (recommended but optional):
```bash
hatch env new
```
Activate the virtual environment:
```bash
hatch env activate
```
Install project dependencies:
```bash
hatch build
```

### Adding New Dependencies with Hatch

You can easily add new dependencies to your project using Hatch:

Edit the pyproject.toml file to include your new dependencies in the [tool.hatch.envs.default] section. For example:
```toml
[tool.hatch.envs.default]
dependencies = [
  "coverage[toml]>=6.5",
]
```

### License
This project is licensed under the MIT License