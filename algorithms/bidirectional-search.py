
import heapq

def bidirectional_search_with_costs(graph, start_node, goal_node):
    forward_queue = [(0, start_node, [start_node])]  # (cost, current_node, path)
    backward_queue = [(0, goal_node, [goal_node])]
    
    forward_visited = {}
    backward_visited = {}
    
    best_cost = float('inf')
    best_path = None
    
    while forward_queue and backward_queue:
        if forward_queue:
            forward_cost, forward_node, forward_path = heapq.heappop(forward_queue)
            if forward_node in forward_visited and forward_cost > forward_visited[forward_node][0]:
                continue
            forward_visited[forward_node] = (forward_cost, forward_path)
            
            if forward_node in backward_visited:
                total_cost = forward_cost + backward_visited[forward_node][0]
                if total_cost < best_cost:
                    best_cost = total_cost
                    best_path = forward_path + backward_visited[forward_node][1][::-1][1:]
            
            for neighbor, cost in graph.get(forward_node, []):
                if neighbor not in forward_visited or forward_cost + cost < forward_visited[neighbor][0]:
                    heapq.heappush(forward_queue, (forward_cost + cost, neighbor, forward_path + [neighbor]))
        
        if backward_queue:
            backward_cost, backward_node, backward_path = heapq.heappop(backward_queue)
            if backward_node in backward_visited and backward_cost > backward_visited[backward_node][0]:
                continue
            backward_visited[backward_node] = (backward_cost, backward_path)
            
            if backward_node in forward_visited:
                total_cost = backward_cost + forward_visited[backward_node][0]
                if total_cost < best_cost:
                    best_cost = total_cost
                    best_path = forward_visited[backward_node][1] + backward_path[::-1][1:]
            
            for neighbor, cost in graph.get(backward_node, []):
                if neighbor not in backward_visited or backward_cost + cost < backward_visited[neighbor][0]:
                    heapq.heappush(backward_queue, (backward_cost + cost, neighbor, backward_path + [neighbor]))
    
    return best_cost, best_path


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 1)],
    'D': [('B', 2), ('G', 1)],
    'E': [('B', 5), ('G', 2)],
    'F': [('C', 1), ('G', 3)],
    'G': [('D', 1), ('E', 2), ('F', 3)]
}

start = 'A'
goal = 'G'

cost, path = bidirectional_search_with_costs(graph, start, goal)
print(f"Cost: {cost}, Path: {path}")
