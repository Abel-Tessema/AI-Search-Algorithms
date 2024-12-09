def depth_limited_search(graph, start_node, depth_limit):
    traversal_order = []
    
    def dls(node, depth):
        if depth > depth_limit:
            return
        if node not in traversal_order:
            traversal_order.append(node)
            for neighbor in graph[node]:
                dls(neighbor, depth + 1)
    
    dls(start_node, 0)
    return traversal_order

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F', 'G'],
    'C': ['H', 'I'],
    'D': ['J'],
    'E': ['K', 'L'],
    'F': [],
    'G': ['M'],
    'H': [],
    'I': ['N', 'O'],
    'J': ['P'],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': [],
    'P': []
}

# Demonstrate Depth-Limited Search with various limits
print("Depth Limit 1:", depth_limited_search(graph, 'A', 1))
print("Depth Limit 2:", depth_limited_search(graph, 'A', 2))
print("Depth Limit 3:", depth_limited_search(graph, 'A', 3))
