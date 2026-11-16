
import json
import os


def load_parcels(filename):
    """
    Load parcel details from a JSON dataset.
    """

    if not os.path.exists(filename):
        print("Error: Dataset file not found!")
        return []

    try:
        with open(filename, "r") as file:
            parcels = json.load(file)

        print("Parcel dataset loaded successfully!")
        return parcels

    except (json.JSONDecodeError, OSError) as error:
        print("Error loading dataset:", error)
        return []


def display_parcels(parcels):
    """
    Display details of all parcels.
    """

    print("\n========== PARCEL DETAILS ==========")

    if not parcels:
        print("No parcels available.")
        return

    for parcel in parcels:
        print("-----------------------------------")
        print("Parcel ID:", parcel["parcel_id"])
        print("Destination:", parcel["destination"])
        print("Weight:", parcel["weight"], "kg")
        print("Priority:", parcel["priority"])
        print("Deadline:", parcel["deadline"])
        print("Value:", parcel["value"])

    print("-----------------------------------")
    print("Total parcels:", len(parcels))


def get_total_weight(parcels):
    """
    Calculate the total weight of all parcels.
    """

    total = 0

    for parcel in parcels:
        total += parcel["weight"]

    return total
