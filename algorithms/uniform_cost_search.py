import heapq

def uniform_cost_traversal(graph, goal_node, start_node='A'):
    if not goal_node:
        return (False, float('inf'), [])
    
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_node, [start_node]))
    visited = set()
    
    while priority_queue:
        current_cost, current_node, current_path = heapq.heappop(priority_queue)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        if current_node == goal_node:
            return (True, current_cost, current_path)
        
        for neighbor, cost in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (current_cost + cost, neighbor, current_path + [neighbor]))
    
    return (False, float('inf'), [])


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 3)],
    'G': []
}

def uniform_cost_search(graph, goal):
    return uniform_cost_traversal(graph, goal)
