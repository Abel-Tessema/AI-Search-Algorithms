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

def depth_limited_search(graph, depth_limit, goal=None,):
    if goal == None:
        return depth_limited_traversal(graph, depth_limit)
    else:
        return depth_limited_traversal(graph, depth_limit, goal)
