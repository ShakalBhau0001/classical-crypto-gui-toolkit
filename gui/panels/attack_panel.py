import customtkinter as ctk
from .attacks.caesar_attack_panel import CaesarAttackPanel
from .attacks.railfence_attack_panel import RailFenceAttackPanel


class AttackPanel(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        # Layout configuration
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Dropdown menu for selecting attack type
        self.dropdown = ctk.CTkOptionMenu(
            self,
            values=["Caesar", "Rail Fence"],
            command=self.load_attack,
        )
        self.dropdown.grid(row=0, column=0, pady=10)

        # Container for loading attack panels
        self.container = ctk.CTkFrame(self)
        self.container.grid(row=1, column=0, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.current_panel = None
        self.load_attack("Caesar")

    def load_attack(self, name):
        if self.current_panel:
            self.current_panel.destroy()

        if name == "Caesar":
            self.current_panel = CaesarAttackPanel(self.container)

        elif name == "Rail Fence":
            self.current_panel = RailFenceAttackPanel(self.container)

        self.current_panel.grid(row=0, column=0, sticky="nsew")

