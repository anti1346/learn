#!/bin/bash

file_name="database"
working_directory="/home/user1/screwdir"

# 디렉토리 변경
cd "$working_directory" || exit

# 운영 체제 확인
if command -v apt-get &> /dev/null; then
    result_file_name="ubuntu22"
elif command -v yum &> /dev/null; then
    result_file_name="centos7"
else
    echo "This operating system is not supported."
    exit 1
fi

# screwim 명령어 실행
screwim "${file_name}.inc"

# 파일 복사
cp "${file_name}.inc.screw" "${file_name}_${result_file_name}.inc"

# 생성된 파일 확인
if [ -e "${file_name}_${result_file_name}.inc" ]; then
    echo "디비 암호화 파일이 생성되었습니다."
else
    echo "디비 암호화 파일이 생성되지 않았습니다."
fi
