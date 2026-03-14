from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=50
)

result = embedding.embed_query("Gandhinagar is the capital of Gujarat")

print(result)