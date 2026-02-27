from core.ciphers import row_column
import customtkinter as ctk
from tkinter import messagebox


class RowColumnPanel(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.title_label = ctk.CTkLabel(
            self, text="Row Column Cipher", font=("Arial", 20, "bold")
        )
        self.title_label.pack(pady=20)

        self.input_label = ctk.CTkLabel(self, text="Input Text")
        self.input_label.pack(anchor="w", padx=20)

        self.input_text = ctk.CTkTextbox(self, height=120)
        self.input_text.pack(fill="x", padx=20, pady=5)

        self.key_label = ctk.CTkLabel(self, text="Keyword")
        self.key_label.pack(anchor="w", padx=20)

        self.key_entry = ctk.CTkEntry(self)
        self.key_entry.pack(fill="x", padx=20, pady=5)

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=15)

        self.encrypt_button = ctk.CTkButton(
            self.button_frame, text="Encrypt", command=self.encrypt_action
        )
        self.encrypt_button.pack(side="left", padx=10)

        self.decrypt_button = ctk.CTkButton(
            self.button_frame, text="Decrypt", command=self.decrypt_action
        )
        self.decrypt_button.pack(side="left", padx=10)

        # Output
        self.output_label = ctk.CTkLabel(self, text="Output")
        self.output_label.pack(anchor="w", padx=20)

        self.output_text = ctk.CTkTextbox(self, height=120)
        self.output_text.pack(fill="x", padx=20, pady=5)
        self.output_text.configure(state="disabled")

    def encrypt_action(self):
        text = self.input_text.get("1.0", "end").strip()
        key = self.key_entry.get().strip()

        if not text or not key:
            messagebox.showerror("Error", "Text and Keyword are required.")
            return

        try:
            result = row_column.encrypt(text, key)
            self.display_output(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decrypt_action(self):
        text = self.input_text.get("1.0", "end").strip()
        key = self.key_entry.get().strip()

        if not text or not key:
            messagebox.showerror("Error", "Ciphertext and Keyword are required.")
            return

        try:
            result = row_column.decrypt(text, key)
            self.display_output(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_output(self, result):
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result)
        self.output_text.configure(state="disabled")
