## Algorithm Complexity Analysis

The Mini-Courier Planner uses four major algorithms to optimize parcel selection and delivery routing.

### 1. Merge Sort

- **Purpose:** Sorts parcels according to priority and delivery deadline.
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)

Merge Sort divides the parcel list into smaller sublists, sorts them recursively and merges them into a sorted list. Its time complexity remains O(n log n) across best, average and worst cases.

### 2. 0/1 Knapsack using Dynamic Programming

- **Purpose:** Selects the parcels that maximize total value without exceeding vehicle weight capacity.
- **Time Complexity:** O(nW)
- **Space Complexity:** O(nW)

The algorithm uses a two-dimensional DP table to compare including and excluding each parcel at different capacity limits. It guarantees an optimal selection for the given integer weights and capacity.

### 3. Dijkstra's Shortest Path Algorithm

- **Purpose:** Finds the shortest distance from the warehouse or a current delivery point to other locations.
- **Time Complexity:** O((V + E) log V)
- **Space Complexity:** O(V + E)

The implementation uses an adjacency-list graph representation and a priority queue implemented using Python's heapq module. It repeatedly selects the vertex with the smallest known distance and relaxes its neighbouring edges.

### 4. Nearest Neighbour TSP Approximation

- **Purpose:** Determines an approximate delivery order by repeatedly selecting the nearest unvisited destination and finally returning to the warehouse.
- **Time Complexity:** O(k(V + E) log V + k²)
- **Space Complexity:** O(V + E + k)

The implementation uses Dijkstra's algorithm to calculate shortest paths between delivery points. It then selects the nearest unvisited destination at each step. This is an approximation technique and does not guarantee the globally optimal travelling-salesperson route.

### Overall Analysis

Merge Sort efficiently prioritizes parcels, while Dynamic Programming ensures optimal parcel selection within the vehicle capacity. Dijkstra determines shortest paths between locations, and Nearest Neighbour provides a practical approximate delivery sequence.

The execution time of the algorithms increases as the input size grows, with the rate of growth depending on their respective time complexities.

## Performance Testing and Analysis

### Testing Environment

The Mini-Courier Planner was tested using different input sizes to observe the execution time of its major algorithms.

The following test sizes were used:

| Algorithm | Input Sizes |
|---|---|
| Merge Sort | 5, 100, 500 parcels |
| 0/1 Knapsack | 5, 100, 500 parcels |
| Dijkstra | 6, 20, 50 vertices |
| Nearest Neighbour TSP | 5, 10, 15 delivery destinations |

The performance tests used generated datasets and weighted graphs. The Knapsack capacity was kept fixed during testing so that the effect of increasing the number of parcels could be observed.

### Performance Observations

**1. Merge Sort**

The execution time increased as the number of parcels increased. This behaviour is consistent with its O(n log n) time complexity. Merge Sort provides efficient sorting even when the input dataset becomes larger.

**2. 0/1 Knapsack**

The execution time increased with the number of parcels. The algorithm uses a two-dimensional dynamic programming table, and its performance depends on both the number of parcels and the vehicle capacity. Its time complexity is O(nW).

**3. Dijkstra's Algorithm**

The execution time increased as the number of graph vertices increased. The algorithm uses an adjacency list and a priority queue to calculate shortest paths efficiently.

**4. Nearest Neighbour TSP**

The execution time increased as the number of delivery destinations increased. The implementation repeatedly calculates shortest paths using Dijkstra's algorithm before selecting the next nearest unvisited destination.

### Comparative Analysis

Merge Sort showed relatively efficient growth with increasing parcel counts. The Knapsack algorithm required more computation because it evaluates different parcel and capacity combinations using dynamic programming.

Dijkstra's algorithm handled the tested graph sizes efficiently. Nearest Neighbour TSP required additional computations because it repeatedly invokes shortest-path calculations while constructing the delivery route.

The observations demonstrate that algorithm selection and input size have a significant effect on execution time.

### Limitations of Performance Testing

- The datasets and graphs are synthetically generated.
- Graph edge weights are illustrative and do not represent verified real-world road distances.
- Execution times may vary depending on system specifications and background processes.
- The Nearest Neighbour approach is an approximation and does not guarantee the globally optimal delivery route.

The performance results are therefore used to compare the implemented algorithms under the selected test conditions rather than to establish universal execution-time benchmarks.

## Optimization Opportunities and Future Improvements

The current Mini-Courier Planner provides a working implementation of sorting, dynamic programming and graph-based routing. The following improvements could further enhance its efficiency:

1. **Merge Sort:** The existing implementation already provides O(n log n) time complexity. Further improvements could focus on reducing temporary memory allocation during merging.

2. **0/1 Knapsack:** The current two-dimensional DP table requires O(nW) space. A one-dimensional DP implementation could reduce auxiliary space to O(W), provided capacities are processed in descending order.

3. **Dijkstra's Algorithm:** The use of an adjacency list and priority queue is suitable for sparse graphs. Reusing previously calculated shortest-path results could avoid redundant computations when multiple route-planning requests use the same graph.

4. **Nearest Neighbour TSP:** The route can potentially be improved using local-search techniques such as 2-opt, which attempts to reduce route length by exchanging pairs of route edges.

These improvements are proposed as future enhancements and are not claimed as implemented features of the current version.

