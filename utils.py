# utils.py

def print_main_menu():
    print("\n--- Algorithm Demonstration ---")
    print("1. BFS (Breadth-First Search)")
    print("2. DFS (Depth-First Search)")
    print("3. Exit")

def print_algorithm_choice(algorithm_name):
    print("\n--- {} Algorithm ---".format(algorithm_name))
    print("1. View verbose steps")
    print("2. View only input/output")

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
