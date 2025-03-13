from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# .env 파일의 절대 경로를 지정
env_path = os.getenv("ENV_PATH")  # .env 파일이 있는 실제 경로로 변경
load_dotenv(dotenv_path=env_path)

prompt = ChatPromptTemplate.from_template("나이: {age} 이름: {name} 성별: {gender}")
partial_prompt = prompt.partial(age=10)
print(partial_prompt.format(name="홍길동"))
