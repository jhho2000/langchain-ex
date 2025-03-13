from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# .env 파일의 절대 경로를 지정
env_path = os.getenv("ENV_PATH")  # .env 파일이 있는 실제 경로로 변경
load_dotenv(dotenv_path=env_path)

chat = ChatOpenAI(
    model_name="gpt-4o-mini", 
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature = 0)
for chunk in chat.stream("달에 관한 시를 써줘"):
    print(chunk.content, end="", flush=True)
