import os
import subprocess

current_directory = os.getcwd()

directory_list = subprocess.check_output(['ls', current_directory], universal_newlines=True)

print("Current working directory:", current_directory)

print(directory_list)

