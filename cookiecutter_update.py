""" 
Updates the Flask package from local storage. 

Built so that the Flask project can be worked on independent of the Cookiecutter project.
"""

import os
from pathlib import Path
from shutil import copytree, ignore_patterns, rmtree

CUR_DIR = os.getcwd()

SRC_DIR = os.path.dirname(CUR_DIR) + "/flask-tailwind-template"
DEST_DIR = CUR_DIR + "/{{cookiecutter.project_slug}}"


def update_package():
    """ Copies from the Flask directory to the {{cookiecutter.project_slug}} directory
    """

    copytree(
        SRC_DIR,
        DEST_DIR,
        ignore=ignore_patterns(
            "*.pyc", "*.git", "*.idea", "*.DS_Store", ".venv", "node_modules"
        ),
        dirs_exist_ok=True,        
    )


if __name__ == "__main__":
    update_package()