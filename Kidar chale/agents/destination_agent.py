def destination_agent(requirements, rag_results):
    """
    Destination Research Agent

    Handles both:
    1. User already knows the destination
    2. User wants AI to discover a destination
    """

    # -----------------------------------------------------
    # DESTINATIONS SUPPORTED BY OUR KNOWLEDGE BASE
    # -----------------------------------------------------

    destination_names = [
        "Goa",
        "Manali",
        "Ooty",
        "Jaipur",
        "Kerala",
        "Hyderabad"
    ]

    destinations = []

    # -----------------------------------------------------
    # CASE 1 — USER ALREADY KNOWS DESTINATION
    # -----------------------------------------------------

    chosen_destination = requirements.get("destination")

    if chosen_destination:

        for destination in destination_names:

            if destination.lower() in chosen_destination.lower():
                destinations.append(destination)
                break

        # If destination isn't in our knowledge base,
        # keep the user's destination anyway.
        if not destinations:
            destinations.append(chosen_destination)


    # -----------------------------------------------------
    # CASE 2 — USER WANTS AI TO DISCOVER DESTINATION
    # -----------------------------------------------------

    if not destinations:

        for result in rag_results:

            text = result.get("text", "")

            for destination in destination_names:

                if destination.lower() in text.lower():
                    destinations.append(destination)


    # -----------------------------------------------------
    # USE USER INTEREST AS BACKUP
    # -----------------------------------------------------

    if not destinations:

        interests = requirements.get(
            "interests",
            []
        )

        interest_text = " ".join(
            interests
        ).lower()

        if "beach" in interest_text:
            destinations = ["Goa", "Kerala"]

        elif "mountain" in interest_text:
            destinations = ["Manali", "Ooty"]

        elif "nature" in interest_text:
            destinations = ["Ooty", "Kerala"]

        elif "history" in interest_text:
            destinations = ["Jaipur", "Hyderabad"]

        elif "food" in interest_text:
            destinations = ["Hyderabad", "Jaipur"]

        elif "adventure" in interest_text:
            destinations = ["Manali", "Goa"]

        elif "nightlife" in interest_text:
            destinations = ["Goa", "Hyderabad"]

        elif "relaxation" in interest_text:
            destinations = ["Kerala", "Ooty"]


    # -----------------------------------------------------
    # FINAL FALLBACK
    # -----------------------------------------------------

    if not destinations:
        destinations = ["Goa"]


    # -----------------------------------------------------
    # REMOVE DUPLICATES
    # -----------------------------------------------------

    destinations = list(
        dict.fromkeys(destinations)
    )


    return {
        "requirements": requirements,
        "recommended_destinations": destinations,
        "research": rag_results
    }