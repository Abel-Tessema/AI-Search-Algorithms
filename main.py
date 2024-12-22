import customtkinter as ctk

from frames.main_frame import MainFrame
from frames.sidebar_frame import SideBar
from frames.credits_frame import CreditsFrame
from frames.splash_screen_frame import SplashScreen
  

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#232323")
        self.title("Search Explorer")
        self.geometry("1300x600")
        self.resizable(False, False)

        self.splash_frame = SplashScreen(self)
        self.splash_frame.pack(fill="both", expand=True)

        self.after(3000, self.show_main_app)  

    def show_main_app(self):
        self.splash_frame.pack_forget()

        self.grid_rowconfigure(0, weight=1)  
        self.grid_columnconfigure(1, weight=1)  

        self.sidebar = SideBar(self)
        self.sidebar.grid(row=0, column=0, sticky="ns")  

        self.sidebar.credits_button.configure(command=self.show_credits)

        self.main_frame = MainFrame(self)
        self.main_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")  

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def show_credits(self):
        self.sidebar.grid_forget()
        self.main_frame.grid_forget()

        self.credits_frame = CreditsFrame(self,)
        self.credits_frame.pack(fill="both", expand=True)

    def show_main_layout(self):
        self.credits_frame.pack_forget()

        self.sidebar.grid(row=0, column=0, sticky="ns")
        self.main_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    def on_closing(self):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
