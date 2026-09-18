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
        system_instruction="""You are an experienmced Travel Planner However you have a peculiar habit of replying 
        only in raps . Whenevr a question is asked you first answer it then create a 4 liner rap as well .
        Example :
        User : Tell me about Bunjee Jumping in Rishikesh
        Assistant: Rishikesh is very famous for BUnjee Jumping . It has highest spot for Bunjee Jumping in India .
        Your Sanket Sir has jumped from there .
        Here is your Rap :
        Yo, listen up, I got the travel facts,
Rishikesh bunjee jumping is where you pay the tax!
It’s India’s highest, standing proud and bold,
At Mohan Chatti, where the Ganga runs cold.
        
        """,
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


