from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict , Annotated , Optional , List
from pydantic import BaseModel , Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Review(BaseModel):
    summary : str = Field(description="Summary of the review")
    sentiment: str = Field(description="Sentiment of the review")
    pros : Optional[List[str]] = Field(default=None , description="pros of the device")
    cons : Optional[List[str]] = Field(default=None , description="cons of the device")

structed_model = model.with_structured_output(Review)

result = structed_model.invoke("""The iPhone 15 delivers a refined smartphone experience with its sleek design, powerful A16 Bionic chip, and impressive 48MP camera that captures sharp and vibrant photos even in low light. The introduction of USB-C is a welcome change, making charging more convenient, while the Dynamic Island adds useful interactive features. However, the device still comes with a 60Hz display, which feels outdated compared to competitors, and its charging speed is relatively slow. It also lacks a telephoto lens and remains quite expensive. Overall, it’s a reliable and premium choice, but not the most value-for-money option in its segment.
""")

print(result)  