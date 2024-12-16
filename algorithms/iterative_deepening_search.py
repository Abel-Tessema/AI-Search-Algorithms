def iterative_deepening_traversal(graph, goal_node, max_depth, start_node="A"):
    def dls(node, depth):
        if depth == 0:
            return node == goal_node
        if depth > 0:
            for neighbor in graph.get(node, []):
                if dls(neighbor, depth - 1):
                    path.append(neighbor)
                    return True
        return False

    for depth in range(max_depth + 1):
        path = []
        if dls(start_node, depth):
            path.append(start_node)
            return (True, path[::-1])
    return (False, [])

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H'],
    'E': [],
    'F': ['I', 'J'],
    'G': ['K'],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}

start = 'A'
goal = 'K'
max_depth = 5

def iterative_deepening_search(graph, goal, max_depth):
    if goal == None:
        return iterative_deepening_traversal(graph, goal,  max_depth)
    else:
        return iterative_deepening_traversal(graph, goal, max_depth)
