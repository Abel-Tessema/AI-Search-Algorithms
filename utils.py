# utils.py

def print_verbose_graph(curr_node):
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
    print(tree_structure[curr_node])

def print_main_menu():
    print("\n--- Algorithm Demonstration ---")
    print("1. BFS (Breadth-First Search)")
    print("2. DFS (Depth-First Search)")
    print("3. Exit")

def print_algorithm_choice(algorithm_name):
    print("\n--- {} Algorithm ---".format(algorithm_name))
    print("1. View verbose steps")
    print("2. View only input/output")

def print_dfs_type():
    print("\n--- DFS type --- \n")
    print("1. Left-most dfs")
    print("2. Right-most dfs")

def print_back_or_exit():
    print("\n1. Back to main menu")
    print("2. Exit")

def back_or_exit():
    choice = input("Choose an option (1 or 2): ")
    if choice == '1':
        return True
    elif choice == '2':
        return False
    else:
        print("Invalid choice, please try again.")
        return back_or_exit()
