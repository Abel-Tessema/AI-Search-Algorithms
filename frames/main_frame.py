import customtkinter as ctk

from widgets.noteWidget import noteWidget
from widgets.graphWidget import graphWidget
from widgets.search_output import search_output


class MainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,fg_color="#232323")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1, pad=20)

        # create an area to display the notes that are needed
        self.textbox = noteWidget(self)
        self.textbox.grid(row=0, column=0, padx=10, pady=10,rowspan=2, sticky="nsew",)

        # create an area to diplay the graph being used
        self.graphWidget = graphWidget(self,)
        self.graphWidget.grid(row=0, column=1, padx=10, pady=10,sticky="nsew",  )

        self.search_output = search_output(self, )
        self.search_output.grid(row=1, padx=10, pady=10,column=1, sticky="nsew", )

    def button_clicked(self, algorithm):
        self.textbox.update_content(algorithm)
        self.graphWidget.update_graph(algorithm)
        self.search_output.update_algorithm(algorithm)
