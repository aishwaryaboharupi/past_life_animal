import streamlit as st
import hashlib

# List of animals and their fun descriptions
animal_descriptions = {
    "Lazy Panda 🐼": "You mastered the art of eating and sleeping, occasionally rolling off trees just for fun.",
    "Dramatic Peacock 🦚": "You lived for attention and would scream dramatically if people weren’t looking at you.",
    "Confused Goldfish 🐠": "You forgot things every 5 seconds and spent most of your life staring at your own reflection.",
    "Nervous Squirrel 🐿️": "You spent your days collecting nuts and immediately forgetting where you buried them.",
    "Seagull With No Manners 🦤": "You stole fries from strangers and screamed when confronted.",
    "Royal Cat 🐱": "You expected everyone to serve you and ignored anyone who didn’t.",
    "Chatterbox Parrot 🦜": "You repeated everything you heard and caused drama between pirates."
}

# Function to get an animal based on the name
def get_animal(name):
    hashed_value = int(hashlib.sha256(name.encode()).hexdigest(), 16)
    animal = list(animal_descriptions.keys())[hashed_value % len(animal_descriptions)]
    return animal

# Function to generate the past life animal response
def get_spirit_critter(name):
    animal = get_animal(name)
    return f"🌟 **{name}** – **{animal}** 🌟\n\n_{animal_descriptions[animal]}_"

# Set custom page title
st.set_page_config(page_title="Spirit Critter", page_icon="🦜")

# Custom CSS for new theme
st.markdown(
    """
    <style>
        /* Background: Mystical Wild Theme */
        .stApp {
            background: linear-gradient(135deg, #4B0082, #2E8B57, #8B4513);
            color: white;
        }
        
        /* Title Styling */
        .stTitle {
            font-size: 50px;
            font-weight: bold;
            text-align: center;
            color: #ffffff;
            text-shadow: 3px 3px 8px #000000;
        }
        
        /* Input Box: Now visible while typing */
        .stTextInput input {
            border-radius: 10px;
            border: 3px solid white;
            font-size: 22px;
            text-align: center;
            background-color: rgba(255, 255, 255, 0.2);
            color: black;
            font-weight: bold;
        }

        /* Button Styling */
        .stButton button {
            background-color: #FF4500;
            color: white;
            font-size: 24px;
            font-weight: bold;
            border-radius: 15px;
            padding: 12px 25px;
            box-shadow: 3px 3px 10px black;
        }

        /* Animal Output Styling */
        .animal-output {
            font-size: 30px;
            font-weight: bold;
            color: #fff;
            text-shadow: 2px 2px 8px black;
            text-align: center;
            margin-top: 20px;
            padding: 20px;
            border-radius: 15px;
            background: rgba(255, 255, 255, 0.2);
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌟 Welcome to Spirit Critter 🌟")
name = st.text_input("Enter your name:", "")

if name:
    result = get_spirit_critter(name)
    st.markdown(f"<div class='animal-output'>{result}</div>", unsafe_allow_html=True)
