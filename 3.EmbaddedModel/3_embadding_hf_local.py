from langchain_huggingface import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
text="Gandhinagar is the capital of Gujarat"
vector=embedding.embed_query(text)
print(str(vector))
#also we can embed documents
documents = [
    "Gandhinagar is the capital of Gujarat",
    "Ahmedabad is the largest city in Gujarat", 
    "Vadodara is the cultural capital of Gujarat"
]
vectors=embedding.embed_documents(documents)
print([str(vector) for vector in vectors])