import heapq


def create_graph():
    graph = {
        "W": {
            "Dwarka": 4,
            "Uttam Nagar": 2
        },

        "Dwarka": {
            "W": 4,
            "Uttam Nagar": 1,
            "Rohini": 5
        },

        "Uttam Nagar": {
            "W": 2,
            "Dwarka": 1,
            "Rohini": 8,
            "Hauz Khas": 7
        },

        "Rohini": {
            "Dwarka": 5,
            "Uttam Nagar": 8,
            "Hauz Khas": 2,
            "Arjan Garh": 6
        },

        "Hauz Khas": {
            "Uttam Nagar": 7,
            "Rohini": 2,
            "Arjan Garh": 3
        },

        "Arjan Garh": {
            "Rohini": 6,
            "Hauz Khas": 3
        }
    }

    return graph


def dijkstra(graph, source):
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}

    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbour, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbour]:
                distances[neighbour] = distance
                previous[neighbour] = current_node

                heapq.heappush(
                    priority_queue,
                    (distance, neighbour)
                )

    return distances, previous


def reconstruct_path(previous, source, destination):
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if path[0] != source:
        return []

    return path