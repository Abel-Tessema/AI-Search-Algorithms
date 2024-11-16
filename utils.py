# utils.py

def print_verbose_graph(curr_node):
    """
    Prints the current graph structure with the current node marked.

    Args:
        curr_node (str): The current node being visited.
    """
    # Predefined tree structure for visualization
    tree_structure = {
        "A": r"""    
        *A
        / \
       B   C
      / \   \
     D   E   F""",
        "B": r"""     
        A
       / \
     *B   C
     / \   \
    D   E   F""", 
        "C": r"""     
        A
       / \
      B  *C
     / \   \
    D   E   F""", 
        "D": r"""     
        A
       / \
      B   C
     / \   \
   *D   E   F""", 
        "E": r"""    
        A
       / \
      B   C
     / \   \
    D  *E   F""", 
        "F": r"""     
        A
       / \
      B   C
     / \   \
    D   E  *F""", 
    }
    # Ensure the node exists in the structure
    if curr_node in tree_structure:
        print(tree_structure[curr_node])
    else:
        print(f"Node '{curr_node}' not found in the predefined graph structure.")


def print_main_menu():
    """
    Prints the main menu for algorithm selection.
    """
    print("\n--- Algorithm Demonstration ---")
    print("1. BFS (Breadth-First Search)")
    print("2. DFS (Depth-First Search)")
    print("3. Exit")


def print_algorithm_choice(algorithm_name):
    """
    Prints the menu for algorithm-specific options.

    Args:
        algorithm_name (str): Name of the selected algorithm.
    """
    print(f"\n--- {algorithm_name.upper()} Algorithm ---")
    print("1. View verbose steps")
    print("2. View only input/output")


def print_dfs_type():
    """
    Prints the menu for selecting the type of DFS traversal.
    """
    print("\n--- DFS Type Selection ---")
    print("1. Left-most DFS")
    print("2. Right-most DFS")


def print_action_selection():
    """
    Prints the menu for selecting the action (search or demonstrate traversal).
    """
    print("\n--- Action Selection ---")
    print("1. Search for a specific node.")
    print("2. Demonstrate full traversal steps.")


def print_back_or_exit():
    """
    Prints the menu for navigating back to the main menu or exiting.
    """
    print("\n1. Back to Main Menu")
    print("2. Exit")


def back_or_exit():
    """
    Handles user input for navigating back or exiting.

    Returns:
        bool: True if the user chooses to go back, False to exit.
    """
    while True:
        choice = input("Choose an option (1 or 2): ")
        if choice == '1':
            return True  # Back to main menu
        elif choice == '2':
            return False  # Exit the program
        else:
            print("Invalid choice, please try again.")
