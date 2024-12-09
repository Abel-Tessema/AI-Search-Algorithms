import customtkinter as ctk

from notes.notes import notes

class noteWidget(ctk.CTkTextbox):
    def __init__(self, master, algorithm="DFS"):
        super().__init__(master, width=550, wrap="word")

        self.insert("1.0", notes[f"{algorithm}"])
        self.configure(state="disabled")  # Make the textbox read-only

    def update_content(self, algorithm):
        self.configure(state="normal")
        self.delete("1.0", "end")
        self.insert("1.0", notes[f"{algorithm}"])
        self.configure(state="disabled")  # Make the textbox read-only