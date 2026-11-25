from graph import dijkstra, reconstruct_path
def nearest_neighbour(graph, start, destinations):
    unvisited = list(dict.fromkeys(
    node for node in destinations if node != start
))

    current = start
    route = [start]
    total_distance = 0

    complete_path = [start]

    while unvisited:

        distances, previous = dijkstra(graph, current)

        nearest = min(
            unvisited,
            key=lambda node: distances[node]
        )

        total_distance += distances[nearest]

        path = reconstruct_path(
            previous, current, nearest
        )

        complete_path.extend(path[1:])

        current = nearest
        route.append(current)
        unvisited.remove(current)

    if current != start:
        distances, previous = dijkstra(graph, current)
        total_distance += distances[start]
        return_path = reconstruct_path(
            previous, current, start
        )

        complete_path.extend(return_path[1:])
        route.append(start)

    return route, total_distance, complete_path

def calculate_route_distance(graph, route):
    """
    Calculate total distance of a given route
    using Dijkstra's shortest paths.
    """
    total_distance = 0

    for i in range(len(route) - 1):
        distances, _ = dijkstra(graph, route[i])
        total_distance += distances[route[i + 1]]

    return total_distance