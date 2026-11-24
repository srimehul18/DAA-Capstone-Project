
import csv
import random
import time
import statistics
import json
import shutil

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

DATASET_DIR.mkdir(exist_ok=True)
RESULTS_DIR.mkdir(exist_ok=True)


# Benchmark configuration
SIZES = [10, 50, 100, 500, 1000]
REPEATS = 5
SEED = 42
KNAPSACK_CAPACITY = 100


# Chart colours
COLORS = {
    "Merge Sort": "#3b82f6",
    "0/1 Knapsack": "#ff7043",
    "Dijkstra": "#10b981",
    "Nearest Neighbour TSP": "#f59e0b"
}


def generate_parcels(n, rng):
    """Generate reproducible parcel data."""

    parcels = []

    for i in range(n):
        parcels.append({
            "parcel_id": f"P{i + 1}",
            "destination": f"N{rng.randint(1, n)}",
            "weight": rng.randint(1, 10),
            "priority": rng.randint(1, 3),
            "deadline": rng.randint(1, 100),
            "value": rng.randint(10, 100)
        })

    return parcels


def generate_graph(n, rng):
    """
    Generate a connected, sparse, undirected graph.

    W represents the warehouse.
    N1...Nn represent delivery nodes.
    Edge weights are illustrative.
    """

    nodes = ["W"] + [f"N{i}" for i in range(1, n + 1)]

    graph = {node: {} for node in nodes}

    # Connect consecutive nodes to guarantee connectivity
    for i in range(len(nodes) - 1):
        weight = rng.randint(1, 20)

        graph[nodes[i]][nodes[i + 1]] = weight
        graph[nodes[i + 1]][nodes[i]] = weight

    # Add additional sparse connections
    for i in range(len(nodes)):
        for j in range(i + 2, len(nodes)):
            if rng.random() < 0.003:
                weight = rng.randint(1, 20)

                graph[nodes[i]][nodes[j]] = weight
                graph[nodes[j]][nodes[i]] = weight

    return graph


def measure_time(function, repeats=REPEATS):
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




def run_performance_tests():

    results = []

    print("\n========== PERFORMANCE TESTING ==========")
    print("Input sizes:", SIZES)
    print("Repetitions:", REPEATS)
    print("Random seed:", SEED)

    for size in SIZES:

        print(f"\nTesting input size: {size}")

        rng = random.Random(SEED + size)

        # Generate inputs
        parcels = generate_parcels(size, rng)
        graph = generate_graph(size, rng)

        destinations = [
            f"N{i}" for i in range(1, size + 1)
        ]

        # 1. Merge Sort
        sorting_time = measure_time(
            lambda p=parcels: sort_parcels(p.copy())
        )

        results.append({
            "Algorithm": "Merge Sort",
            "Input Size": size,
            "Runtime (seconds)": sorting_time
        })

        # 2. 0/1 Knapsack
        knapsack_time = measure_time(
            lambda p=parcels: knapsack(p, KNAPSACK_CAPACITY)
        )

        results.append({
            "Algorithm": "0/1 Knapsack",
            "Input Size": size,
            "Runtime (seconds)": knapsack_time
        })

        # 3. Dijkstra
        dijkstra_time = measure_time(
            lambda g=graph: dijkstra(g, "W")
        )

        results.append({
            "Algorithm": "Dijkstra",
            "Input Size": size,
            "Runtime (seconds)": dijkstra_time
        })

        # 4. Nearest Neighbour TSP
        tsp_time = measure_time(
            lambda g=graph, d=destinations: nearest_neighbour(
                g, "W", d
            )
        )

        results.append({
            "Algorithm": "Nearest Neighbour TSP",
            "Input Size": size,
            "Runtime (seconds)": tsp_time
        })

        print("All four algorithms tested.")

    return results


def save_results(results):
    """
    Save performance results in CSV format.
    """

    filepath = RESULTS_DIR / "runtime_results.csv"

    with open(filepath, "w", newline="", encoding="utf-8") as file:

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
    Generate a log-log runtime comparison chart.
    """

    algorithms = list(COLORS.keys())

    # Preserve the previous chart before replacing it
    chart_path = RESULTS_DIR / "runtime_chart.png"

    if chart_path.exists():
        backup_path = RESULTS_DIR / "runtime_chart_previous.png"

        shutil.copy2(chart_path, backup_path)

        print("Previous chart backed up to:", backup_path)

    plt.figure(figsize=(12, 7))

    for algorithm in algorithms:

        data = [
            item for item in results
            if item["Algorithm"] == algorithm
        ]

        sizes = [item["Input Size"] for item in data]

        runtimes = [
            item["Runtime (seconds)"] * 1000
            for item in data
        ]

        plt.loglog(
            sizes,
            runtimes,
            marker="o",
            linewidth=2,
            markersize=6,
            color=COLORS[algorithm],
            label=algorithm
        )

    plt.xlabel("Input Size (parcels, vertices or destinations)")
    plt.ylabel("Execution Time (milliseconds)")
    plt.title("Algorithm Runtime Comparison")

    plt.grid(
        True,
        which="both",
        linestyle="--",
        alpha=0.3
    )

    plt.legend()
    plt.tight_layout()

    plt.savefig(chart_path, dpi=300)
    plt.close()

    print("Runtime chart saved to:", chart_path)


def main():

    print("\n========== PERFORMANCE TESTING ==========")

    print("Using generated benchmark inputs.")
    print("Existing parcel datasets will not be modified.")

    # Execute benchmarks
    results = run_performance_tests()

    # Save CSV results
    save_results(results)

    # Generate comparison chart
    generate_runtime_chart(results)

    print("\n========== PERFORMANCE TESTING COMPLETED ==========")


if __name__ == "__main__":
    main()