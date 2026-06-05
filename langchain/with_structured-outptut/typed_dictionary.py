 
from dotenv import load_dotenv
from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Review(TypedDict):
    summary : str
    sentiment: str
    
structed_model = model.with_structured_output(Review)
result = structed_model.invoke("The hardware is great, but the software is bloadted. there are too many pre-installed app that i cant remove. also the UI looks too outdated compated to other brands. Hoping for a software update to fix this") 

print(result)