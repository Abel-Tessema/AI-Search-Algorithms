from collections import deque

def breadth_first_traversal(graph, goal='', start_node='A'):
    visited = set()
    queue = deque([start_node])
    traversal_order = []
    
    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.add(current_node)
            traversal_order.append(current_node)
            if goal == current_node:
                return (True, traversal_order)
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    if goal:
        return (False, traversal_order)
    
    return (None,traversal_order)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def breadth_first_search(graph, goal=None, ):
    if goal == None:
        return breadth_first_traversal(graph)
    else:
        return breadth_first_traversal(graph, goal)
