def budget_agent(requirements, destination_data):
    """
    Budget Agent
    Estimates the trip budget based on the
    user's budget, duration and destination.
    """

    user_budget = requirements.get("budget", 0)
    duration = requirements.get("duration", 1)
    travellers = requirements.get("travellers", 1)

    destinations = destination_data.get(
        "recommended_destinations", []
    )

    budget_details = []

    for destination in destinations:

        # Basic estimated daily cost per person
        if destination == "Goa":
            daily_cost = 3500

        elif destination == "Manali":
            daily_cost = 4000

        elif destination == "Ooty":
            daily_cost = 3000

        elif destination == "Jaipur":
            daily_cost = 3000

        elif destination == "Kerala":
            daily_cost = 3500

        elif destination == "Hyderabad":
            daily_cost = 2500

        else:
            daily_cost = 3000

        estimated_cost = daily_cost * duration * travellers

        budget_details.append({
            "destination": destination,
            "estimated_cost": estimated_cost,
            "user_budget": user_budget,
            "within_budget": estimated_cost <= user_budget
        })

    return {
        "budget_analysis": budget_details
    }