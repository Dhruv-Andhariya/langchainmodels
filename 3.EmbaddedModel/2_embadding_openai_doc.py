from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=50
)
documents = [
    "Gandhinagar is the capital of Gujarat",
    "Ahmedabad is the largest city in Gujarat",
    "Vadodara is the cultural capital of Gujarat"
]

result = embedding.embed_documents(documents)

print(result)