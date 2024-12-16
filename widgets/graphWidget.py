import customtkinter as ctk
from utils.graphPlotter import plot_graph
from utils.graphs import (
    bidirectional_search_graph, 
    bfs_and_dfs_search_graph, 
    depth_limited_search_graph, 
    iddfs_graph, 
    uniform_cost_search_graph,
    informed_detail,
)

class graphWidget(ctk.CTkFrame):
    def __init__(self, master, algorithm="BFS"):
        super().__init__(master, fg_color="white")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.algorithm = algorithm
        self.plot_area = ctk.CTkFrame(self,)
        self.plot_area.grid(row=0, column=0, padx=2, pady=2,sticky='n')

        self.display_graph()

    def display_graph(self):
        """Display the graph based on the current algorithm."""
        adjacency_list = self.get_graph_data(self.algorithm)
        # Clear previous plot widgets if any
        for widget in self.plot_area.winfo_children():
            widget.destroy()

        weighted = self.algorithm in ["Bidirectional Search", "UCS", "Best-First Search", "A* Search"]
        plot_graph(self.plot_area, self.algorithm, adjacency_list, weighted)

    def update_graph(self, algorithm):
        """Update the graph with a new algorithm."""
        if self.algorithm != algorithm:
            self.algorithm = algorithm
            self.display_graph()

    def get_graph_data(self, algorithm):
        """Retrieve the corresponding adjacency list based on the selected algorithm."""
        graphs = {
            "DFS": bfs_and_dfs_search_graph,
            "BFS": bfs_and_dfs_search_graph,
            "Bidirectional Search": bidirectional_search_graph,
            "DLS": depth_limited_search_graph,
            "IDDFS": iddfs_graph,
            "UCS": uniform_cost_search_graph,
            "Best-First Search": informed_detail[0] , 
            "A* Search": informed_detail[0] ,
        }
        return graphs.get(algorithm, bfs_and_dfs_search_graph)
