from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

prompt = input("Enter the query :")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

result = llm.invoke(prompt)
print(result.content)
