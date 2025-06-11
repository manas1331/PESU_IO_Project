# PESU IO Course Project: Health Assistant Bot

## Overview
This project is a Health Assistant Bot built using Google's Gemini model. It is part of the **PES University** (PESU) IO course. The bot provides assistance in health-related topics, offering actionable steps, health tips,location based services and factual information based on user queries. It also features a **Chatbot** page and an **FAQ** page displaying frequently asked questions related to health and wellness.**(Note this is not a replacement to a physician.)**

### Features:
- **Chatbot**: The chatbot interacts with users, answering health-related queries using the Gemini model. 
- **FAQ Page**: A page that displays frequently asked questions along with the bot’s responses.
- **Health Tips**: Provides general health advice like hydration, diet, exercise, and mental well-being.
- **Location-Based Services**: The bot can extract coordinates from user queries and help with location-based searches (e.g., nearby hospitals).

## Installation

To set up the project on your local machine, follow these steps:

### Prerequisites:
- Python 3.x
- Streamlit
- `google-generativeai` library (for interacting with the Gemini model)
- `llama-index` (for prompt management)

### Step-by-Step Setup:

1. Clone the repository:
    ```bash
    git clone https://github.com/<your-github-username>/health-assistant-bot.git
    cd health-assistant-bot
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your **Google Gemini API Key**:
    - Create a project in the Google Cloud Console.
    - Enable the Gemini API.
    - Create an API key and store it in a safe place.
    - Replace `"YOUR_API_KEY"` in the code with your actual API key.

4. Run the Streamlit app:
    ```bash
    streamlit run home.py
    ```

5. Visit the app in your browser at `http://localhost:8501`.

## Usage

Once the application is running, you can interact with the bot through the following pages:

1. **Chatbot**: 
   - Ask health-related questions (e.g., "How can I improve my diet?" or "What are some exercises for back pain?").
   - The bot will provide an AI-generated response using the Gemini model.

2. **FAQ**:
   - Common health queries will be displayed on the FAQ page, where users can find answers to frequently asked questions such as:
     - "How can I stay hydrated?"
     - "What foods are good for immunity?"
     - "How often should I exercise?"

3. **Location-Based Health Services**:
   - You can provide a query with coordinates (e.g., "(12.9716, 77.5946)") to find nearby hospitals or health facilities.

## Code Structure

- `app.py`: Main Streamlit app for running the chatbot and FAQ pages.
- `chatbot.py`: Handles the chatbot interactions and responses.
- `faq.py`: Displays the FAQ section with predefined health-related questions and answers.
- `home.py`: Helper functions for generating responses and handling user input.

## Technologies Used

- **Streamlit**: For building the interactive web application.
- **Google Gemini**: For natural language processing and generating health-related responses.
- **Python**: For backend functionality.
- **Regular Expressions**: For extracting coordinates from user queries.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push to your forked repository.
5. Open a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Thanks to **Google Gemini** for providing the powerful generative model used in this project.
- Special thanks to **PES University(PESU I/O)** for providing the opportunity to work on this project.
