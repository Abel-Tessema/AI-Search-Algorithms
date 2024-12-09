import customtkinter as ctk

from widgets.noteWidget import noteWidget
from widgets.graphWidget import graphWidget
from widgets.search_output import search_output


class MainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="blue")

        self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)
        # self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create an area to display the notes that are needed
        self.textbox = noteWidget(self)
        self.textbox.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=20, pady=20)

        # create an area to diplay the graph being used
        self.graphWidget = graphWidget(self,)
        self.graphWidget.grid(row=0, column=1,  sticky="nsew", padx=20, pady=20)

        self.search_output = search_output(self, )
        self.search_output.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

    def button_clicked(self, algorithm):
        # Update the note
        self.textbox.update_content(algorithm)
        
        # # Update the graph section
        # self.graphWidget.grid_remove()
        # self.graphWidget = graphWidget(self, algorithm=algorithm)
        # self.graphWidget.grid(row=0, column=1,  sticky="nsew", padx=20, pady=20)

        # # Update the search output
        # self.search_output.grid_remove()
        # self.search_output = search_output(self, algorithm=algorithm)
        # self.search_output.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
        # print("Button clicked!")
