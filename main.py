import os

os.system('cls')

# main.py
import sys
from algorithms import bfs,dfs
from utils import print_main_menu, print_algorithm_choice, print_back_or_exit, back_or_exit

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
    print_algorithm_choice(algorithm_name=algorithm)
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        if algorithm == 'bfs':
            print("\nVerbose Mode: Showing each step of BFS traversal...\n\n")
            steps = bfs(graph, 'A', verbose=True)
        elif algorithm == 'dfs':
            print("\nVerbose Mode: Showing each step of DFS traversal...\n\n")
            steps = dfs(graph, 'A', verbose=True)
        print(f"Final Traversal Order: {steps}")
    elif choice == '2':
        print("\nStandard Mode: Showing final result only...\n")
        if algorithm == 'bfs':
            steps = bfs(graph, 'A', verbose=False)
        elif algorithm == 'dfs':
            steps = dfs(graph, 'A', verbose=False)
        print(f"Final Traversal Order: {steps}")
    else:
        print("Invalid choice, please try again.")
        algorithm_choice()

    print(print_back_or_exit())
    if not back_or_exit():
        sys.exit()

if __name__ == "__main__":
    main_menu()

# include right most and left most dfs
# searching specific node from the graph with both algs
# make a room for inputed graph **