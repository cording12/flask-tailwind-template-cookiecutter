# Flask + TailwindCSS Template

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for quickly creating Flask projects with TailwindCSS. Using [Blueprints](https://flask.palletsprojects.com/en/2.1.x/blueprints/) and an [Application Factory](https://flask.palletsprojects.com/en/2.1.x/patterns/appfactories/) pattern, this template allows quick building of Flask apps with minimal configuration and no extensions outside of what is necessary, or applicable, to all projects.

### Flask Extensions included

1. Flask-Assets
2. Flask-Testing
3. Flask-DebugToolbar
4. Flask-Admin

### Features

1. Self-installing using either Pip or Poetry, whichever you choose
2. Self-installing node dependencies

## Installation

1. Install Cookiecutter globally: `pip install cookiecutter`
2. Generate the template `cookiecutter https://github.com/cording12/flask-tailwind-template-cookiecutter.git`
3. Run Tailwind in a terminal with `npm run dev`
4. Run the Flask app

### Local install

This cookiecutter template installs all modules using either Poetry or Pip (as selected in the installation config). If necessary, refer to the README.md of the template package

## To do
- [X] Add Tailwind JIT compiling
- [ ] convert {{ cookiecutter.project_slug }} to git submodule. Current Cookiecutter issue [#1469](https://github.com/cookiecutter/cookiecutter/pull/1469)
- [ ] Configure a Docker version
- [ ] Add license config
- [ ] New default homepage once installed