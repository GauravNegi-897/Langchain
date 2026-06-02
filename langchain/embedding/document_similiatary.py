from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

document = ["Virat Kohli is the Indian Cricket known for its batting" , "Rohit Sharma is the Cricket Player known for its leadership" , "Jaspreet Bumrah known for its fast bowling"]

query="Tell me about jaspreet bumrah"

embed_document = embeddings.embed_documents(document)
embed_query = embeddings.embed_query(query)

similarity_score = cosine_similarity([embed_query] , embed_document)[0]

index , score = sorted(list(enumerate(similarity_score)) , key=lambda x:x[1])[-1]

print(document[index]) 