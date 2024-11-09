import streamlit as st

st.title("Frequently Asked Questions (FAQ)")

faq_items = {
    "What type of health advice can I get?": "Our chatbot provides general health information.",
    "Is this for emergencies?": "No, consult emergency services for serious health concerns.",
    "Can the chatbot diagnose health conditions?": "No, the chatbot does not diagnose health conditions. It's here for general guidance only.",
    "What topics can I ask about?": "You can ask about nutrition, fitness, mental health, lifestyle habits, and preventive care.",
    "How accurate is the information provided by the chatbot?": "The chatbot uses general health information, but it cannot replace advice from a healthcare professional.",
    "Can the chatbot suggest medications?": "No, the chatbot cannot recommend or prescribe medications. Consult a doctor for prescriptions.",
    "Does the chatbot keep my information private?": "Yes, your questions are not stored, and we do not collect any personal health information.",
    "Can I ask about diet and nutrition?": "Yes, the chatbot can provide general advice on diet, nutrition, and healthy eating habits.",
    "Can I use this chatbot if I am managing a chronic condition?": "While the chatbot provides general health advice, you should always consult your doctor for managing chronic conditions.",
    "How should I interpret the advice given by the chatbot?": "Consider the information as general guidance and not a personalized medical opinion.",
    "Is the chatbot available 24/7?": "Yes, you can access the chatbot anytime, but for urgent needs, please contact a medical professional.",
    "Can I ask questions about mental health?": "Yes, the chatbot can provide tips on mental health, stress management, and self-care practices.",
    "Can the chatbot help me understand test results?": "No, only a healthcare provider can accurately interpret medical test results.",
    "Is the chatbot able to give advice on fitness routines?": "Yes, the chatbot can offer general fitness and exercise suggestions based on common wellness practices.",
    "How can I get in touch with a real healthcare provider?": "For medical advice, we recommend scheduling an appointment with a licensed healthcare provider.",
    "What if I want more specific health recommendations?": "The chatbot offers general advice. For personalized guidance, please consult a healthcare professional.",
    "Can I ask questions about supplements?": "Yes, the chatbot can provide general information on common supplements, but consult a healthcare provider before starting any supplement.",
    "Does the chatbot have information on COVID-19 or other infectious diseases?": "Yes, the chatbot provides general guidance on infectious diseases, but follow official health guidelines for the latest information.",
    "Can the chatbot give advice for children's health?": "The chatbot can offer general advice, but consult a pediatrician for any concerns about children's health.",
    "How do I know if I need a doctor?": "If you have severe symptoms or a persistent health issue, we recommend consulting a healthcare professional for evaluation."
}

for question, answer in faq_items.items():
    with st.expander(question):
        st.write(answer)
