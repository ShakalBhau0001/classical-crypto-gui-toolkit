import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent, switch_callback):
        super().__init__(parent, width=200)

        self.grid_rowconfigure(4, weight=1)

        ctk.CTkLabel(self, text="Crypto Toolkit", font=("Arial", 18, "bold")).grid(
            row=0, column=0, pady=20, padx=10
        )

        ctk.CTkButton(
            self, text="Cipher", command=lambda: switch_callback("Cipher")
        ).grid(row=1, column=0, pady=10, padx=15, sticky="ew")

        ctk.CTkButton(
            self, text="Attack", command=lambda: switch_callback("Attack")
        ).grid(row=2, column=0, pady=10, padx=15, sticky="ew")

        ctk.CTkButton(
            self, text="About", command=lambda: switch_callback("About")
        ).grid(row=3, column=0, pady=10, padx=15, sticky="ew")
