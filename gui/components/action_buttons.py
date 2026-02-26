import customtkinter as ctk


class ActionButtons(ctk.CTkFrame):
    def __init__(self, parent, encrypt_callback, decrypt_callback):
        super().__init__(parent)

        self.encrypt_btn = ctk.CTkButton(
            self, text="Encrypt", command=encrypt_callback, width=120
        )
        self.encrypt_btn.pack(side="left", padx=10)

        self.decrypt_btn = ctk.CTkButton(
            self, text="Decrypt", command=decrypt_callback, width=120
        )
        self.decrypt_btn.pack(side="left", padx=10)
