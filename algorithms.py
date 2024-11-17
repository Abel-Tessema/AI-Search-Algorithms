# algorithms.py
from collections import deque
# from termcolor import colored

from utils import print_verbose_graph

def bfs(graph, start_node, search_node='', verbose=False):
    """
    Breadth-First Search (BFS) algorithm.

    Args:
        graph (dict): Graph represented as an adjacency list.
        start_node (str): The starting node for the traversal.
        search_node (str): The node to search for (optional).
        verbose (bool): If True, displays step-by-step traversal details.

    Returns:
        list: Order of traversal or traversal up to the search node.
    """
    visited = set()  # Tracks visited nodes
    queue = deque([start_node])  # Queue for BFS
    steps = []  # Tracks the traversal order

    while queue:
        node = queue.popleft()  # Dequeue the next node
        if node not in visited:
            visited.add(node)    # Mark node as visited
            steps.append(node)   # Add node to traversal list

            # Add unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

            # Verbose output for traversal
            if verbose:
                print_verbose_graph(node)
                print(f"Current Node: {node}")
                print(f"Queue: {list(queue)}")
                print(f"Visited Nodes: {visited}")
                input("\n Press Enter to continue...\n")
            
            # Check if the search node is found
            if node == search_node:
                if verbose:
                    print(f"\nNode '{search_node}' found!\n", 'green')
                return steps

    # If search_node is specified but not found
    if search_node:
        print(f"Node '{search_node}' not found in the graph.")

    return steps


def dfs(graph, start_node, search_node='', direction="left-most", verbose=False):
    """
    Depth-First Search (DFS) algorithm with options for left-most or right-most traversal.

    Args:
        graph (dict): Graph represented as an adjacency list.
        start_node (str): The starting node for the traversal.
        search_node (str): The node to search for (optional).
        direction (str): Direction of traversal, either "left-most" or "right-most".
        verbose (bool): If True, displays step-by-step traversal details.

    Returns:
        list: Order of traversal or traversal up to the search node.
    """
    visited = set()  # Tracks visited nodes
    stack = [start_node]  # Stack for DFS
    steps = []  # Tracks the traversal order

    while stack:
        node = stack.pop()  # Pop the next node
        if node not in visited:
            visited.add(node)  # Mark node as visited
            steps.append(node)  # Add node to traversal list

            # Determine traversal direction and add neighbors
            neighbors = (
                reversed(graph[node]) if direction == 'left-most' else graph[node]
            )
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)

            # Verbose output for traversal
            if verbose:
                print_verbose_graph(node)
                print(f"Current Node: {node}")
                print(f"Stack: {stack}")
                print(f"Visited Nodes: {visited}")
                input("\n Press Enter to continue...\n")

            # Check if the search node is found
            if node == search_node:
                if verbose:
                    print(f"\nNode '{search_node}' found!\n", 'red')
                return steps

    # If search_node is specified but not found
    if search_node:
        print(f"Node '{search_node}' not found in the graph.")

    return steps
