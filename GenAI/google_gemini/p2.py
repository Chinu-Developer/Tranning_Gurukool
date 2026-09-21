from google import genai
from dotenv import load_dotenv
import time

load_dotenv()

client = genai.Client()
query = input("Gemini: ")
while True: 
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=query,
        generation_config={
            "temperature":0.7,
            "top_k":20,
            "max_output_tokens":400},
    )

    print("Triangulating")
    for i in range(5):
        print(".", end ="", flush=True)
        time.sleep(1)
    
    
    print("Gemini Replies: \n\n", interaction.output_text)
    query = input("Gemini:")
    if (query == "") or (query=="exit") :
        break


