import customtkinter as ctk

uninformed_alg_list = ['BFS', 'DFS', "DLS", "UCS", "IDDFS", "Bidirectional Search",]
informed_alg_list = ["Best-First Search", "A* Search",]


class SideBar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, )  

        # Set font for the titles
        heading_1 = ctk.CTkFont("Arial", 20, "bold",)

        # First title
        self.label = ctk.CTkLabel(self, text="Uninformed Search Algorithms", text_color="white" ,font=heading_1)
        self.label.grid(row=0, column=0, pady=20, padx=20)

        # Algorithm choices
        for i, alg in enumerate(uninformed_alg_list, start=1):
            ctk.CTkButton(self, text=alg, 
                          command=lambda alg=alg: self.button_clicked(alg)).grid(row=i, column=0, padx=20, pady=5, sticky='w')
        
        # Second title
        self.label = ctk.CTkLabel(self, text="Informed Search Algorithms", text_color="white" ,font=heading_1)
        self.label.grid(column=0,pady=20, padx=20)

        # Algorithm choices
        for i, alg in enumerate(informed_alg_list, start=len(uninformed_alg_list)+2):
            ctk.CTkButton(self, text=alg, 
                          command=lambda alg=alg: self.button_clicked(alg)).grid(row=i, column=0, padx=20, pady=5, sticky='w')

    def button_clicked(self, alg):
        self.master.main_frame.button_clicked(alg)
