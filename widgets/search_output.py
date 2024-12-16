import customtkinter as ctk

from utils.graphs import (
    bidirectional_search_graph_1, 
    bfs_and_dfs_search_graph, 
    depth_limited_search_graph, 
    iddfs_graph, 
    uniform_cost_search_graph,
    informed_detail,
)
from algorithms.breadth_first_search import breadth_first_search
from algorithms.depth_first_search import depth_first_search
from algorithms.depth_limited_search import depth_limited_traversal
from algorithms.iterative_deepening_search import iterative_deepening_search
from algorithms.uniform_cost_search import uniform_cost_search
from algorithms.bidirectional_search import bidirectional_search_with_costs
from algorithms.a_star_search import a_star_search
from algorithms.best_first_search import best_first_search


class search_output(ctk.CTkFrame):
    def __init__(self, master, algorithm="BFS"):
        super().__init__(master)
        self.algorithm = algorithm
        self.columnconfigure(1, weight=1)

        # Input Widgets
        self.label_goal = ctk.CTkLabel(self, text="Goal Node: ", text_color="white")
        self.goal_node_input = ctk.CTkEntry(self, placeholder_text="Enter goal node")

        self.label_depth = ctk.CTkLabel(self, text="Depth: ", text_color="white")
        self.depth_input = ctk.CTkEntry(self, placeholder_text="Enter depth limit")

        self.search_button = ctk.CTkButton(self, text="Search", command=self.submit_action)

        self.result_label_1 = ctk.CTkLabel(self, text="Search a node...")
        self.result_label_2 = ctk.CTkLabel(self, text="Search result...")

        self.layout_widgets()  # Initial layout

    def layout_widgets(self):
        self.clear_grid()
        if self.algorithm in ["BFS", "DFS", "Best-First Search", "A* Search"]:
            self.add_widget(self.label_goal, 0, 0)
            self.add_widget(self.goal_node_input, 0, 1)
            self.add_widget(self.search_button, 2, 0, 2)
        elif self.algorithm == "DLS":
            self.add_widget(self.label_goal, 0, 0)
            self.add_widget(self.goal_node_input, 0, 1)
            self.add_widget(self.label_depth, 1, 0)
            self.add_widget(self.depth_input, 1, 1)
            self.add_widget(self.search_button, 2, 0, 2)
        elif self.algorithm in ["UCS", "Bidirectional Search"]:
            self.add_widget(self.label_goal, 0, 0)
            self.add_widget(self.goal_node_input, 0, 1)
            self.add_widget(self.search_button, 2, 0, 2)
        elif self.algorithm == "IDDFS":
            self.add_widget(self.label_goal, 0, 0)
            self.add_widget(self.goal_node_input, 0, 1)
            self.add_widget(self.label_depth, 1, 0)
            self.add_widget(self.depth_input, 1, 1)
            self.add_widget(self.search_button, 2, 0, 2)

        self.add_widget(self.result_label_1, 3, 0, 2)

    def add_widget(self, widget, row, col, colspan=1):
        widget.grid(row=row, column=col, columnspan=colspan, sticky="ew", padx=5, pady=5)

    def clear_grid(self):
        for widget in self.winfo_children():
            widget.grid_forget()

    def update_algorithm(self, algorithm):
        if algorithm != self.algorithm:
            self.algorithm = algorithm
            self.goal_node_input.delete(0, ctk.END)
            self.goal_node_input.configure(placeholder_text="Enter goal node")
            self.depth_input.delete(0, ctk.END)
            self.depth_input.configure(placeholder_text="Enter depth limit")
            self.result_label_1.configure(text="Search a node...")
            self.layout_widgets()

    def submit_action(self):
        user_input = self.goal_node_input.get().capitalize()
        depth_limit = int(self.depth_input.get() or 1)

        path = self.get_path(user_input, depth_limit)

        if self.algorithm in ["DFS", "BFS"]:
            if path[0] == None:
                self.result_label_1.configure(text=f"The the traversal order is {path[1]}!")
            else:
                if path[0] == True:
                    self.add_widget(self.result_label_2, 4, 0, 2)
                    self.result_label_2.configure(text=f"Successfully found, path: {path[1]}")
                else:
                    self.add_widget(self.result_label_2, 4, 0, 2)
                    self.result_label_2.configure(text=f"Node not found, order of traversal is:\n {path[1]}")
        
        if self.algorithm == "DLS":
            if path[0] == None:
                self.result_label_1.configure(text=f"The traversal for {depth_limit} depth limit is: \n {path[1]}!")
            else:
                if path[0] == True:
                    self.add_widget(self.result_label_2, 4, 0, 2)
                    self.result_label_2.configure(text=f"Successfully found at depth limit: {depth_limit}, \npath: {path[1]}")
                else:
                    self.add_widget(self.result_label_2, 4, 0, 2)
                    self.result_label_2.configure(text=f"Node not found at depth limit: {depth_limit}, \npath: {path[1]}!")
        if self.algorithm == "IDDFS":
            if user_input == '':
                self.result_label_1.configure(text="Please enter a goal node.")
                return
            else:
                if path[0] == True:
                    self.result_label_1.configure(text=f"Successfully found at max depth limit: {depth_limit}, \npath: {path[1]}")
                else:
                    self.result_label_1.configure(text=f"Node not found at max depth limit: {depth_limit}, \npath: {path[1]}")
        if self.algorithm == "UCS":
            if user_input == '':
                self.result_label_1.configure(text="Please enter a goal node.")
                return
            else:
                if path[0]:
                    self.result_label_1.configure(text=f"Successfully found at path cost: {path[1]}, \npath: {path[2]}")
                else:
                    self.result_label_1.configure(text=f"Node not found.")
        if self.algorithm == "Bidirectional Search":
            if user_input == '':
                self.result_label_1.configure(text="Please enter a goal node.")
                return
            else:
                if path[0]:
                    self.result_label_1.configure(text=f"Successfully found at path cost: {path[1]}, \npath: {path[2]}")
                else:
                    self.result_label_1.configure(text=f"Node not found.")
        if self.algorithm in "A* Search":
            if user_input == '':
                self.result_label_1.configure(text="Please enter a goal node.")
                return
            else: 
                if path[0]:
                    self.result_label_1.configure(
                        text=f"Successfully found at path cost: {path[1]}, \npath: {path[2]}"
                        )
                else:
                    self.result_label_1.configure(text=f"Node not found.")
        if self.algorithm in "Best-First Search":
            if user_input == '':
                self.result_label_1.configure(text="Please enter a goal node.")
                return
            else: 
                if path[0]:
                    self.result_label_1.configure(
                        text=f"Successfully found at path: {path[1]}"
                        )
                else:
                    self.result_label_1.configure(text=f"Node not found.")


    def get_path(self, goal, depth_limit=1):
        if self.algorithm == "BFS":
            response = breadth_first_search(bfs_and_dfs_search_graph, goal)
        elif self.algorithm == "DFS":
            response = depth_first_search(bfs_and_dfs_search_graph, goal)
        elif self.algorithm == "DLS":
            response = depth_limited_traversal(depth_limited_search_graph, depth_limit, goal)
        elif self.algorithm == "IDDFS":
            response = iterative_deepening_search(iddfs_graph, goal, depth_limit)
        elif self.algorithm == "UCS":
            response = uniform_cost_search(uniform_cost_search_graph, goal)
        elif self.algorithm == "Bidirectional Search":
            response = bidirectional_search_with_costs(bidirectional_search_graph_1, goal)
        elif self.algorithm == "A* Search":
            response = a_star_search(informed_detail[0], informed_detail[1], goal)
        elif self.algorithm == "Best-First Search":
            response = best_first_search(informed_detail[0], informed_detail[1], goal)
        return response
