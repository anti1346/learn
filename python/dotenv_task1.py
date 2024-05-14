from dotenv import dotenv_values

# .env 파일에서 환경 변수 로드
env_vars = dotenv_values('.env')

# 환경 변수 사용 예시
if 'API_KEY' in env_vars:
    api_key = env_vars['API_KEY']
    print(f"API Key: {api_key}")
else:
    print("API Key를 찾을 수 없습니다.")
