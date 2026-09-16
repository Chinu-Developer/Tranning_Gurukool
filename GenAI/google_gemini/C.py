from google import genai
from dotenv import load_dotenv
import time
load_dotenv()

client = genai.Client()
query = input("Gemini : HI i am your helpful assitant gemini please tell me your query :")
while True:

    
    interaction = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input=query,
    system_instruction="""You are an experienced Travel Planner However you have a peculiar habit of replaying  in the raps.
      Whenever a question is asked you first answer it then create a four line rap as well 
      Example :
      User : Tell me about Bunjee Jumping In Rishikesh 
      Asiistant : Rishikesh is very famous for bunjee jumping .It has highest spot for Bunjee Jumping in India 
      Your Chinmay Sir has jumped from there .
      Here is your rap 
      Yo, listen up close, I got travel advice,
      Rishikesh bridges make you think twice!
    Step off the ledge and you're touching the sky,
    Hear the river roar while you learn how to fly!
      """,
    stream=True,
    generation_config={
         "temperature": 0.7,
         "top_k": 20,
         "max_output_tokens": 400 ,
         }
)
    # print ("Triangulating")
    # for i in  range(5):
    #      print(".",end = "", flush=True)
    #      time.sleep(1)

   # print( "Gemini : here is your answer \n\n",interaction.output_text)
    for event in interaction:
      if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)






    query = input("Gemini : ")
    if (query == "") or (query == "exit") :
         break
       