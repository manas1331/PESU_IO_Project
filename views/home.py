import streamlit as st

# def show_home():
st.title("Welcome to Health Chatbot Assistant")
st.image("Images/welcome.jpg", caption="Your health companion at your fingertips.")  # Adjust width as needed

st.write("""
    ## About Us
    Our Health Chatbot is designed to offer accessible, reliable, and quick responses to general health inquiries. We believe that health information should be available to everyone, no matter where they are. While our chatbot doesn’t replace medical professionals, it provides helpful guidance, educational resources, and tips to empower users to make informed choices about their wellness journey.

    ### Our Vision
    At Health Chatbot, we envision a world where technology bridges the gap to health awareness and support. Our goal is to:
    - **Empower Users**: Equip individuals with accessible, evidence-based health information to make informed choices.
    - **Promote Preventative Health**: Encourage users to adopt healthy lifestyle practices and gain insight into preventive care.
    - **Foster Inclusivity**: Make health knowledge accessible to people from all walks of life, regardless of location or circumstances.
    - **Support Mental and Physical Well-being**: Guide users towards balanced living with advice on nutrition, fitness, and mental health.

    Through innovation, empathy, and a commitment to accuracy, we strive to be a reliable health resource, simplifying the journey to better health and well-being. Join us as we bring health knowledge closer to you, ensuring that support is just a conversation away.
""")

st.write("### Quick Links")
st.markdown("""
- [Chatbot](chatbot) - Interact with our AI-powered chatbot.
- [FAQ](faq) - Common questions and answers.
- [Contact Us](mailto:support@healthchatbot.com) - For additional help.
""")
