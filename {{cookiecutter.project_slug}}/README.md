# Installation

### Prerequisites

This application is built in Windows 10 and as such, other operating systems may require alternative configuration. Ensure the below are installed before continuing:

#### Required

- [Python 3.10.x](https://www.python.org/downloads/release/python-3100/)
- [NodeJS](https://nodejs.org/en/)

#### Optional (recommended)

- [Poetry](https://python-poetry.org/docs/)
- [VSCode](https://code.visualstudio.com/) is the recommended IDE as this repo contains non-essential configuration specific to VSCode

### Installing via Cookie Cutter

If installing via cookie cutter, the app will be installed and configured for you.

### Installing with Poetry

- Clone the repo using `git clone https://github.com/cording12/flask-tailwind-template.git`
- In the project root, open a cmd prompt and run `poetry install` to create a venv & install dependencies
- `npm install` to install node packages
- Run `npm run dev` to run Tailwind with JIT compiling
- Either launch Flask in debug mode with the VSCode pre-configured launch, or in a second terminal run ` wsgi.py`
- For production, run `npm run build:prod`


# Configuration recommendations

### **Poetry**

Full configuration information is available in the [Poetry docs](https://python-poetry.org/docs/configuration/).

### **Create virtual environment within project directory**

The default behaviour of Poetry is to create virtual environments in a cache folder, separate to the project. The cache folder's default location is `%LocalAppData%\pypoetry\Cache\virtualenvs`

To create the Python venv within the project directory, you must update the config:

- `poetry config virtualenvs.in-project true`

For a per project level rather than global:

- Run `poetry config virtualenvs.in-project true --local` from the project directory

Check the settings with `poetry config --list`

### **VS Code**

The below configurations for VS Code are optional, but designed to make debugging and development easier and faster.

### **Workspace configuration**

The .code-workspace file contains extension recommendations as well as a debug configuration for debugging the Flask app.

The following settings are used:

- editor
  - formatOnSave - formats the file on save (using Black)
  - codeActionsOnSave - runs the code action. Using ISort, organises imports on save
- launch
  - The config for VSCode to debug the Flask app

### **Extensions**

Recommended extensions for use with the app:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - Provides Python support in VSCode
- [Path Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense) - Adds intellisense for filenames.
- [Thunder-client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client) - API testing tool; think Postman in VSCode
- [PyLance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) - Adds further Python language support
- [Jinja](https://marketplace.visualstudio.com/items?itemName=wholroyd.jinja) - Adds language colorization support for Jinja
- [ISort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort) - Provides import sorting using isort (also installed as a package via pyproject.toml)

