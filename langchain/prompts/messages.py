from langchain_core.messages import HumanMessage , AIMessage , SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

messages = [SystemMessage(content="You are helpful assistant") , HumanMessage(content="What is the Capital of India")]

response = model.invoke(messages)

messages.append(AIMessage(response.content))

print(messages) 