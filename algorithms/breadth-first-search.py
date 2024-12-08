from collections import deque

def breadth_first_traversal(graph, start_node):
    visited = set()
    queue = deque([start_node])
    traversal_order = []
    
    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.add(current_node)
            traversal_order.append(current_node)
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return traversal_order

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

print(breadth_first_traversal(graph, 'A'))
