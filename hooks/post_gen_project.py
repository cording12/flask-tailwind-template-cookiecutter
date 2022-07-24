import glob
import os
import urllib.request

from colorama import Fore, init

init(autoreset=True)


def _remove_files(file_list: list) -> None:
    """Removes files from the file system

    Args:
        file_list (list): List of files to be removed
    """

    for file in file_list:
        if os.path.exists(file):
            os.remove(file)


def remove_utils():
    """Removes utils.py"""
    _remove_files(["utils.py"])


def remove_poetry():
    """Removes files associated with Poetry"""

    files = ["poetry.lock", "poetry.toml", "pyproject.toml", "utils.py"]
    _remove_files(files)


def remove_pip():
    """Removes files associated with using pip install"""

    files = ["requirements.txt"]
    _remove_files(files)


def install_poetry():
    """
    Installs Poetry + Dependencies
    """
    print(Fore.YELLOW + "[INFO] Installing with Poetry")
    try:
        os.system("poetry install")
        print(Fore.YELLOW + "[INFO] Packages installed with Poetry successfully!")
    except:
        print(Fore.RED + "[ERROR] Failed to install using Poetry")


def install_pip():
    """
    Installs pip dependencies
    """
    print(Fore.YELLOW + "[INFO] Installing with Pip")
    try:
        os.system("pip install -r requirements.txt")
        print(Fore.YELLOW + "[INFO] Packages installed with pip successfully!")
    except:
        print(Fore.RED + "[ERROR] Failed to install using pip")


def install_node_deps():
    """
    Installs node dependencies
    """
    try:
        os.system("npm install")
    except:
        print(Fore.RED + "[ERROR] Failed to install node dependencies")


def _jinja_remove_raw(target_file):
    """
    Remove raw from jinja templates
    """
    raw_strings = ["{% raw %}", "{% endraw %}"]

    with open(target_file, "r") as f:
        file_content = f.read()

    for raw_string in raw_strings:
        file_content = file_content.replace(raw_string, "").strip()

    with open(target_file, "w") as f:
        f.write(file_content)

    return


def remove_jinja_raw():
    """
    Removes the raw tags from jinja templates
    """
    for file in glob.glob("**/*.html", recursive=True):
        _jinja_remove_raw(file)


def fix_missing_lib_js():
    """
    Checks if Cookiecutter copied the application/static/src/js/lib files
    and adds the file if not found
    """
    if os.path.exists("application/static/src/js/lib"):
        return

    target_js_loc = "application/static/src/js/lib"
    os.makedirs(target_js_loc, exist_ok=True)

    urllib.request.urlretrieve(
        "https://code.jquery.com/jquery-3.6.0.min.js",
        f"{target_js_loc}/jquery-3.6.0.min.js",
    )


def main():
    """
    Cleans up file structure depending on user's choices during setup
    """

    if "{{cookiecutter.use_poetry}}" == "y":
        remove_pip()
        install_poetry()
    else:
        remove_poetry()
        install_pip()

    install_node_deps()
    print(Fore.YELLOW + "[INFO] Node dependencies installed successfully!")

    fix_missing_lib_js()

    remove_jinja_raw()
    remove_utils()

    print(Fore.GREEN + "[SUCCESS] Flask app installed successfully!")


if __name__ == "__main__":
    main()
