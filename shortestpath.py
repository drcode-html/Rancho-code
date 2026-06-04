neighbours = {
    'A': {'C': 3, 'F': 2},
    'B': {'D': 1, 'E': 2, 'F': 6, 'G': 2},
    'C': {'A': 3, 'D': 4, 'E': 1, 'F': 2},
    'D': {'B': 1, 'C': 4},
    'E': {'B': 2, 'C': 1, 'F': 3},
    'F': {'A': 2, 'B': 6, 'C': 2, 'E': 3, 'G': 5},
    'G': {'B': 2, 'F': 5}
}
def dijkstra(a,b):
    shortestPath = {}
    previousCity = {}
    unexplored = {}

    for city in neighbours:
        shortestPath[city] = float("inf")
        unexplored.append(city)