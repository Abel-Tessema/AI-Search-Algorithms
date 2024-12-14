import heapq

def best_first_search(graph, start, goal, heuristic):
    # Priority queue for frontier nodes (priority, current_node, path)
    open_set = []
    heapq.heappush(open_set, (heuristic[start], start, [start]))

    # Visited set to avoid re-exploring nodes
    visited = set()

    while open_set:
        # Get the node with the lowest heuristic value
        _, current_node, path = heapq.heappop(open_set)

        # If the goal is reached, return the path and visited nodes
        if current_node == goal:
            return path, visited

        # Skip if already visited
        if current_node in visited:
            continue

        # Mark the current node as visited
        visited.add(current_node)

        # Expand neighbors
        for neighbor, _ in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(open_set, (heuristic.get(neighbor, float('inf')), neighbor, path + [neighbor]))

    # If no path is found
    return None, visited

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

    # Run Best-First Search
    start = 'A'
    goal = 'G'
    path, visited_nodes = best_first_search(graph, start, goal, heuristic)

    if path:
        print(f"Path: {path}")
        print(f"Visited Nodes: {visited_nodes}")
    else:
        print(f"No path found from {start} to {goal}")

if __name__ == "__main__":
    main()
