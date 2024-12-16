# import customtkinter as ctk
# from frames.main_frame import MainFrame
# from frames.sidebar_frame import SideBar

# ctk.set_appearance_mode("dark")  # Dark mode
# ctk.set_default_color_theme("blue")  # Blue theme

# class App(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#         self.title("CustomTkinter Modular App")
#         self.geometry("1300x600")
#         self.resizable(False, False)

#         # Create a grid layout for the App window
#         self.grid_rowconfigure(0, weight=1)  # Make the row stretchable
#         self.grid_columnconfigure(1, weight=1)  # Make the main frame stretchable

#         # Create the sidebar frame
#         self.sidebar = SideBar(self)
#         self.sidebar.grid(row=0, column=0, sticky="ns")  # Sidebar spans top to bottom

#         # Create the main frame
#         self.main_frame = MainFrame(self)
#         self.main_frame.grid(row=0, column=1, sticky="nsew")  # Main frame fills the space

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

import customtkinter as ctk
from frames.main_frame import MainFrame
from frames.sidebar_frame import SideBar

ctk.set_appearance_mode("dark")  # Dark mode
ctk.set_default_color_theme("blue")  # Blue theme

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#232323")
        self.title("CustomTkinter Modular App")
        self.geometry("1300x600")
        self.resizable(False, False)

        # Create a grid layout for the App window
        self.grid_rowconfigure(0, weight=1)  # Make the row stretchable
        self.grid_columnconfigure(1, weight=1)  # Make the main frame stretchable

        # Create the sidebar frame
        self.sidebar = SideBar(self)
        self.sidebar.grid(row=0, column=0, sticky="ns")  # Sidebar spans top to bottom

        # Create the main frame
        self.main_frame = MainFrame(self)
        self.main_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")  # Main frame fills the space

        # Register close event
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
