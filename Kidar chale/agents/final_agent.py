def final_agent(
    requirements,
    destination_data,
    budget_data,
    itinerary_data
):
    """
    Final Agent
    Combines the outputs of all agents
    into one complete travel plan.
    """

    destinations = destination_data.get(
        "recommended_destinations", []
    )

    budget_analysis = budget_data.get(
        "budget_analysis", []
    )

    itineraries = itinerary_data.get(
        "itineraries", {}
    )

    travel_plans = []

    for destination in destinations:

        budget_info = next(
            (
                item
                for item in budget_analysis
                if item["destination"] == destination
            ),
            None
        )

        plan = {
            "destination": destination,
            "duration": requirements.get("duration"),
            "travellers": requirements.get("travellers"),
            "interests": requirements.get("interests"),
            "travel_style": requirements.get("travel_style"),
            "estimated_cost": (
                budget_info["estimated_cost"]
                if budget_info
                else None
            ),
            "within_budget": (
                budget_info["within_budget"]
                if budget_info
                else None
            ),
            "itinerary": itineraries.get(
                destination,
                {}
            )
        }

        travel_plans.append(plan)

    return {
        "travel_plans": travel_plans
    }