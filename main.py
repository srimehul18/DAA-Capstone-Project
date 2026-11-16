from pathlib import Path

from parcel_manager import (
    load_parcels,
    display_parcels,
    get_total_weight
)

from sorting import sort_parcels
from knapsack import knapsack
from graph import create_graph, dijkstra
from route_planner import nearest_neighbour

def main():

    BASE_DIR = Path(__file__).resolve().parent

    dataset_path = BASE_DIR / "datasets" / "small_dataset.json"

    parcels = load_parcels(dataset_path)

    if not parcels:
        print("No parcels available. Exiting.")
        return

    display_parcels(parcels)

    sorted_parcels = sort_parcels(parcels)

    print("\n========== SORTED PARCELS ==========")

    for parcel in sorted_parcels:
        print(
            parcel["parcel_id"],
            "| Recipient:", parcel["name"],
            "| Priority:", parcel["priority"],
            "| Deadline:", parcel["deadline"]
        )
    capacity = 10

    selected, selected_weight, total_value = knapsack(
        sorted_parcels, capacity
    )

    print("\n========== OPTIMAL PACKING PLAN ==========")

    for parcel in selected:
        print(
            parcel["parcel_id"],
            "| Recipient:", parcel["name"],
            "| Destination:", parcel["destination"],
            "| Weight:", parcel["weight"], "kg",
            "| Value:", parcel["value"]
        )

    print("\nVehicle Capacity:", capacity, "kg")
    print("Selected Weight:", selected_weight, "kg")
    print("Total Parcel Value:", total_value)

    if not selected:
        print("No parcels selected for delivery.")
        return

    graph = create_graph()

    print("\n========== SHORTEST PATHS ==========")

    distances, previous = dijkstra(graph, "W")

    for parcel in selected:

        destination = parcel["destination"]

        print(
            "Warehouse to", destination,
            "| Distance:", distances[destination], "km"
        )

    destinations = list(dict.fromkeys(
        parcel["destination"] for parcel in selected
    ))

    route, route_distance, complete_path = nearest_neighbour(
        graph, "W", destinations
    )

    print("\n========== FINAL DELIVERY ROUTE ==========")
    print("Delivery Order:", " -> ".join(route))
    print("Actual Road Path:", " -> ".join(complete_path))
    print("Total Route Distance:", route_distance, "km")
    print("\n========== COURIER PLANNER SUMMARY ==========")

    print("Total Available Parcels:", len(parcels))
    print("Selected Parcels:", len(selected))
    print("Total Original Weight:", get_total_weight(parcels), "kg")
    print("Vehicle Capacity:", capacity, "kg")
    print("Selected Weight:", selected_weight, "kg")
    print("Maximum Selected Value:", total_value)
    print("Final Delivery Distance:", route_distance, "km")


if __name__ == "__main__":
    main()