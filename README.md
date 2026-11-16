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