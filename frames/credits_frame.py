import customtkinter as ctk

# Text for credits
text = """
Developed by: Group One
"""

class CreditsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#232323")

        # Title label
        title_label = ctk.CTkLabel(
            self,
            text="Credits",
            font=("Arial", 36, "bold"),
            text_color="white",
        )
        title_label.pack(pady=(30, 10))

        # Credits information (scrollable area)
        credits_text = ctk.CTkLabel(
            self,
            text=text,
            font=("Arial", 16),
            text_color="lightgray",
            anchor="w",
            justify="left",
        )
        credits_text.pack(padx=20, pady=(10, 0), anchor="w")

        # Table below the credits text
        self.create_table()

        # Back button at the bottom
        back_button = ctk.CTkButton(
            self,
            text="Back",
            command=self.master.show_main_layout,
            fg_color="#1a73e8",
            font=("Arial", 16),
            corner_radius=8,
            width=150,
        )
        back_button.pack(pady=(20, 30))

    def create_table(self):
        # Table Headers
        headers = ["No", "Name", "ID"]
        header_font = ctk.CTkFont("Arial", size=16, weight="bold")

        # Table Frame for Layout
        table_frame = ctk.CTkFrame(self, fg_color="#232323")
        table_frame.pack(pady=0, padx=20, fill="both", expand=True)

        # Header Row Styling
        for col, header in enumerate(headers):
            label = ctk.CTkLabel(
                table_frame,
                text=header,
                font=header_font,
                text_color="white",
                fg_color="#232323",
                corner_radius=6,
                padx=15,
                pady=10,
            )
            label.grid(row=0, column=col, padx=5, pady=5, sticky="ew")

        # Table Data
        data = [
            (1, "Abduselam Sultan", "ETS0024/14"),
            (2, "Abel Tessema", "ETS0027/14"),
            (3, "Abel Maireg", "ETS0028/14"),
            (4, "Abel Mulat", "ETS0029/14"),
            (5, "Abel Seyoum", "ETS0032/14"),
            (6, "Abel Bogale", "ETS0035/14"),
        ]

        # Populate Data Rows
        for row, entry in enumerate(data, start=1):
            for col, value in enumerate(entry):
                label = ctk.CTkLabel(
                    table_frame,
                    text=str(value),
                    font=("Arial", 14),
                    text_color="lightgray",
                    padx=15,
                    pady=0,
                )
                label.grid(row=row, column=col, padx=5, pady=0, sticky="ew")

