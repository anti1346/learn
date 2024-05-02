import os
import subprocess

file_name = 'package_list.txt'

subprocess.run(["touch", file_name])

def is_package_installed(package_name):
    result = subprocess.run(['apt', 'list', '--installed', package_name], capture_output=True, text=True)

    if package_name in result.stdout:
        return True
    else:
        return False

package_name = 'ssacli'
if is_package_installed(package_name):
    print(f"{package_name} 패키지가 시스템에 설치되어 있습니다.")
else:
    print(f"{package_name} 패키지가 시스템에 설치되어 있지 않습니다.")

context = package_name

with open(file_name, 'w') as f:
    f.write(context)

with open(file_name, 'r') as f:
    file_contents = f.read()
    print("File contents:", file_contents)
