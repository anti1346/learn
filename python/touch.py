import os
import subprocess

file_name = 'exmple.txt'

subprocess.run(["touch", file_name])

context = "Hello, world!!"

with open(file_name, 'w') as f:
    f.write(context)

with open(file_name, 'r') as f:
    file_contents = f.read()
    print("File contents:", file_contents)
