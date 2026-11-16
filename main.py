from pathlib import Path

from sorting import sort_parcels

from parcel_manager import (
    load_parcels,
    display_parcels,
    get_total_weight
)

def main():

    BASE_DIR = Path(__file__).resolve().parent
    dataset_path = BASE_DIR / "datasets" / "small_dataset.json"
    parcels = load_parcels(dataset_path)
    display_parcels(parcels)
    sorted_parcels = sort_parcels(parcels)

    print("\n========== SORTED PARCELS ==========")
    for parcel in sorted_parcels:
        print(
            parcel["parcel_id"],
            "| Priority:", parcel["priority"],
            "| Deadline:", parcel["deadline"]
        )

    total_weight = get_total_weight(parcels)

    print("\n========== SUMMARY ==========")
    print("Total Parcel Weight:", total_weight, "kg")


if __name__ == "__main__":
    main()