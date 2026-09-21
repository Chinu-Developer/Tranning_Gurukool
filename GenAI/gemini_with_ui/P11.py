import streamlit as st 
st.title("J Travels ")
from google import genai
from dotenv import load_dotenv
import time

load_dotenv(r"C:\Users\User\Desktop\Training_Python_Beginner\GenAI\google_gemini\.env")

client = genai.Client()
#st.title("Travle Assistant")
st.markdown(
    """
    <style>

    /* Dark Blue Website Background */
    .stApp {
        background-color: #6FAED6;
    }

    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-8px) rotate(3deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }

    @keyframes pulseGlow {
        0% { opacity: 0.6; }
        50% { opacity: 1; filter: drop-shadow(0 0 10px rgba(255,255,255,0.6)); }
        100% { opacity: 0.6; }
    }

    .travel-hero {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        padding: 2.5rem 2rem;
        border-radius: 18px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .travel-icon {
        display: inline-block;
        animation: float 4s ease-in-out infinite;
        font-size: 3.5rem;
        margin-bottom: 5px;
    }

    .travel-title {
        font-size: 3rem;
        margin: 0;
        font-weight: 800;
        letter-spacing: 1px;
        font-family: 'Inter', sans-serif;
        background: linear-gradient(to right, #ffffff, #a8ff78);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .travel-badge {
        margin-top: 15px;
        display: inline-block;
        background: rgba(255, 255, 255, 0.12);
        padding: 6px 18px;
        border-radius: 20px;
        font-size: 0.9rem;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        animation: pulseGlow 3s infinite;
    }

    </style>

    <div class="travel-hero">
        <div class="travel-icon">✈️🌍</div>
        <h1 class="travel-title">J Travels</h1>
        <p style="font-size: 1.2rem; margin-top: 12px; color: #d0d7de; font-weight: 300;">
            Your intelligent companion for seamless journeys, itineraries, and local secrets.
        </p>
        <div class="travel-badge">
            🚀 Ready for takeoff • Let's explore the world
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.caption("Appka Appna Planner")

Location = st.text_input("Where do you want to go Dudee ")
days_no = st.number_input("How many days of trip do you want ", min_value=1 , max_value=40)


budget = st.selectbox("Select Buddget", ["Premium","Standard","Classic"])
travel_type = st.radio("Who are you travelling with ", ["Family", "With Friends" , "Solo"])
Food_type = st.selectbox("Select Your Food Preference  ",["Choose Your Food  Type", "Vegetarian  Food ", "Non-Vegetarian Food" , "Both Of The Choices"])
Sorry_mess = ("The type of service is not available , We will come with asolution shortly  ")


prompt = f""" You are a travel planner if your client wants to go {Location} and for {days_no} days  in the world , 
plan their trip ans share the answer in bulett format  User is saying he is on the budest{budget}  & they are travelling as 
Travel_Type : {travel_type} 
If the user enters their Particular Preference about Food{Food_type} if that particular foof type exists in that 
Particular arear Guve them that recommendation or simply say Sorry that particular type is not available 
If{Food_type} is not available then type this message {Sorry_mess} 
 ,
   also give them a helpful tip about their loaction and say enjoy Your stay along with tips   """
if st.button("Plan Trip"):
    interaction = client.interactions.create(
                model="gemini-3.5-flash-lite",
                input= prompt
    )


    with st.spinner("Wait for it...", show_time=True):
            time.sleep(5)
    
    st.success("Hoorray !! here are some Goated suggestions ")
    st.write(interaction.output_text) 
    st.balloons()