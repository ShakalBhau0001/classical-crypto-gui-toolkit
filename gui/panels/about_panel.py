import customtkinter as ctk


class AboutPanel(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self, text="Classical Crypto GUI Toolkit", font=("Arial", 22, "bold")
        )
        self.title_label.grid(row=0, column=0, pady=15)

        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        self.content_frame.grid_columnconfigure(0, weight=1)

        description = (
            "This application is a Classical Cryptography Toolkit built using Python "
            "and CustomTkinter.\n\n"
            "It provides implementations of multiple classical encryption algorithms "
            "along with brute-force attack modules."
        )

        self.desc_label = ctk.CTkLabel(
            self.content_frame, text=description, justify="left", wraplength=700
        )
        self.desc_label.grid(row=0, column=0, sticky="w", pady=10)

        cipher_text = (
            "Supported Ciphers:\n"
            "• Caesar Cipher\n"
            "• Rail Fence Cipher\n"
            "• Playfair Cipher\n"
            "• Row Column Transposition"
        )

        self.cipher_label = ctk.CTkLabel(
            self.content_frame, text=cipher_text, justify="left"
        )
        self.cipher_label.grid(row=1, column=0, sticky="w", pady=10)

        attack_text = (
            "Supported Attacks:\n" "• Caesar Brute Force\n" "• Rail Fence Brute Force"
        )

        self.attack_label = ctk.CTkLabel(
            self.content_frame, text=attack_text, justify="left"
        )
        self.attack_label.grid(row=2, column=0, sticky="w", pady=10)

        tech_text = (
            "Tech Stack:\n"
            "• Python\n"
            "• CustomTkinter\n"
            "• Modular Architecture"
        )

        self.tech_label = ctk.CTkLabel(
            self.content_frame, text=tech_text, justify="left"
        )
        self.tech_label.grid(row=3, column=0, sticky="w", pady=10)

        # Footer
        self.footer_label = ctk.CTkLabel(self, text="Version 1.0", font=("Arial", 12))
        self.footer_label.grid(row=2, column=0, pady=10)
