from dotenv import load_dotenv
from langchain_core.messages import AIMessage , HumanMessage , SystemMessage

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

chat_history = [SystemMessage("You are helpful assistant")]

while True: 
    user_input = input("You : ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(response.content))
    print("Bot : " , response.content)

print(chat_history)