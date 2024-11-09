import streamlit as st

# Set page config as the very first Streamlit command
st.set_page_config(page_title="Health Chatbot", page_icon="🤖", layout="centered")

st.logo("Images/logo.png")

with st.sidebar:
    st.title("Health Chatbot")
    st.write("**Welcome!** Navigate through the app to learn more about health guidance and get answers to your health-related questions.")
    st.warning("""**Caution:** This chatbot is intended to provide general health information and guidance. It is **not a substitute** for professional medical advice.""")

home_page = st.Page("views/home.py", title="Home", icon="🏠", default=True)
chatbot_page = st.Page("views/chatbot.py", title="Chatbot", icon="🤖")
faq_page = st.Page("views/faq.py", title="FAQ", icon="🙋🏻‍♂️")

pg = st.navigation({
    "Basic Info": [home_page, faq_page],
    "Chatbot": [chatbot_page],
})

pg.run()

st.markdown("""
<div style='text-align: center; font-size: 20px; margin-top: 50px;'>
    © Copyright 2024 . All rights reserved.
</div>
""", unsafe_allow_html=True)
