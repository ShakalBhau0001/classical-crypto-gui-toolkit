import customtkinter as ctk
from .components.sidebar import Sidebar
from .panels.cipher_panel import CipherPanel
from .panels.attack_panel import AttackPanel
from .panels.about_panel import AboutPanel


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Classical Crypto Toolkit")
        self.geometry("1000x600")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = Sidebar(self, self.switch_panel)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.container = ctk.CTkFrame(self)
        self.container.grid(row=0, column=1, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.current_panel = None
        self.switch_panel("Cipher")

    def switch_panel(self, name):
        if self.current_panel:
            self.current_panel.destroy()

        if name == "Cipher":
            self.current_panel = CipherPanel(self.container)
        elif name == "Attack":
            self.current_panel = AttackPanel(self.container)
        else:
            self.current_panel = AboutPanel(self.container)

        self.current_panel.grid(row=0, column=0, sticky="nsew")
