# algorithms.py
from collections import deque

# Breadth first search algorithm
def bfs(graph, start_node, verbose=False):
    visited = set()  # Set to track visited nodes
    queue = deque([start_node])  # Initialize queue with start node
    steps = []  # List to store traversal steps

    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            visited.add(node)    # Mark node as visited
            steps.append(node)   # Add to traversal steps
            
            if verbose:
                print(f"Visiting Node: {node}")
                print(f"Queue: {list(queue)}")
                print(f"Visited: {visited}")
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return steps

# Depth first search algorithm
def dfs(graph, start_node, verbose=False):
    visited = set()
    stack = [start_node]
    steps = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            steps.append(node)
            
            if verbose:
                print(f"Visiting Node: {node}")
                print(f"Stack: {stack}")
                print(f"Visited: {visited}")
            
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return steps
