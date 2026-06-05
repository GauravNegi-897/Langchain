from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

json_schema = {
    "title" : "Review",
    "type" : "object",
    "properties" : {
        "summary" : {
            "type" : "string",
            "description" : "Summary of the review"
        },
        "sentiment" : {
            "type" : "string",
            "description" : "Sentiment of the review"
        },
        "pros" : {
            "type" : "array",
            "items" : {
                "type" : "string"
            },
            "description" : "pros of the device"
        },
        "cons" : {
            "type" : "array",
            "items" : {
                "type" : "string"
            },
            "description" : "cons of the device"
        }
    },
    "required" : ["summary" , "sentiment"]
}

review = """The iPhone 15 delivers a refined smartphone experience with its sleek design, powerful A16 Bionic chip, and impressive 48MP camera that captures sharp and vibrant photos even in low light. The introduction of USB-C is a welcome change, making charging more convenient, while the Dynamic Island adds useful interactive features. However, the device still comes with a 60Hz display, which feels outdated compared to competitors, and its charging speed is relatively slow. It also lacks a telephoto lens and remains quite expensive. Overall, it’s a reliable and premium choice, but not the most value-for-money option in its segment.
"""

structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke(review)

print(result)   