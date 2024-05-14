import os
from dotenv import load_dotenv, dotenv_values

# .env 파일 경로 설정
dotenv_path = '.env'

# .env 파일로부터 환경 변수 로드
load_dotenv(dotenv_path)

# 방법 1: os.getenv()를 사용하여 환경 변수 로드
api_key_os = os.getenv('API_KEY')
print(f"API Key(os.getenv()): {api_key_os}")

# 방법 2: dotenv_values()를 사용하여 환경 변수 로드
env_vars = dotenv_values(dotenv_path)
api_key_dotenv = env_vars.get('API_KEY')

if api_key_dotenv:
    print(f"API Key(dotenv_values()): {api_key_dotenv}")
else:
    print("API Key를 찾을 수 없습니다.")
