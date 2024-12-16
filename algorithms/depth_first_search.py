def depth_first_traversal(graph, goal='', start_node='A'):
    visited = set()
    traversal_order = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            if node == goal:
                return True
            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True
        return False

    found = dfs(start_node)
    if goal:
        return (found, traversal_order)
    return None, traversal_order


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def depth_first_search(graph, goal=None, ):
    if goal == None:
        return depth_first_traversal(graph)
    else:
        return depth_first_traversal(graph, goal)