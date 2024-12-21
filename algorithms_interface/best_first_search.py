import heapq

def best_first_traversal(graph, heuristic, goal, start='A'):
    open_set = []
    heapq.heappush(open_set, (heuristic[start], start, [start]))

    visited = set()

    while open_set:
        _, current_node, path = heapq.heappop(open_set)

        if current_node == goal:
            return (True, path, visited)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, _ in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(open_set, (heuristic.get(neighbor, float('inf')), neighbor, path + [neighbor]))

    return (False, None, visited)

def best_first_search(graph, heuristic, goal):
    return best_first_traversal(graph, heuristic, goal)
