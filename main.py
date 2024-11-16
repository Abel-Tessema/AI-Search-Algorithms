# main.py
import os

os.system('cls')

import sys
from algorithms import bfs,dfs
from utils import print_main_menu, print_algorithm_choice, print_back_or_exit, back_or_exit, print_dfs_type, print_action_selection

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
    # ###########################################################################
    print_action_selection()
    action = input("Choose an action (1 or 2): ")
    if action == '1':
        search_node = input("Input the node to be searched: ")

        print_algorithm_choice(algorithm_name=algorithm)
        choice = input("Choose an option (1 or 2): ")

        if choice == '1':
            if algorithm == 'bfs':
                steps = bfs(graph, 'A', search_node, verbose=True)
            elif algorithm == 'dfs':
                steps = dfs_type_choice(True, search_node)
            print(f"Final Traversal Order: {steps}")
        elif choice == '2':
            if algorithm == 'bfs':
                steps = bfs(graph, 'A', search_node,verbose=False)
            elif algorithm == 'dfs':
                steps = dfs_type_choice(False, search_node)
            print("\nStandard Mode: Showing final result only...\n")
            print(f"Final Traversal Order: {steps}")
        else:
            print("Invalid choice, please try again.")
            algorithm_choice(algorithm)
    elif action == 2:
        print_algorithm_choice(algorithm_name=algorithm)
        choice = input("Choose an option (1 or 2): ")

        if choice == '1':
            if algorithm == 'bfs':
                steps = bfs(graph, 'A', verbose=True)
            elif algorithm == 'dfs':
                steps = dfs_type_choice(True)
            print(f"Final Traversal Order: {steps}")
        elif choice == '2':
            if algorithm == 'bfs':
                steps = bfs(graph, 'A', verbose=False)
            elif algorithm == 'dfs':
                steps = dfs_type_choice(False)
            print("\nStandard Mode: Showing final result only...\n")
            print(f"Final Traversal Order: {steps}")
        else:
            print("Invalid choice, please try again.")
            algorithm_choice(algorithm)
    # ###########################################################################
    
    # print_algorithm_choice(algorithm_name=algorithm)
    # choice = input("Choose an option (1 or 2): ")

    # if choice == '1':
    #     if algorithm == 'bfs':
    #         steps = bfs(graph, 'A', verbose=True)
    #     elif algorithm == 'dfs':
    #         steps = dfs_type_choice(True)
    #     print(f"Final Traversal Order: {steps}")
    # elif choice == '2':
    #     if algorithm == 'bfs':
    #         steps = bfs(graph, 'A', verbose=False)
    #     elif algorithm == 'dfs':
    #         steps = dfs_type_choice(False)
    #     print("\nStandard Mode: Showing final result only...\n")
    #     print(f"Final Traversal Order: {steps}")
    # else:
    #     print("Invalid choice, please try again.")
    #     algorithm_choice(algorithm)

    print(print_back_or_exit())
    if not back_or_exit():
        sys.exit()

# dfs type choice
def dfs_type_choice(verbose, search_node=''):
    print_dfs_type()
    dfs_type = input("Choose an option (1 or 2): ")

    if dfs_type == '1':
        return dfs(graph, 'A', search_node, verbose=verbose)
    elif dfs_type == '2': 
        return dfs(graph, 'A', search_node, direction='right-most', verbose=verbose)
    else: 
        print("Invalid choice, Please try again.")
        dfs_type_choice(verbose)

if __name__ == "__main__":
    main_menu()

# include right most and left most dfs  [done]
# searching specific node from the graph with both algs  [done]
# make a room for inputed graph **