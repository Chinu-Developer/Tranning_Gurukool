from google import genai
from dotenv import load_dotenv
import time

load_dotenv()

client = genai.Client()
query = input("Gemini: ")
id = None
while True: 
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=query,
        previous_interaction_id=id
    )
    
    print("Gemini Replies: \n\n", interaction.output_text)
    id = interaction.id
    query = input("Gemini:")
    if (query is None) or (query=="exit") :
        break


