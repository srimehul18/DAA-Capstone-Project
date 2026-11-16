import heapq
def create_graph():
    """
    Create an undirected weighted graph using an adjacency list.
    """

    graph = {
        "W": [("A", 4), ("B", 2)],
        "A": [("W", 4), ("B", 1), ("C", 5)],
        "B": [("W", 2), ("A", 1), ("C", 8), ("D", 7)],
        "C": [("A", 5), ("B", 8), ("D", 2), ("E", 6)],
        "D": [("B", 7), ("C", 2), ("E", 3)],
        "E": [("C", 6), ("D", 3)]
    }

    return graph

def dijkstra(graph, source):
    """
    Find shortest distances from source to all other vertices.
    """

    distances = {node: float("inf") for node in graph}
    distances[source] = 0

    previous = {node: None for node in graph}

    pq = [(0, source)]

    while pq:

        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbour, weight in graph[current_node]:

            new_distance = current_distance + weight

            if new_distance < distances[neighbour]:

                distances[neighbour] = new_distance
                previous[neighbour] = current_node

                heapq.heappush(
                    pq, (new_distance, neighbour)
                )

    return distances, previous


def reconstruct_path(previous, source, destination):
    """
    Reconstruct the shortest path using previous nodes.
    """

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if not path or path[0] != source:
        return []

    return path