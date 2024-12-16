import customtkinter as ctk

from utils.notes import notes

class noteWidget(ctk.CTkTextbox):
    def __init__(self, master, algorithm="BFS"):
        super().__init__(master, width=550, wrap="word")

        self.algorithm = algorithm
        self.insert("1.0", notes[f"{algorithm}"])
        self.configure(state="disabled")  # Make the textbox read-only

    def update_content(self, algorithm):
        if self.algorithm != algorithm:
            self.algorithm = algorithm
            self.configure(state="normal")
            self.delete("1.0", "end")
            self.insert("1.0", notes[f"{algorithm}"])
            self.configure(state="disabled")  # Make the textbox read-only