import customtkinter as ctk

class search_output(ctk.CTkFrame):
    def __init__(self, master, algorithm="DFS"):
        super().__init__(master, fg_color="magenta")

        self.columnconfigure(0, weight=1)

        def submit_action():
            user_input = input_field.get()
            result_label.configure(text=f"You entered: {user_input}")

        # Create an Input Field
        input_field = ctk.CTkEntry(self, placeholder_text="Enter something")
        input_field.grid(row=0, column=0, sticky="ew")

        # Create a Submit Button
        search_button = ctk.CTkButton(self, text="Search", command=submit_action)
        search_button.grid(row=0, column=1)

        # Create a Label to Display the Result
        result_label = ctk.CTkLabel(self, text="Your input will appear here.")
        result_label.grid(row=1, column=0, columnspan=2, sticky="w")