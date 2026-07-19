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
# =====================================================
# FEATURE 3
# =====================================================

elif feature == "🏨 Hotel Suggestions":

    st.header("🏨 Hotel Suggestions")

    city = st.text_input("Enter City")

    hotel_type = st.selectbox(
        "Hotel Type",
        [
            "Budget",
            "Standard",
            "Luxury",
            "Family",
            "Business"
        ]
    )

    if city:

        prompt = f"Suggest the best {hotel_type} hotels in {city}."

        system_prompt = """
You are a hotel recommendation expert.

ONLY recommend hotels.

Include:
- Hotel Name
- Price Range
- Facilities
- Why it is recommended

Do NOT include:
- Tourist places
- Food
- Budget planning
- Packing list
- Transport
"""

# =====================================================
# FEATURE 4
# =====================================================

elif feature == "🍔 Food Guide":

    st.header("🍔 Food Guide")

    city = st.text_input("Enter City")

    if city:

        prompt = f"Recommend famous foods and restaurants in {city}."

        system_prompt = """
You are a food expert.

ONLY recommend:

- Famous local dishes
- Best restaurants
- Street food
- Desserts
- Drinks

Do NOT include:

- Hotels
- Tourist places
- Budget
- Transport
- Packing
"""

# =====================================================
# FEATURE 5
# =====================================================

elif feature == "💰 Budget Planner":

    st.header("💰 Budget Planner")

    city = st.text_input("Destination")

    budget = st.number_input(
        "Budget (PKR)",
        min_value=5000,
        max_value=1000000,
        value=50000,
        step=5000
    )

    if city:

        prompt = f"Create a travel budget for {city} within PKR {budget}."

        system_prompt = """
You are a travel budget expert.

ONLY estimate:

- Hotel cost
- Food cost
- Transport cost
- Entry ticket cost
- Total estimated budget

Do NOT recommend tourist places or restaurants.
"""

# =====================================================
# FEATURE 6
# =====================================================

elif feature == "🚖 Transport Guide":

    st.header("🚖 Transport Guide")

    city = st.text_input("Destination")

    if city:

        prompt = f"Explain transport options in {city}."

        system_prompt = """
You are a transport guide.

ONLY explain:

- Taxi
- Bus
- Metro
- Train
- Car Rental
- Local transport tips

Do NOT include:

- Hotels
- Food
- Tourist places
- Budget
"""        
