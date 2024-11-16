# algorithms.py
from collections import deque
from utils import print_verbose_graph

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
                print("\nVerbose Mode: Showing each step of BFS traversal...\n\n")
                print_verbose_graph(node)
                print(f"Visiting Node: {node}")
                print(f"Queue: {list(queue)}")
                print(f"Visited: {visited}")
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return steps

# Depth first search algorithm
def dfs(graph, start_node, direction="left-most",verbose=False):
    visited = set()
    stack = [start_node]
    steps = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            steps.append(node)
            
            if verbose:
                print("\nVerbose Mode: Showing each step of DFS traversal...\n\n")
                print_verbose_graph(node)
                print(f"Visiting Node: {node}")
                print(f"Stack: {stack}")
                print(f"Visited: {visited}\n")

            if direction == 'left-most':
                for neighbor in reversed(graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)
            else: 
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)


    return steps
