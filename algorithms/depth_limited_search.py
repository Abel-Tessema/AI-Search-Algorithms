def depth_limited_traversal(graph, depth_limit, goal='', start_node='A'):
    traversal_order = []
    found = False

    def dls(node, depth):
        nonlocal found
        if depth > depth_limit or found:
            return
        
        if node not in traversal_order:
            traversal_order.append(node)
            if node == goal:
                found = True
                return
            
            for neighbor in graph[node]:
                dls(neighbor, depth + 1)

    dls(start_node, 0)
    
    if goal:
        return (found, traversal_order)
    return (None, traversal_order)


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


def depth_limited_search(graph, depth_limit, goal=None,):
    if goal == None:
        return depth_limited_traversal(graph, depth_limit)
    else:
        return depth_limited_traversal(graph, depth_limit, goal)

# print(depth_limited_search(graph, 1, "P"))
# # Demonstrate Depth-Limited Search with various limits
# print("Depth Limit 1:", depth_limited_traversal(graph, 1))
# print("Depth Limit 2:", depth_limited_traversal(graph, 2))
# print("Depth Limit 3:", depth_limited_traversal(graph, 3))
