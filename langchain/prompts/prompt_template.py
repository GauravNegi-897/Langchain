from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

topic = input("Type your topic : ")
style = input("Type the style of the output : ")
length = input("Type the length of the topic : ")

prompt = PromptTemplate.from_template(
"""
Please summarize the topic titled "{topic}" with the following specifications:
Explanation Style: {style}  
Explanation Length: {length}  

1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  

2. Analogies:  
   - Use relatable analogies to simplify complex ideas.

If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  

Ensure the summary is clear, accurate, and aligned with the provided style and length.
"""
)

formatted_prompt = prompt.format(
    topic=topic,
    style=style,
    length=length
)

result = model.invoke(formatted_prompt)

print(result.content)  # important: access content