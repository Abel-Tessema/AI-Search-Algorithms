import customtkinter as ctk

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
        self.result_label = ctk.CTkLabel(self, text="Search a node...")

        self.layout_widgets()  # Initial layout

    def layout_widgets(self):
        self.clear_grid()
        if self.algorithm in ["BFS", "DFS"]:
            self.add_widget(self.label_goal, 0, 0)
            self.add_widget(self.goal_node_input, 0, 1)
            self.add_widget(self.search_button, 2, 0, 2)
        elif self.algorithm == "DLS":
            self.add_widget(self.label_depth, 0, 0)
            self.add_widget(self.depth_input, 0, 1)
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

        self.add_widget(self.result_label, 3, 0, 2)

    def add_widget(self, widget, row, col, colspan=1):
        widget.grid(row=row, column=col, columnspan=colspan, sticky="ew", padx=5, pady=5)

    def clear_grid(self):
        for widget in self.winfo_children():
            widget.grid_forget()

    def update_algorithm(self, algorithm):
        if algorithm != self.algorithm:
            self.algorithm = algorithm
            self.goal_node_input.delete(0, ctk.END)
            self.depth_input.delete(0, ctk.END)
            self.result_label.configure(text="Search a node...")
            self.layout_widgets()

    def submit_action(self):
        user_input = self.goal_node_input.get()
        depth_limit = int(self.depth_input.get() or 1)
        path = self.get_path(user_input, depth_limit)
        self.result_label.configure(text=f"The path to the goal node {user_input} is {path}!")

    def get_path(self, goal, depth_limit=1):
        # Replace with actual algorithm calls
        return f"Path calculated for {self.algorithm} to {goal} with depth {depth_limit}."
