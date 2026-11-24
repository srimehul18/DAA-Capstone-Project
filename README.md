# Mini-Courier Planner

## Project Overview

The **Mini-Courier Planner** is a Python-based application developed as part of the Design and Analysis of Algorithms (ETCCDA302) capstone assignment.

The project simulates a courier delivery planning system that prioritizes parcels, selects an optimal set of packages within a given vehicle capacity, calculates shortest paths between delivery locations and generates an approximate delivery route.

It integrates four major algorithmic techniques:

- Merge Sort
- 0/1 Knapsack using Dynamic Programming
- Dijkstra's Shortest Path Algorithm
- Nearest Neighbour TSP Approximation

## Objectives

- Prioritize parcels based on their priority and delivery deadlines.
- Select parcels that maximize total value without exceeding vehicle capacity.
- Calculate shortest paths between the warehouse and delivery locations.
- Generate an approximate delivery route.
- Evaluate the runtime performance of the implemented algorithms using different input sizes.

## Technologies Used

- **Programming Language:** Python
- **Data Storage:** JSON
- **Performance Measurement:** Python `time` and `statistics` modules
- **Data Visualization:** Matplotlib
- **File Handling:** CSV and JSON

## Project Structure

```text
Mini_Courier_Planner/
│
├── datasets/
│   ├── small_dataset.json
│   ├── medium_dataset.json
│   └── large_dataset.json
│
├── results/
│   ├── runtime_chart.png
│   └── runtime_results.csv
│
├── screenshots/
│
├── main.py
├── parcel_manager.py
├── sorting.py
├── knapsack.py
├── graph.py
├── route_planner.py
├── performance.py
├── utils.py
├── README.md
└── requirements.txt
```

## Algorithms Implemented

### 1. Merge Sort

Used to arrange parcels according to priority and delivery deadlines.

- Time Complexity: O(n log n)
- Space Complexity: O(n)

### 2. 0/1 Knapsack using Dynamic Programming

Used to select the most valuable combination of parcels without exceeding the vehicle's weight capacity.

- Time Complexity: O(nW)
- Space Complexity: O(nW)

Here, `n` represents the number of parcels and `W` represents the vehicle capacity.

### 3. Dijkstra's Shortest Path Algorithm

Used to calculate the shortest distance from the warehouse to delivery locations.

- Time Complexity: O((V + E) log V)
- Space Complexity: O(V + E)

The implementation uses an adjacency-list graph representation and a priority queue.

### 4. Nearest Neighbour TSP Approximation

Used to generate an approximate delivery sequence by repeatedly selecting the nearest unvisited destination and finally returning to the warehouse.

The algorithm uses repeated shortest-path calculations to determine the next destination. It does not guarantee the globally optimal route.

## Dataset Information

The project includes three parcel datasets:

| Dataset | Number of Parcels |
|---|---:|
| Small | 5 |
| Medium | 100 |
| Large | 500 |

The integrated courier-planning application currently uses the small dataset for its complete parcel selection and route-planning workflow.

The medium and large datasets are also used for performance testing.

## Installation and Execution

### Prerequisites

- Python 3.x
- Matplotlib

### Install Required Library

Open a terminal in the project directory and execute:

```bash
pip install matplotlib
```

### Run the Main Application

```bash
python main.py
```

The program performs the following operations:

1. Loads and displays parcel information.
2. Sorts parcels using Merge Sort.
3. Selects parcels using the 0/1 Knapsack algorithm.
4. Calculates shortest paths using Dijkstra's algorithm.
5. Generates an approximate delivery route using Nearest Neighbour.
6. Displays the final delivery summary.

### Run Performance Testing

```bash
python performance.py
```

The performance script:

- Generates reproducible parcel data and connected weighted graphs.
- Tests all four algorithms using input sizes of 10, 50, 100, 500 and 1,000.
- Performs five repetitions for each test.
- Records the median execution time.
- Saves the performance results in CSV format.
- Generates a runtime comparison chart.
- Generates medium and large parcel datasets.

## Performance Testing and Analysis

The performance of the four algorithms is evaluated using different input sizes.

The benchmark configuration is:

| Parameter | Value |
|---|---|
| Input Sizes | 10, 50, 100, 500, 1,000 |
| Repetitions | 5 |
| Measurement | Median Runtime |
| Knapsack Capacity | 100 |
| Random Seed | 42 |

Execution time is measured using Python's `time.perf_counter()` function.

The results are stored in:

- `results/runtime_results.csv`
- `results/runtime_chart.png`

### Performance Observations

**Merge Sort:** Execution time increases as the number of parcels grows, consistent with its O(n log n) time complexity.

**0/1 Knapsack:** Execution time increases with the number of parcels because the algorithm evaluates different parcel and capacity combinations using dynamic programming.

**Dijkstra's Algorithm:** Runtime increases with graph size as more vertices and edges need to be processed.

**Nearest Neighbour TSP:** This algorithm requires additional computation because it repeatedly invokes shortest-path calculations while constructing the delivery route.

The measurements are specific to the generated datasets and the system on which the tests were performed.

## Limitations

- The integrated application currently uses the small dataset for its complete planning workflow.
- Medium and large datasets are used for performance benchmarking.
- Graph edge weights are illustrative and do not represent verified real-world road distances.
- Nearest Neighbour is an approximation and may not produce the globally shortest delivery route.
- Execution times may vary depending on hardware and system conditions.

## Future Enhancements

- Add interactive dataset selection to the main application.
- Integrate real-world road distance data.
- Improve route optimization using techniques such as 2-opt.
- Reduce the space complexity of the Knapsack implementation using a one-dimensional DP table.
- Cache previously calculated shortest paths to reduce repeated computations.
- Develop a graphical interface for easier interaction.

## Conclusion

The Mini-Courier Planner demonstrates the practical application of sorting, dynamic programming, greedy graph algorithms and approximation techniques in a courier delivery scenario.

By combining Merge Sort, 0/1 Knapsack, Dijkstra's algorithm and Nearest Neighbour TSP, the application provides a systematic approach to parcel prioritization, packing optimization and delivery route planning.

Performance testing across multiple input sizes provides an opportunity to observe and compare the behaviour of the implemented algorithms.

The project demonstrates how different algorithmic techniques can be integrated to solve a practical optimization problem.
 
### Author:
- Mehul Srivasatava
- 2501730149