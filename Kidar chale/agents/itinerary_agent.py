def itinerary_agent(requirements, destination_data):
    """
    Itinerary Agent
    Creates a simple day-by-day travel plan
    based on the selected destination and duration.
    """

    duration = requirements.get("duration", 1)

    destinations = destination_data.get(
        "recommended_destinations", []
    )

    itineraries = {}

    for destination in destinations:

        if destination == "Goa":

            activities = [
                "🏖️ Baga Beach & Calangute Beach",
                "🌅 Anjuna & Vagator",
                "🏰 Fort Aguada & Panjim",
                "⛪ Basilica of Bom Jesus"
            ]

        elif destination == "Manali":

            activities = [
                "🏔️ Mall Road & Old Manali",
                "🌲 Hadimba Temple & Vashisht",
                "🏂 Solang Valley",
                "❄️ Rohtang Pass"
            ]

        elif destination == "Ooty":

            activities = [
                "🌊 Ooty Lake",
                "🌸 Botanical Garden",
                "🏔️ Doddabetta Peak",
                "🌹 Rose Garden"
            ]

        elif destination == "Jaipur":

            activities = [
                "🏰 Amber Fort",
                "🏛️ City Palace",
                "🪟 Hawa Mahal",
                "🌅 Jal Mahal"
            ]

        elif destination == "Kerala":

            activities = [
                "🌿 Munnar",
                "🚤 Alleppey Backwaters",
                "🏛️ Kochi",
                "🏖️ Varkala"
            ]

        elif destination == "Hyderabad":

            activities = [
                "🕌 Charminar",
                "🏰 Golconda Fort",
                "🌊 Hussain Sagar",
                "🏛️ Salar Jung Museum"
            ]

        else:

            activities = [
                "📍 Explore local attractions",
                "🍜 Try local food",
                "🌅 Visit nearby places",
                "🛍️ Explore local markets"
            ]

        daily_plan = {}

        for day in range(1, duration + 1):

            activity_index = (day - 1) % len(activities)

            daily_plan[f"Day {day}"] = activities[activity_index]

        itineraries[destination] = daily_plan

    return {
        "itineraries": itineraries
    }