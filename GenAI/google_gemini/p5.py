from google import genai
from dotenv import load_dotenv
import time

load_dotenv()

client = genai.Client()
try:
    with open("chat_1.txt", "r") as f:
        history = f.read()
except FileNotFoundError:
    pass

query = input("Gemini: ")

history = history + "User :" + query
while True: 
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=history
    )

    # print("Triangulating")
    # for i in range(5):
    #     print(".", end ="", flush=True)
    #     time.sleep(1)
    
    
    print("Gemini Replies: \n\n", interaction.output_text)
    history = history + "Assistant :" + interaction.output_text
    query = input("Gemini:")
    history = history + "user :" + query
    
    if (query is None) or (query=="exit") :
        with open("chat_1.txt", "a") as f:
            f.write(history)
        break


