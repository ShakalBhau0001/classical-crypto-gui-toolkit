import customtkinter as ctk
from .main_window import MainWindow


def run_app():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = MainWindow()
    app.mainloop()
