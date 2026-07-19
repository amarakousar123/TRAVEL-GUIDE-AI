feature = st.sidebar.radio(
    "🌍 Select Feature",
    [
        "🏖️ Tourist Places",
        "📅 Trip Planner",
        "💰 Budget Planner",
        "🏨 Hotels",
        "🍔 Food",
        "🚖 Transport",
        "🎒 Packing List",
        "🛡️ Safety Tips",
        "🌤️ Best Time to Visit",
        "💬 Ask Anything"
    ]
)
if feature == "📅 Trip Planner":
    city = st.text_input("Destination")
    days = st.slider("Trip Days",1,15,3)
    trip_type = st.selectbox(
        "Trip Type",
        ["Solo","Family","Friends","Couple","Business"]
    )

    prompt = f"Plan a {days}-day {trip_type} trip to {city}."

elif feature == "💰 Budget Planner":
    city = st.text_input("Destination")
    budget = st.number_input("Budget (PKR)",10000,500000,50000)

    prompt = f"Create a travel plan for {city} within PKR {budget}."

elif feature == "🏨 Hotels":
    city = st.text_input("City")

    prompt = f"Suggest the best hotels in {city}."

elif feature == "🍔 Food":
    city = st.text_input("City")

    prompt = f"Recommend famous foods in {city}."

elif feature == "🎒 Packing List":
    city = st.text_input("Destination")
    season = st.selectbox(
        "Season",
        ["Summer","Winter","Spring","Autumn"]
    )

    prompt = f"Create a packing list for {city} in {season}."
    
if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.history = []
    
st.session_state.history.append(("You",prompt))
st.session_state.history.append(("AI",answer))

st.subheader("💬 Conversation")

for sender,msg in st.session_state.history:
    st.markdown(f"**{sender}:** {msg}")
    if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.history = []
    st.download_button(
    "📥 Download Travel Plan",
    answer,
    file_name="travel_plan.txt"
)
    col1,col2,col3 = st.columns(3)

col1.metric("Countries","190+")
col2.metric("Travel Tips","1000+")
col3.metric("AI Support","24/7")
st.subheader("🚀 Quick Questions")

if st.button("Murree Trip"):
    prompt = "Plan a 3-day trip to Murree."

if st.button("Hunza Trip"):
    prompt = "Plan a 5-day trip to Hunza."

if st.button("Skardu Trip"):
    prompt = "Plan a 7-day trip to Skardu."
