import heapq

def a_star_traversal(graph, heuristic, goal, start="A"):
    open_set = []
    heapq.heappush(open_set, (heuristic[start], 0, start, [start]))

    visited = {}

    while open_set:
        _, cost, current_node, path = heapq.heappop(open_set)

        if current_node == goal:
            return (True, cost, path)

        if current_node in visited and visited[current_node] <= cost:
            continue

        visited[current_node] = cost

        for neighbor, edge_cost in graph.get(current_node, []):
            new_cost = cost + edge_cost  
            priority = new_cost + heuristic.get(neighbor, float('inf'))  
            heapq.heappush(open_set, (priority, new_cost, neighbor, path + [neighbor]))

    return (False, None, [])

def a_star_search(graph, heuristic, goal):
    return a_star_traversal(graph, heuristic, goal)
