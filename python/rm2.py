import os

# 파일 삭제
file_path = 'example.txt'
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} 파일이 삭제되었습니다.")
else:
    print(f"{file_path} 파일이 존재하지 않습니다.")

# 디렉토리 삭제
directory_path = 'example_directory'
if os.path.exists(directory_path):
    os.rmdir(directory_path)
    print(f"{directory_path} 디렉토리가 삭제되었습니다.")
else:
    print(f"{directory_path} 디렉토리가 존재하지 않습니다.")
