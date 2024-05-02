import os

# 디렉토리 경로 설정
directory_path = '/tmp/python'

# 디렉토리가 존재하지 않는 경우에만 생성
if not os.path.exists(directory_path):
    os.mkdir(directory_path)
    print("디렉토리가 생성되었습니다.")
else:
    print("이미 디렉토리가 존재합니다.")
