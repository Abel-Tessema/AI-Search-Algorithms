# main.py
import os
import sys
from algorithms import bfs, dfs
from utils import print_main_menu, print_algorithm_choice, print_back_or_exit, back_or_exit, print_dfs_type, print_action_selection

os.system("cls")

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

def main_menu():
    """
    Display the main menu and handle user input to choose an algorithm or exit.
    """
    while True:
        print_main_menu()
        choice = input("Choose an algorithm (1 or 2): ")

        if choice == '1':
            algorithm_choice(algorithm='bfs')
        elif choice == '2':
            algorithm_choice(algorithm='dfs')
        elif choice == '3':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

def algorithm_choice(algorithm):
    """
    Handle algorithm-specific actions, including verbose traversal or searching for a specific node.
    """
    print_action_selection()
    action = input("Choose an action (1 or 2): ")

    # Search for a specific node in the graph
    if action == '1':
        search_node = input("Input the node to be searched: ").strip()
        if search_node not in graph:
            print(f"Node '{search_node}' does not exist in the graph. Please try again.")
            return

        process_algorithm(algorithm, search_node=search_node)
    
    # Traverse the graph without searching for a node
    elif action == '2':
        process_algorithm(algorithm)
    else:
        print("Invalid choice, please try again.")
        algorithm_choice(algorithm)

    # Back or Exit after completion
    print(print_back_or_exit())
    if not back_or_exit():
        sys.exit()

def process_algorithm(algorithm, search_node=''):
    """
    Process the selected algorithm in either verbose or standard mode.
    """
    print_algorithm_choice(algorithm_name=algorithm)
    choice = input("Choose an option (1 or 2): ")

    verbose = choice == '1'
    if algorithm == 'bfs':
        steps = bfs(graph, 'A', search_node, verbose=verbose)
    elif algorithm == 'dfs':
        steps = dfs_type_choice(verbose, search_node)

    if verbose:
        print(f"Final Traversal Steps: {steps}")
    else:
        print("\nStandard Mode: Showing final result only...\n")
        print(f"Final Traversal Steps: {steps}")

def dfs_type_choice(verbose, search_node=''):
    """
    Allow the user to choose the type of DFS (left-most or right-most).
    """
    print_dfs_type()
    dfs_type = input("Choose an option (1 or 2): ")

    if dfs_type == '1':  # Left-most DFS
        return dfs(graph, 'A', search_node, verbose=verbose)
    elif dfs_type == '2':  # Right-most DFS
        return dfs(graph, 'A', search_node, direction='right-most', verbose=verbose)
    else:
        print("Invalid choice, please try again.")
        return dfs_type_choice(verbose, search_node)

if __name__ == "__main__":
    main_menu()
