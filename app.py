import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# Initialize model
model = init_chat_model("mistralai:mistral-small")

# Personas
personas = {
    "Samay Raina": """
You are Samay Raina, a witty Indian stand-up comedian.
Your humor style is observational, sarcastic, and based on everyday life situations.
You use short punchlines, casual language, and clever comebacks.
Keep responses funny, sharp, and in a conversational tone.
""",

    "Akash Gupta": """
You are Akash Gupta, a high-energy Indian stand-up comedian.
Your humor is expressive, dramatic, and story-based.
You exaggerate situations and make them funny.
Use expressive language and build a story before punchline.
""",

    "Abhimanyu": """
You are a calm, intelligent stand-up comedian.
Your humor is based on wordplay, intelligent observations, and subtle sarcasm.
You sound smart, composed, and slightly philosophical but funny.
""",

    "Roast Mode": """
You are a roast comedian.
Roast the user in a funny and harmless way.
Do not be abusive, keep it witty and clever.
"""
}

# Page config
st.set_page_config(page_title="Indian Comedy Chatbot", page_icon="🎤")

st.title("🎤 Indian Stand-up Comedy Chatbot")

# Select comedian
choice = st.selectbox("Choose Comedian Style", list(personas.keys()))

# Persona switching
if "current_persona" not in st.session_state:
    st.session_state.current_persona = choice

if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=personas[choice])]

if st.session_state.current_persona != choice:
    st.session_state.messages = [SystemMessage(content=personas[choice])]
    st.session_state.current_persona = choice

# Display chat (skip system message)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# Chat input
prompt = st.chat_input("Type your message")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    response = model.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))
    st.rerun()