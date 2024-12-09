def depth_first_traversal(graph, start_node):
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
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

print(depth_first_traversal(graph, 'A'))

