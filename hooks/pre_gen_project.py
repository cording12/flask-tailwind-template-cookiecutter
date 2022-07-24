import subprocess
import sys

from colorama import Fore, init

init(autoreset=True)


""" Checks if the user has already got NodeJS installed """
try:
    subprocess.check_output(['node', '--version'])
    print(Fore.YELLOW + "[INFO] NodeJS is installed, continuing installation")
except:
    print(Fore.RED + "[WARNINIG] NodeJS is not installed. Please install NodeJS to continue.")
    sys.exit(1)
 