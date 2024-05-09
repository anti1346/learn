import subprocess

def is_package_installed(package_name):
    result = subprocess.run(['apt', 'list', '--installed', package_name], capture_output=True, text=True)

    if package_name in result.stdout:
        return True
    else:
        return False

package_name = 'ssacli'
if is_package_installed(package_name):
    print(f"{package_name} 패키지가 시스템 설치되어 있습니다.")
else:
    print(f"{package_name} 패키지가 시스템에 설치되어 있습니다.")
