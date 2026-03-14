from langchain_openai import OpenAI
from dotenv import load_dotenv # to load environment variables from .env file- like API keys, database credentials, etc.
load_dotenv()
llm = OpenAI(model='gpt-3.5-turbo-instruct')
result = llm.invoke('What is the capital of Gujarat ?')
print(result)