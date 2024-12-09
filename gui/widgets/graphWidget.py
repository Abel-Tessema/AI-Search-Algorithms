import customtkinter as ctk

class graphWidget(ctk.CTkFrame):
    def __init__(self, master, algorithm="DFS"):
        super().__init__(master, fg_color="yellow")