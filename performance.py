
import csv
import random
import time
import statistics
import json

from pathlib import Path
import matplotlib.pyplot as plt

from sorting import sort_parcels
from knapsack import knapsack
from graph import dijkstra
from route_planner import nearest_neighbour


# Project directories
BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "datasets"
RESULTS_DIR = BASE_DIR / "results"

RESULTS_DIR.mkdir(exist_ok=True)

random.seed(42)


def generate_parcels(n):

    parcels = []

    for i in range(n):
        parcel = {
            "parcel_id": f"P{i + 1}",
            "destination": random.choice(["A", "B", "C", "D", "E"]),
            "weight": random.randint(1, 10),
            "priority": random.randint(1, 3),
            "deadline": random.randint(1, 100),
            "value": random.randint(10, 100)
        }

        parcels.append(parcel)

    return parcels



def generate_graph(n):
    nodes = ["W"] + [f"N{i}" for i in range(1, n)]

    graph = {node: {} for node in nodes}

    for i in range(len(nodes) - 1):
        weight = random.randint(1, 20)

        graph[nodes[i]][nodes[i + 1]] = weight
        graph[nodes[i + 1]][nodes[i]] = weight

    for i in range(len(nodes)):
        for j in range(i + 2, len(nodes)):
            if random.random() < 0.3:
                weight = random.randint(1, 20)

                graph[nodes[i]][nodes[j]] = weight
                graph[nodes[j]][nodes[i]] = weight

    return graph

def measure_time(function, repeats=3):
    """
    Measure execution time and return median runtime.
    """

    times = []

    for _ in range(repeats):

        start = time.perf_counter()
        function()
        end = time.perf_counter()

        times.append(end - start)

    return statistics.median(times)


def save_test_datasets():
    """
    Generate and save medium and large parcel datasets.
    """

    datasets = {
        "medium_dataset.json": 100,
        "large_dataset.json": 500
    }

    for filename, size in datasets.items():

        parcels = generate_parcels(size)

        filepath = DATASET_DIR / filename

        with open(filepath, "w") as file:
            json.dump(parcels, file, indent=4)

        print(f"Generated {filename}: {size} parcels")


def run_performance_tests():

    results = []


    print("\nTesting Sorting and Knapsack...")

    parcel_sizes = [5, 100, 500]

    for size in parcel_sizes:

        parcels = generate_parcels(size)

        sorting_time = measure_time(
            lambda: sort_parcels(parcels.copy())
        )

        knapsack_time = measure_time(
            lambda: knapsack(parcels, 100)
        )

        results.append({
            "Algorithm": "Merge Sort",
            "Input Size": size,
            "Runtime (seconds)": sorting_time
        })

        results.append({
            "Algorithm": "0/1 Knapsack",
            "Input Size": size,
            "Runtime (seconds)": knapsack_time
        })


    print("Testing Dijkstra...")

    graph_sizes = [6, 20, 50]

    for size in graph_sizes:

        graph = generate_graph(size)

        dijkstra_time = measure_time(
            lambda: dijkstra(graph, "W")
        )

        results.append({
            "Algorithm": "Dijkstra",
            "Input Size": size,
            "Runtime (seconds)": dijkstra_time
        })



    print("Testing Nearest Neighbour TSP...")

    tsp_sizes = [5, 10, 15]

    for size in tsp_sizes:

        graph = generate_graph(size + 1)

        destinations = [
            f"N{i}" for i in range(1, size + 1)
        ]

        tsp_time = measure_time(
            lambda: nearest_neighbour(
                graph, "W", destinations
            )
        )

        results.append({
            "Algorithm": "Nearest Neighbour TSP",
            "Input Size": size,
            "Runtime (seconds)": tsp_time
        })

    return results


def save_results(results):
    """
    Save performance results in CSV format.
    """

    filepath = RESULTS_DIR / "runtime_results.csv"

    with open(filepath, "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Algorithm",
                "Input Size",
                "Runtime (seconds)"
            ]
        )

        writer.writeheader()
        writer.writerows(results)

    print("\nRuntime results saved to:", filepath)


def generate_runtime_chart(results):
    """
    Generate runtime comparison chart.
    """

    algorithms = list(dict.fromkeys(
        result["Algorithm"] for result in results
    ))

    plt.figure(figsize=(10, 6))

    for algorithm in algorithms:

        data = [
            result for result in results
            if result["Algorithm"] == algorithm
        ]

        sizes = [item["Input Size"] for item in data]
        runtimes = [
            item["Runtime (seconds)"] for item in data
        ]

        plt.plot(
            sizes,
            runtimes,
            marker="o",
            label=algorithm
        )

    plt.xlabel("Input Size (parcels or vertices)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Algorithm Runtime Comparison")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    chart_path = RESULTS_DIR / "runtime_chart.png"

    plt.savefig(chart_path, dpi=300)
    plt.close()

    print("Runtime chart saved to:", chart_path)


def main():

    print("========== PERFORMANCE TESTING ==========")

    # Generate datasets
    save_test_datasets()

    # Execute benchmarks
    results = run_performance_tests()

    # Save results
    save_results(results)

    # Generate chart
    generate_runtime_chart(results)

    print("\n========== PERFORMANCE TESTING COMPLETED ==========")


if __name__ == "__main__":
    main()
