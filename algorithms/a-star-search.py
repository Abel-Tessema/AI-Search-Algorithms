import heapq

def a_star_search(graph, start, goal, heuristic):
    # Priority queue to store (priority, cost, current_node, path)
    open_set = []
    heapq.heappush(open_set, (heuristic[start], 0, start, [start]))

    # Visited dictionary to store the minimum cost to reach each node
    visited = {}

    while open_set:
        # Get the node with the lowest priority (f = g + h)
        _, cost, current_node, path = heapq.heappop(open_set)

        # If we've reached the goal, return the total cost and path
        if current_node == goal:
            return cost, path

        # If we've already visited this node with a lower cost, skip it
        if current_node in visited and visited[current_node] <= cost:
            continue

        # Mark the current node as visited with its cost
        visited[current_node] = cost

        # Explore neighbors
        for neighbor, edge_cost in graph.get(current_node, []):
            new_cost = cost + edge_cost  # g(n): cost from start to this neighbor
            priority = new_cost + heuristic.get(neighbor, float('inf'))  # f(n) = g(n) + h(n)
            heapq.heappush(open_set, (priority, new_cost, neighbor, path + [neighbor]))

    # If no path is found
    return None, []


def main():
    # Example graph (Adjacency list representation)
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 2), ('E', 5)],
        'C': [('F', 1)],
        'D': [('G', 1)],
        'E': [('G', 2)],
        'F': [('G', 3)],
        'G': []
    }

    # Heuristic values for each node
    heuristic = {
        'A': 7,
        'B': 6,
        'C': 4,
        'D': 3,
        'E': 2,
        'F': 6,
        'G': 0
    }

    # Run A* Search
    start = 'A'
    goal = 'G'
    cost, path = a_star_search(graph, start, goal, heuristic)

    if path:
        print(f"Cost: {cost}, Path: {path}")
    else:
        print(f"No path found from {start} to {goal}")

if __name__ == "__main__":
    main()
