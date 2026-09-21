# import time
# for i in range(5, 1, -1):
#     print(i, end="...", flush=False)
#     time.sleep(1)


from google import genai
from dotenv import load_dotenv
import time

load_dotenv()


query = input("Gemini: ")
history = "User :" + query
while True: 
    history = history + "Assistant :" + "Model ka Answer"
    query = input("Gemini:")
    history = history + "user :" + query
    
    if (query is None) or (query=="exit") :
        break

print(history)

