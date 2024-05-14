from dotenv import dotenv_values

# .env 파일에서 API_KEY 환경 변수 로드
env_vars = dotenv_values('.env')

# API_KEY 변수 값 확인
api_key = env_vars.get('API_KEY')

if api_key:
    print(f"API Key: {api_key}")
else:
    print("API Key를 찾을 수 없습니다.")
