import os
from dotenv import load_dotenv

# .env 파일 경로 설정
dotenv_path = '.env'

# .env 파일로부터 환경 변수 로드
load_dotenv(dotenv_path)

# .env 파일에 정의된 환경 변수 사용
api_key = os.getenv('API_KEY')
print(f"API Key: {api_key}")