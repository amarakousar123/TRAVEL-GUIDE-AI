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
# =====================================================
# FEATURE 7
# =====================================================

elif feature == "🎒 Packing List":

    st.header("🎒 Packing List")

    city = st.text_input("Destination")

    season = st.selectbox(
        "Season",
        [
            "Summer",
            "Winter",
            "Spring",
            "Autumn"
        ]
    )

    if city:

        prompt = f"Create a packing checklist for {city} during {season}."

        system_prompt = """
You are a travel packing expert.

ONLY create a packing checklist.

Include:
- Clothes
- Shoes
- Toiletries
- Electronics
- Documents
- Medicines

Do NOT include hotels, food, budget or tourist places.
"""

# =====================================================
# FEATURE 8
# =====================================================

elif feature == "☀️ Best Time to Visit":

    st.header("☀️ Best Time to Visit")

    city = st.text_input("Destination")

    if city:

        prompt = f"What is the best time to visit {city}?"

        system_prompt = """
You are a travel season expert.

ONLY explain:

- Best months
- Weather
- Peak season
- Off season
- Festivals (if relevant)

Do NOT include hotels or budget.
"""

# =====================================================
# FEATURE 9
# =====================================================

elif feature == "🛡 Safety Tips":

    st.header("🛡 Safety Tips")

    city = st.text_input("Destination")

    if city:

        prompt = f"Give travel safety tips for {city}."

        system_prompt = """
You are a travel safety expert.

ONLY provide:

- Safety precautions
- Emergency numbers
- Local laws
- Scams to avoid
- Health advice

Do NOT include hotels, food or itinerary.
"""

# =====================================================
# FEATURE 10
# =====================================================

elif feature == "💬 Ask AI":

    st.header("💬 Ask AI")

    prompt = st.text_area(
        "Ask any travel-related question"
    )

    system_prompt = """
You are an expert AI Travel Guide.

Answer ONLY what the user asks.

Do not add unnecessary information.
"""

# =====================================================
# GENERATE BUTTON
# =====================================================

st.markdown("---")

if st.button("✈️ Generate Answer"):

    if prompt.strip() == "":
        st.warning("Please enter your question or destination.")

    else:

        with st.spinner("🌍 Generating..."):

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

        st.success("✅ Done!")

        st.markdown(answer)

        st.session_state.history.append(("You", prompt))
        st.session_state.history.append(("AI", answer))
# =====================================================
# CHAT HISTORY
# =====================================================

st.markdown("---")
st.subheader("💬 Conversation History")

if len(st.session_state.history) == 0:
    st.info("No conversation yet. Start by selecting a feature from the sidebar.")
else:

    for sender, message in st.session_state.history:

        if sender == "You":
            st.markdown(f"👤 **You:** {message}")

        else:
            st.markdown(f"🤖 **AI:** {message}")

# =====================================================
# DOWNLOAD LAST RESPONSE
# =====================================================

if len(st.session_state.history) > 0:

    last_answer = ""

    for sender, message in reversed(st.session_state.history):

        if sender == "AI":
            last_answer = message
            break

    if last_answer:

        st.download_button(
            label="📥 Download Last Answer",
            data=last_answer,
            file_name="travel_guide_response.txt",
            mime="text/plain"
        )

# =====================================================
# QUICK DESTINATIONS
# =====================================================

st.markdown("---")
st.subheader("🌍 Popular Destinations")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏔 Murree"):
        st.info("Select 'Trip Planner' or another feature from the sidebar, then enter Murree.")

with col2:
    if st.button("🏞 Hunza"):
        st.info("Select 'Trip Planner' or another feature from the sidebar, then enter Hunza.")

with col3:
    if st.button("🏕 Skardu"):
        st.info("Select 'Trip Planner' or another feature from the sidebar, then enter Skardu.")

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption("🌍 AI Travel Guide | Powered by Groq + Streamlit")

