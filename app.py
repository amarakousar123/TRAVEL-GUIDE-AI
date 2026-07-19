import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# ----------------------------
# LOAD API
# ----------------------------

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# ----------------------------
# PAGE SETTINGS
# ----------------------------

st.set_page_config(
    page_title="🌍 AI Travel Guide",
    page_icon="🌍",
    layout="wide"
)

# ----------------------------
# TITLE
# ----------------------------

st.title("🌍 AI Travel Guide")
st.write("Plan your perfect trip with AI.")

# ----------------------------
# SESSION STATE
# ----------------------------

if "history" not in st.session_state:
    st.session_state.history = []

# ----------------------------
# SIDEBAR
# ----------------------------

st.sidebar.title("✈️ Travel Assistant")

feature = st.sidebar.radio(
    "Choose a Feature",
    (
        "📅 Trip Planner",
        "🏖 Tourist Places",
        "🏨 Hotel Suggestions",
        "🍔 Food Guide",
        "💰 Budget Planner",
        "🚖 Transport Guide",
        "🎒 Packing List",
        "☀️ Best Time to Visit",
        "🛡 Safety Tips",
        "💬 Ask AI"
    )
)

st.sidebar.markdown("---")

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.history = []

# ----------------------------
# TOP CARDS
# ----------------------------

col1, col2, col3 = st.columns(3)

col1.metric("🌍 Countries", "190+")
col2.metric("🤖 AI Support", "24/7")
col3.metric("✈️ Happy Trips", "Unlimited")

st.markdown("---")

prompt = ""
system_prompt = ""

# =====================================================
# FEATURE 1
# =====================================================

if feature == "📅 Trip Planner":

    st.header("📅 Trip Planner")

    city = st.text_input("Destination")

    days = st.slider(
        "Trip Days",
        1,
        15,
        3
    )

    trip_type = st.selectbox(
        "Trip Type",
        [
            "Solo",
            "Family",
            "Friends",
            "Couple",
            "Business"
        ]
    )

    if city:

        prompt = f"Create a {days}-day {trip_type} travel itinerary for {city}."

        system_prompt = """
You are a professional travel planner.

ONLY create a detailed travel itinerary.

Do NOT include:
- Hotels
- Food
- Budget
- Transport
- Safety
unless the user specifically asks.

Use headings and bullet points.
"""

# =====================================================
# FEATURE 2
# =====================================================

elif feature == "🏖 Tourist Places":

    st.header("🏖 Tourist Places")

    city = st.text_input("Enter City")

    if city:

        prompt = f"Recommend the best tourist attractions in {city}."

        system_prompt = """
You are a tourism expert.

ONLY recommend tourist attractions.

Do NOT provide:
- Hotels
- Budget
- Food
- Transport

Explain each place briefly.
"""
        
