import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API Key
api_key = os.getenv("GROQ_API_KEY")

# Create Groq Client
client = Groq(api_key=api_key)

# -------------------- PAGE SETTINGS --------------------
st.set_page_config(
    page_title="AI Travel Guide",
    page_icon="🌍",
    layout="centered"
)

# -------------------- TITLE --------------------
st.title("🌍 AI Travel Guide Chatbot")
st.write("Plan your perfect trip with AI!")

# -------------------- SIDEBAR --------------------
st.sidebar.title("✨ Features")
st.sidebar.markdown("""
- 🌍 Tourist Places
- 💰 Budget Estimation
- 🏨 Hotel Suggestions
- 🍽️ Food Recommendations
- 🚗 Transport Guide
- ☀️ Best Time to Visit
- 🧳 Packing Checklist
- 📅 Travel Itinerary
- 💡 Safety Tips
- 🤖 AI Travel Assistant
""")

# -------------------- USER INPUT --------------------
user_input = st.text_area(
    "Ask anything about travelling...",
    placeholder="Example: Plan a 3-day trip to Murree with a budget of PKR 30,000"
)

# -------------------- BUTTON --------------------
if st.button("Generate Travel Plan"):

    if user_input.strip() == "":
        st.warning("Please enter your question.")
    else:

        system_prompt = """
You are an expert AI Travel Guide.

Always help the user with:

1. Tourist attractions
2. Estimated travel budget
3. Hotel recommendations
4. Food recommendations
5. Transport options
6. Best season to visit
7. Packing checklist
8. Safety tips
9. Suggested itinerary
10. Local culture and useful tips

Always answer in a clear and organized format using headings and bullet points.
"""

        final_prompt = system_prompt + "\n\nUser Question:\n" + user_input

        with st.spinner("Planning your trip..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.7,
                max_tokens=1024
            )

            answer = response.choices[0].message.content

        st.success("Travel Plan Ready!")
        st.markdown(answer)
