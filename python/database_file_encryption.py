import os
import shutil
import subprocess

file_name = 'database'
working_directory = '/home/user1/screwdir'

# 디렉토리 변경
os.chdir(working_directory)

# 운영 체제 확인
if shutil.which('apt-get'):
    result_file_name = 'ubuntu22'
elif shutil.which('yum'):
    result_file_name = 'centos7'
else:
    print("This operating system is not supported.")
    exit(1)

# screwim 명령어 실행
subprocess.run(['screwim', f'{file_name}.inc'])

# 파일 복사
shutil.copyfile(f'{file_name}.inc.screw', f'{file_name}_{result_file_name}.inc')

# 생성된 파일 확인
if os.path.exists(f'{file_name}_{result_file_name}.inc'):
    print("디비 암호화 파일이 생성되었습니다.")
else:
    print("디비 암호화 파일이 생성되지 않았습니다.")
