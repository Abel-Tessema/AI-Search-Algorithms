def depth_first_traversal(graph, start_node='A'):
    visited = set()
    traversal_order = []
    
    def dfs(node):
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            for neighbor in graph[node]:
                dfs(neighbor)
    
    dfs(start_node)
    return traversal_order

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print(depth_first_traversal(graph, 'A'))

