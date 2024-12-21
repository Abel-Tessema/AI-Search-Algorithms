import customtkinter as ctk

class SplashScreen(ctk.CTkFrame):
    def __init__(self, master,):
        super().__init__(master, fg_color="#232323")

        self.splash_labels = ctk.CTkFrame(self, fg_color="#232323")
        self.splash_labels.pack(expand=True)

        splash_label = ctk.CTkLabel(
            self.splash_labels,
            text="Search Algorithms Explorer",
            font=("Arial", 36, "bold"),
            text_color="white",
        )
        splash_label.pack()

        splash_label_2 = ctk.CTkLabel(
            self.splash_labels,
            text="Developed by Group 1",
            font=("Arial", 16, "bold"),
            text_color="lightblue",
        )
        splash_label_2.pack()