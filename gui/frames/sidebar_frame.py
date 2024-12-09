import customtkinter as ctk

uninformed_alg_list = ['BFS', 'DFS', "DLS", "UCS", "IDDFS", "Bidirectional Search",]
informed_alg_list = ["Best-First Search", "A* Search",]


class SideBar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="Grey")  

        # Set font for the titles
        my_font_title = ctk.CTkFont("Arial", 20, "bold", )

        # First title
        self.label = ctk.CTkLabel(self, text="Uninformed Search Algorithms", text_color="black" ,font=my_font_title)
        self.label.grid(row=0, column=0,)

        # Algorithm choices
        for i, alg in enumerate(uninformed_alg_list, start=1):
            ctk.CTkButton(self, text=alg, 
                          command=lambda alg=alg: self.button_clicked(alg)).grid(row=i, column=0, padx=10, pady=5)
        
        # Second title
        self.label = ctk.CTkLabel(self, text="Informed Search Algorithms", text_color="black" ,font=my_font_title)
        self.label.grid(column=0,)

        # Algorithm choices
        for i, alg in enumerate(informed_alg_list, start=len(uninformed_alg_list)+2):
            ctk.CTkButton(self, text=alg, 
                          command=lambda alg=alg: self.button_clicked(alg)).grid(row=i, column=0, padx=10, pady=5)

    def button_clicked(self, alg):
        self.master.main_frame.button_clicked(alg)
        print("Button clicked!, {}".format(alg))
