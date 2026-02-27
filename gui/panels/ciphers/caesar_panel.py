import customtkinter as ctk
from core.ciphers.caesar import encrypt, decrypt


class CaesarPanel(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self, text="Caesar Cipher", font=("Arial", 16, "bold")).grid(
            row=0, column=0, pady=10
        )

        self.input_text = ctk.CTkTextbox(self, height=100)
        self.input_text.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        # Shifting Dropdown
        ctk.CTkLabel(self, text="Shift:").grid(row=2, column=0, sticky="w", padx=20)

        self.shift_var = ctk.StringVar(value="3")
        self.shift_menu = ctk.CTkOptionMenu(
            self, values=[str(i) for i in range(26)], variable=self.shift_var
        )
        self.shift_menu.grid(row=3, column=0, padx=20, pady=5, sticky="w")

        ctk.CTkButton(self, text="Encrypt", command=self.encrypt_text).grid(
            row=4, column=0, pady=5
        )

        ctk.CTkButton(self, text="Decrypt", command=self.decrypt_text).grid(
            row=5, column=0, pady=5
        )

        self.output_text = ctk.CTkTextbox(self, height=100)
        self.output_text.grid(row=6, column=0, padx=20, pady=10, sticky="ew")

    def encrypt_text(self):
        try:
            text = self.input_text.get("1.0", "end").strip()
            shift = int(self.shift_var.get())
            result = encrypt(text, shift)

            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", result)

        except Exception as e:
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", str(e))

    def decrypt_text(self):
        try:
            text = self.input_text.get("1.0", "end").strip()
            shift = int(self.shift_var.get())
            result = decrypt(text, shift)

            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", result)

        except Exception as e:
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", str(e))

