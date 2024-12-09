import heapq

def uniform_cost_search(graph, start_node, goal_node):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_node, [start_node]))
    visited = set()
    
    while priority_queue:
        current_cost, current_node, current_path = heapq.heappop(priority_queue)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        if current_node == goal_node:
            return current_cost, current_path
        
        for neighbor, cost in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (current_cost + cost, neighbor, current_path + [neighbor]))
    
    return float('inf'), []

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 3)],
    'G': []
}

start = 'A'
goal = 'G'
cost, path = uniform_cost_search(graph, start, goal)
print(f"Cost: {cost}, Path: {path}")
