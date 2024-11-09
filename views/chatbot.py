import streamlit as st
import google.generativeai as genai
from llama_index.core import PromptTemplate
import re

# Removed the st.set_page_config call from here

genai.configure(api_key="AIzaSyDDDHAs0Pvw25zQHP2Qg8t9rzd-70sFBqA")

st.title("Health Assistant Bot")

instruction_str = """\
    You are a health assistant providing information on health topics.
    Respond with actionable steps, health tips, or factual information based on the user’s query.
    Avoid making any medical diagnoses or providing prescriptions.
"""
health_prompt = PromptTemplate(
    """\
    As a health assistant:
    Follow these instructions:
    {instruction_str}
    Query: {query_str}

    Response: """
)

model = genai.GenerativeModel(
    'gemini-1.5-flash',
    system_instruction=[
        '''
        As a health assistant, provide wellness guidance, including tips on hydration, diet, exercise, and mental well-being.
        '''
    ],
    generation_config={
        "temperature": 0.7,
        "top_p": 0.9,
        "top_k": 50,
        "max_output_tokens": 500,
    },
)

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
    st.session_state.chat_history = []

def generate_hospital_map_link(latitude, longitude):
    base_url = "https://www.google.com/maps/search/?api=1"
    query = "hospital"
    return f"{base_url}&query={query}&query_place_id={latitude},{longitude}"

def extract_coordinates(query):
    match = re.search(r'\((-?\d+\.\d+)\s*,\s*(-?\d+\.\d+)\)', query)
    if match:
        latitude = float(match.group(1))
        longitude = float(match.group(2))
        return latitude, longitude
    return None, None

prompt = st.chat_input("Ask about health and wellness")

if prompt:
    st.session_state.chat_history.append({"role": "user", "message": prompt})
    st.chat_message("user").markdown(prompt)

    if "hospital" in prompt.lower():
        latitude, longitude = extract_coordinates(prompt)
        
        if latitude and longitude:
            hospital_url = generate_hospital_map_link(latitude, longitude)
            hospital_response = f"[Click here to view nearby hospitals on Google Maps]({hospital_url})"
        else:
            hospital_response = "Please provide your latitude and longitude in the format (latitude, longitude)."

        st.session_state.chat_history.append({"role": "assistant", "message": hospital_response})
        st.chat_message("assistant").markdown(hospital_response)
    else:
        response = st.session_state.chat_session.send_message(prompt)
        st.session_state.chat_history.append({"role": "assistant", "message": response.text})
        st.chat_message("assistant").markdown(response.text)

st.subheader("Chat History")
for entry in st.session_state.chat_history:
    role = "User" if entry["role"] == "user" else "Assistant"
    st.markdown(f"*{role}:* {entry['message']}")
