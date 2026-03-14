from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv # to load environment variables from .env file- like API keys, database credentials, etc.
load_dotenv()
model=ChatAnthropic(model='claude-3-5-sonnet-20241022')
result=model.invoke('What is the capital of Gujarat ?')
print(result) # it shows many others details along with the answer. To get only the answer we can use .content
print(result.content)