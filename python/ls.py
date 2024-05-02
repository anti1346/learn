import os
import subprocess

# 현재 작업 디렉토리 가져오기
current_working_directory = os.getcwd()
print("Current working directory:", current_working_directory)

# ls 명령어 실행하여 디렉토리 목록 가져오기
directory_list = subprocess.check_output(['ls', current_working_directory], universal_newlines=True)
print("Directory list:", directory_list)
