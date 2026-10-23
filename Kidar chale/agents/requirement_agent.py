def requirement_agent(trip_data):
    """
    Requirement Agent
    Understands and organizes all user travel requirements.
    """

    requirements = {
        "destination": trip_data.get("destination"),
        "budget": trip_data.get("budget"),
        "duration": trip_data.get("duration"),
        "travellers": trip_data.get("travellers", 1),

        "food_preference": trip_data.get(
            "food_preference",
            "🍛 Local Food"
        ),

        "transport": trip_data.get(
            "transport",
            "🚗 Car / Cab"
        ),

        "interests": trip_data.get(
            "interests",
            []
        ),

        "travel_style": trip_data.get(
            "travel_style",
            "⚖️ Balanced"
        ),

        "stay_preference": trip_data.get(
            "stay_preference",
            "🏨 Budget Hotel"
        )
    }

    return requirements