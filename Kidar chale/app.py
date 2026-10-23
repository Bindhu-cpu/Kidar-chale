import streamlit as st
import base64


from rag.rag_engine import get_relevant_information

from agents.requirement_agent import requirement_agent
from agents.destination_agent import destination_agent
from agents.budget_agent import budget_agent
from agents.itinerary_agent import itinerary_agent
from agents.final_agent import final_agent


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Kidar Chale?",
    page_icon="🌍",
    layout="wide"
)


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "home"


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Fredoka', sans-serif !important;
}

h1, h2, h3 {
    font-family: 'Fredoka', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: 0.5px;
}
.stApp {
    background: linear-gradient(135deg, #fff7ed, #eef9ff, #f5efff);
}

h1, h2, h3, p, label {
    color: #222222 !important;
}


/* HERO */

.hero {
    text-align: center;
    padding: 35px 20px 25px 20px;
}

.hero-title {
    font-size: 52px;
    font-weight: 800;
    color: #222222;
}

.hero-subtitle {
    font-size: 23px;
    color: #555555;
    margin-top: 8px;
}


/* CARDS */

.card {
    background: white;
    padding: 30px;
    border-radius: 22px;
    text-align: center;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    min-height: 220px;
}

.card-icon {
    font-size: 50px;
}

.card-title {
    font-size: 23px;
    font-weight: 700;
    color: #222222;
    margin-top: 10px;
}

.card-text {
    color: #666666;
    font-size: 16px;
    margin-top: 10px;
}


/* BUTTONS */

.stButton > button {
    background: linear-gradient(90deg, #ff7a18, #ff4b2b) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    padding: 10px !important;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #ff4b2b, #ff7a18) !important;
    color: white !important;
}


/* INFO BOX */

.info-box {
    background: linear-gradient(90deg, #fff0d6, #ffe4e1) !important;
    padding: 20px;
    border-radius: 18px;
    border: 2px solid #ff9f43;
    box-shadow: 0px 6px 20px rgba(255, 120, 50, 0.15);
    text-align: center;
    margin-bottom: 25px;
    font-size: 17px;
    color: #222222 !important;
}

.info-box b {
    color: #e85d04 !important;
}


/* RESULT */

.result-box {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    margin-top: 20px;
}
.hero-title {
    font-size: 64px !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    text-shadow: 3px 3px 0px rgba(255,255,255,0.8);
}

.hero-tagline {
    font-size: 28px !important;
    font-weight: 600 !important;
}

</style>
""", unsafe_allow_html=True)
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(
            image_file.read()
        ).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image:
                linear-gradient(
                    rgba(255, 255, 255, 0.72),
                    rgba(255, 255, 255, 0.72)
                ),
                url("data:image/png;base64,{encoded_image}");

            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


set_background("assets/travel_background.png")

# =========================================================
# HOME PAGE
# =========================================================

if st.session_state.page == "home":

    st.markdown("""
    <div class="hero">
        <div class="hero-title">🌍 KIDAR CHALE?</div>
        <div class="hero-subtitle">No clue? We got you! ✨</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        "<h2 style='text-align:center;'>🧳 How do you want to plan your trip?</h2>",
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2, col3 = st.columns(3)


    # =====================================================
    # DISCOVER
    # =====================================================

    with col1:

        st.markdown("""
        <div class="card">
            <div class="card-icon">🌍</div>
            <div class="card-title">I Don't Know Where To Go</div>
            <div class="card-text">
                Tell us your budget, duration and interests.
                We'll discover the perfect destination for you.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        if st.button(
            "✨ Discover My Trip",
            use_container_width=True
        ):
            st.session_state.page = "discover"
            st.rerun()


    # =====================================================
    # PLAN MY TRIP
    # =====================================================

    with col2:

        st.markdown("""
        <div class="card">
            <div class="card-icon">📍</div>
            <div class="card-title">I Know My Destination</div>
            <div class="card-text">
                Already decided where to go?
                We'll create your complete travel plan.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        if st.button(
            "🗺️ Plan My Trip",
            use_container_width=True
        ):
            st.session_state.page = "destination"
            st.rerun()


    # =====================================================
    # VIBE
    # =====================================================

    with col3:

        st.markdown("""
        <div class="card">
            <div class="card-icon">✨</div>
            <div class="card-title">Plan By My Vibe</div>
            <div class="card-text">
                Beach? Mountains? Adventure?
                Choose your vibe and let AI decide.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        if st.button(
            "🎨 Choose My Vibe",
            use_container_width=True
        ):
            st.session_state.page = "vibe"
            st.rerun()


# =========================================================
# DISCOVER PAGE
# =========================================================

elif st.session_state.page == "discover":

    if st.button("← Back to Home"):
        st.session_state.page = "home"
        st.rerun()

    st.markdown("""
    <div class="hero">
        <div class="hero-title">🌍 Discover Your Trip</div>
        <div class="hero-subtitle">
            Tell us what kind of trip you want ✨
        </div>
    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div class="info-box">
        🌍 Don't know where to go?
        Tell us your budget, duration and interests —
        <b>we'll find the perfect destination for you!</b> ✨
    </div>
    """, unsafe_allow_html=True)


    col1, col2 = st.columns(2)


    with col1:

        budget = st.number_input(
            "💰 Your Budget (₹)",
            min_value=1000,
            value=20000,
            step=1000
        )

        duration = st.number_input(
            "📅 Trip Duration (Days)",
            min_value=1,
            value=3,
            step=1
        )


    with col2:

        travellers = st.number_input(
            "👥 Number of Travellers",
            min_value=1,
            value=2,
            step=1
        )

        interests = st.multiselect(
            "❤️ What do you like?",
            [
                "🏖️ Beaches",
                "🏔️ Mountains",
                "🌲 Nature",
                "🏛️ History",
                "🍜 Food",
                "🎢 Adventure",
                "🌃 Nightlife",
                "🧘 Relaxation"
            ]
        )


    travel_style = st.selectbox(
        "🚗 Travel Style",
        [
            "💸 Budget Friendly",
            "⚖️ Balanced",
            "✨ Comfortable",
            "👑 Luxury"
        ]
    )


    st.write("")


    if st.button(
        "✨ Find My Perfect Trip",
        use_container_width=True
    ):

        query = f"""
Find travel destinations for:

Budget: ₹{budget}
Duration: {duration} days
Travellers: {travellers}
Interests: {interests}
Travel style: {travel_style}
"""

        results = get_relevant_information(query)

        st.session_state.rag_results = results

        st.session_state.trip_data = {
            "budget": budget,
            "duration": duration,
            "travellers": travellers,
            "interests": interests,
            "travel_style": travel_style
        }

        st.session_state.page = "processing"
        st.rerun()


# =========================================================
# DESTINATION PAGE
# =========================================================

elif st.session_state.page == "destination":

    if st.button("← Back to Home"):
        st.session_state.page = "home"
        st.rerun()


    st.markdown("""
    <div class="hero">
        <div class="hero-title">📍 Plan My Trip</div>
        <div class="hero-subtitle">
            Already know where you want to go? ✨
        </div>
    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div class="info-box">
        📍 Enter your destination and we'll build your
        <b>complete travel plan</b> around it! 🗺️
    </div>
    """, unsafe_allow_html=True)


    destination = st.text_input(
        "📍 Where do you want to go?",
        placeholder="Example: Goa"
    )


    col1, col2 = st.columns(2)


    with col1:

        budget = st.number_input(
            "💰 Budget (₹)",
            min_value=1000,
            value=20000,
            step=1000
        )


    with col2:

        duration = st.number_input(
            "📅 Duration (Days)",
            min_value=1,
            value=3,
            step=1
        )


    st.write("")


    if st.button(
        "🗺️ Create My Travel Plan",
        use_container_width=True
    ):

        if destination:

            query = f"""
Create a travel plan for:

Destination: {destination}
Budget: ₹{budget}
Duration: {duration} days
"""

            results = get_relevant_information(query)

            st.session_state.rag_results = results

            st.session_state.trip_data = {
                "destination": destination,
                "budget": budget,
                "duration": duration,
                "travellers": 1,
                "interests": [],
                "travel_style": "⚖️ Balanced"
            }

            st.session_state.page = "processing"
            st.rerun()

        else:

            st.warning("Please enter a destination first.")


# =========================================================
# VIBE PAGE
# =========================================================

elif st.session_state.page == "vibe":

    if st.button("← Back to Home"):
        st.session_state.page = "home"
        st.rerun()


    st.markdown("""
    <div class="hero">
        <div class="hero-title">✨ Plan By My Vibe</div>
        <div class="hero-subtitle">
            You choose the vibe. We find the destination. 🌍
        </div>
    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div class="info-box">
        ✨ Choose your travel vibe and let our AI
        <b>discover a destination for you!</b>
    </div>
    """, unsafe_allow_html=True)


    vibe = st.selectbox(
        "🎨 What's your vibe?",
        [
            "🏖️ Beach",
            "🏔️ Mountains",
            "🌲 Nature",
            "🎢 Adventure",
            "🏛️ History",
            "🍜 Food",
            "🌃 Nightlife",
            "🧘 Relaxation"
        ]
    )


    col1, col2 = st.columns(2)


    with col1:

        budget = st.number_input(
            "💰 Budget (₹)",
            min_value=1000,
            value=20000,
            step=1000
        )


    with col2:

        duration = st.number_input(
            "📅 Duration (Days)",
            min_value=1,
            value=3,
            step=1
        )


    st.write("")


    if st.button(
        "✨ Find My Vibe Trip",
        use_container_width=True
    ):

        query = f"""
Find travel destinations for this travel vibe:

Vibe: {vibe}
Budget: ₹{budget}
Duration: {duration} days
"""

        results = get_relevant_information(query)

        st.session_state.rag_results = results

        st.session_state.trip_data = {
            "budget": budget,
            "duration": duration,
            "travellers": 1,
            "interests": [vibe],
            "travel_style": "⚖️ Balanced"
        }

        st.session_state.page = "processing"
        st.rerun()


# =========================================================
# PROCESSING PAGE
# =========================================================

elif st.session_state.page == "processing":

    st.markdown("""
    <div class="hero">
        <div class="hero-title">🤖 Planning Your Trip...</div>
        <div class="hero-subtitle">
            Our AI travel team is working for you ✨
        </div>
    </div>
    """, unsafe_allow_html=True)


    trip_data = st.session_state.get(
        "trip_data",
        {}
    )

    rag_results = st.session_state.get(
        "rag_results",
        []
    )


    # -----------------------------------------------------
    # REQUIREMENT AGENT
    # -----------------------------------------------------

    requirements = requirement_agent(
        trip_data
    )


    # -----------------------------------------------------
    # DESTINATION AGENT
    # -----------------------------------------------------

    destination_data = destination_agent(
        requirements,
        rag_results
    )


    # -----------------------------------------------------
    # BUDGET AGENT
    # -----------------------------------------------------

    budget_data = budget_agent(
        requirements,
        destination_data
    )


    # -----------------------------------------------------
    # ITINERARY AGENT
    # -----------------------------------------------------

    itinerary_data = itinerary_agent(
        requirements,
        destination_data
    )


    # -----------------------------------------------------
    # FINAL AGENT
    # -----------------------------------------------------

    final_data = final_agent(
        requirements,
        destination_data,
        budget_data,
        itinerary_data
    )


    st.session_state.final_data = final_data


    st.markdown("""
    <div class="result-box">

    <h3>🔍 Requirement Agent</h3>
    <p>Understanding your travel requirements... ✅</p>

    <h3>🌍 Destination Research Agent</h3>
    <p>Finding suitable destinations... ✅</p>

    <h3>💰 Budget Agent</h3>
    <p>Calculating estimated trip cost... ✅</p>

    <h3>🗓️ Itinerary Agent</h3>
    <p>Building your day-by-day itinerary... ✅</p>

    <h3>✨ Final Agent</h3>
    <p>Preparing your personalized travel plan... ✅</p>

    </div>
    """, unsafe_allow_html=True)


    st.write("")


    if st.button(
        "🌍 Show My Travel Plan",
        use_container_width=True
    ):

        st.session_state.page = "result"
        st.rerun()


# =========================================================
# RESULT PAGE
# =========================================================

elif st.session_state.page == "result":

    if st.button("← Start Again"):
        st.session_state.page = "home"
        st.rerun()


    st.title("🌍 Your Trip Is Ready!")
    st.write("No clue? We got you! ✨")


    final_data = st.session_state.get(
        "final_data",
        {}
    )

    travel_plans = final_data.get(
        "travel_plans",
        []
    )


    if not travel_plans:

        st.error(
            "😕 No travel plan was generated."
        )

    else:

        for plan in travel_plans:

            destination = plan.get(
                "destination",
                "Unknown"
            )

            duration = plan.get(
                "duration",
                0
            )

            travellers = plan.get(
                "travellers",
                1
            )

            estimated_cost = plan.get(
                "estimated_cost",
                0
            )

            within_budget = plan.get(
                "within_budget",
                False
            )

            itinerary = plan.get(
                "itinerary",
                {}
            )


            # -------------------------------------------------
            # DESTINATION
            # -------------------------------------------------

            st.header(
                f"🌴 {destination}"
            )


            col1, col2 = st.columns(2)


            with col1:

                st.metric(
                    "📅 Duration",
                    f"{duration} Days"
                )


            with col2:

                st.metric(
                    "👥 Travellers",
                    travellers
                )


            st.divider()


            # -------------------------------------------------
            # BUDGET
            # -------------------------------------------------

            st.subheader(
                "💰 Estimated Budget"
            )


            st.metric(
                "Total Estimated Cost",
                f"₹{estimated_cost:,}"
            )


            if within_budget:

                st.success(
                    "✅ This trip fits within your budget!"
                )

            else:

                st.warning(
                    "⚠️ This trip is above your selected budget."
                )


            st.divider()


            # -------------------------------------------------
            # ITINERARY
            # -------------------------------------------------

            st.subheader(
                "🗓️ Day-by-Day Itinerary"
            )


            if itinerary:

                for day, activity in itinerary.items():

                    st.markdown(
                        f"### 📅 {day}"
                    )

                    st.info(
                        activity
                    )

            else:

                st.write(
                    "No itinerary available."
                )


            st.divider()


            # -------------------------------------------------
            # TRAVEL INFORMATION
            # -------------------------------------------------

            st.subheader(
                "🚗 Travel Information"
            )

            st.write(
                "✈️ Choose transport according to your budget."
            )

            st.write(
                "🏨 Consider accommodation near major attractions."
            )

            st.write(
                "📍 Explore nearby attractions to reduce travel time."
            )


    st.write("")


    if st.button(
        "✨ Plan Another Trip",
        use_container_width=True
    ):

        st.session_state.page = "home"
        st.rerun()