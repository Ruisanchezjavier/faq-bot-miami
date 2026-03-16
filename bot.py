# FAQ Bot for bussiness in Miami
# Builded with Python and OpenAI API

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def answer_question(question):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """You are the virtual assistant for Smile Dental Miami,
                a dental clinic in Doral, FL. Answer frequently asked questions
                from patients in English and Spanish. Be friendly and professional.
                Hours: Monday to Friday 9am-6pm, Saturdays 9am-2pm.
                Phone: (305) 555-1234.
                Services: cleaning, whitening, implants, orthodontics."""
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )
    return response.choices[0].message.content

# Run the bot
print("Bot started. Type 'quit' to exit.")
while True:
    question = input("\nYour question: ")
    if question.lower() == "quit":
        break
    answer = answer_question(question)
    print(f"\nBot: {answer}")