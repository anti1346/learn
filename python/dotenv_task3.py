from dotenv import dotenv_values

# .env 파일에서 환경 변수 로드
env_vars = dotenv_values('.env')

# 환경 변수 사용 예시
for key, value in env_vars.items():
    print(f"{key}: {value}")
