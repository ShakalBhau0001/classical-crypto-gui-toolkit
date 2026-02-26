import customtkinter as ctk
from .ciphers.caesar_panel import CaesarPanel
from .ciphers.rail_fence_panel import RailFencePanel
from .ciphers.playfair_panel import PlayfairPanel
from .ciphers.row_column_panel import RowColumnPanel


class CipherPanel(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # Layout configuration
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Dropdown menu for selecting attack type
        self.dropdown = ctk.CTkOptionMenu(
            self,
            values=["Caesar", "Rail Fence", "Playfair", "RowColumn"],
            command=self.load_cipher,
        )
        self.dropdown.grid(row=0, column=0, pady=10)

        # Container for loading attack panels
        self.container = ctk.CTkFrame(self)
        self.container.grid(row=1, column=0, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.current_panel = None
        self.load_cipher("Caesar")

    def load_cipher(self, name):
        if self.current_panel:
            self.current_panel.destroy()

        if name == "Caesar":
            self.current_panel = CaesarPanel(self.container)
        elif name == "Rail Fence":
            self.current_panel = RailFencePanel(self.container)
        elif name == "Playfair":
            self.current_panel = PlayfairPanel(self.container)
        elif name == "RowColumn":
            self.current_panel = RowColumnPanel(self.container)

        self.current_panel.grid(row=0, column=0, sticky="nsew")
