import glob
import os
import subprocess


def poetry_export_requirements():
    """
    Generate requirements_temp.txt with Poetry

    poetry export --dev --without-hashes -f requirements.txt -o requirements_temp.txt
    """
    subprocess.call(
        [
            "poetry",
            "export",
            "--dev",
            "--without-hashes",
            "-f",
            "requirements.txt",
            "-o",
            "requirements_temp.txt",
        ], shell=True
    )

    return


def remove_lines_from_requirements():
    """
    Remove unnecessary text from requirements.txt
    """
    with open("requirements_temp.txt", "r") as input:
        with open("requirements.txt", "w") as output:
            for line in input:
                substr = line.split(";",1)
                
                if "\n" not in substr[0]:
                    clean_line = substr[0] + "\n"
                else:
                    clean_line = substr[0]
                
                if clean_line == "":
                    continue
                output.write(clean_line)

    return


def delete_temp_requirements():
    """
    Delete temporary requirements.txt
    """
    file = "requirements_temp.txt"
    os.remove(file) if os.path.exists(file) else None
    return


def poetry_to_requirements():
    """
    Generate requirements.txt with Poetry
    """
    poetry_export_requirements()
    remove_lines_from_requirements()
    delete_temp_requirements()


def jinja_remove_raw(target_file):
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


def jinja_add_raw(target_file):
    """
    Add raw to jinja templates
    """
    raw_strings = ["{% raw %}", "{% endraw %}"]

    with open(target_file, "r") as f:
        file_content = f.read()

    for raw_string in raw_strings:
        if raw_string not in file_content:
            file_content = "{% raw %}\n" + file_content.strip() + "\n{% endraw %}"

    with open(target_file, "w") as f:
        f.write(file_content)

    return


def add_raw_to_html():
    """
    Adds the raw tag to all html files
    """
    for file in glob.glob("**/*.html", recursive=True):
        jinja_add_raw(file)


def remove_raw_from_html():
    """
    Removes the raw tag from all html files
    """
    for file in glob.glob("**/*.html", recursive=True):
        jinja_remove_raw(file)


def prep_for_deploy():
    add_raw_to_html()
    poetry_to_requirements()
    return


def prep_for_dev():
    remove_raw_from_html()
    return


def main():
    prep_for_deploy()
    # prep_for_dev()


if __name__ == "__main__":
    main()
