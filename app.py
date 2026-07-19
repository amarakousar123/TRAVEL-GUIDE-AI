import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# -------------------- LOAD API --------------------
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

# -------------------- PAGE SETTINGS --------------------
st.set_page_config(
    page_title="🌍 AI Travel Guide",
    page_icon="🌍",
    layout="wide"
)

# -------------------- TITLE --------------------
st.title("🌍 AI Travel Guide")
st.write("Plan your perfect trip with AI.")

# -------------------- SESSION --------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -------------------- SIDEBAR --------------------
st.sidebar.title("✈️ Travel Features")

feature = st.sidebar.radio(
    "Choose a Feature",
    [
        "📅 Trip Planner",
        "🏖 Tourist Places",
        "🏨 Hotels",
        "💰 Budget Planner",
        "🍔 Food Guide",
        "🎒 Packing List",
        "🛡 Safety Tips",
        "💬 Ask AI"
    ]
)

st.sidebar.markdown("---")

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.history = []

# -------------------- DASHBOARD --------------------
col1, col2, col3 = st.columns(3)

col1.metric("🌍 Countries", "190+")
col2.metric("🏨 Hotels", "5000+")
col3.metric("🤖 AI", "24/7")

st.markdown("---")

prompt = ""

# -------------------- FEATURE INPUTS --------------------

if feature == "📅 Trip Planner":

    city = st.text_input("Destination")
    days = st.slider("Trip Days", 1, 15, 3)

    trip = st.selectbox(
        "Trip Type",
        ["Solo", "Family", "Friends", "Couple", "Business"]
    )

    if city:
        prompt = f"Create a {days}-day {trip} travel itinerary for {city}."

elif feature == "🏖 Tourist Places":

    city = st.text_input("City")

    if city:
        prompt = f"Suggest the best tourist attractions in {city}."

elif feature == "🏨 Hotels":

    city = st.text_input("City")

    if city:
        prompt = f"Suggest the best hotels in {city}."

elif feature == "💰 Budget Planner":

    city = st.text_input("Destination")

    budget = st.number_input(
        "Budget (PKR)",
        min_value=10000,
        max_value=1000000,
        value=50000
    )

    if city:
        prompt = f"Create a travel plan for {city} within PKR {budget}."

elif feature == "🍔 Food Guide":

    city = st.text_input("City")

    if city:
        prompt = f"Recommend famous foods in {city}."

elif feature == "🎒 Packing List":

    city = st.text_input("Destination")

    season = st.selectbox(
        "Season",
        ["Summer", "Winter", "Spring", "Autumn"]
    )

    if city:
        prompt = f"Create a packing checklist for {city} during {season}."

elif feature == "🛡 Safety Tips":

    city = st.text_input("Destination")

    if city:
        prompt = f"Give travel safety tips for visitors going to {city}."

elif feature == "💬 Ask AI":

    prompt = st.text_area(
        "Ask Anything About Travel"
    )
# -------------------- GENERATE RESPONSE --------------------

if st.button("✈️ Generate Travel Plan"):

    if prompt.strip() == "":
        st.warning("Please enter a destination or your question.")

    else:

        system_prompt = """
You are an expert AI Travel Guide.

Always provide answers using this format:

# Overview

# Tourist Attractions

# Hotels

# Food

# Budget

# Transport

# Best Time to Visit

# Safety Tips

# Extra Travel Advice

Use headings, bullet points and emojis.
"""

        with st.spinner("🌍 Planning your trip..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=1200
            )

        answer = response.choices[0].message.content

        st.success("✅ Travel Plan Ready!")

        st.markdown(answer)

        # Save Chat History
        st.session_state.history.append(("You", prompt))
        st.session_state.history.append(("AI", answer))
        # -------------------- CHAT HISTORY --------------------

st.markdown("---")
st.subheader("💬 Conversation History")

if len(st.session_state.history) == 0:
    st.info("No conversation yet.")
else:
    for sender, message in st.session_state.history:
        if sender == "You":
            st.markdown(f"**🧑 You:** {message}")
        else:
            st.markdown(f"**🤖 AI:** {message}")

# -------------------- DOWNLOAD LAST RESPONSE --------------------

if len(st.session_state.history) > 0:

    last_answer = ""

    for sender, message in reversed(st.session_state.history):
        if sender == "AI":
            last_answer = message
            break

    if last_answer:
        st.download_button(
            label="📥 Download Travel Plan",
            data=last_answer,
            file_name="travel_plan.txt",
            mime="text/plain"
        )

# -------------------- FOOTER --------------------

st.markdown("---")
st.caption("🌍 AI Travel Guide • Powered by Groq & Streamlit")
