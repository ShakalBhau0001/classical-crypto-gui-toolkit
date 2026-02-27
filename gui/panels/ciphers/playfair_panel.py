import customtkinter as ctk
from core.ciphers import playfair
from tkinter import messagebox


class PlayfairPanel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.title = ctk.CTkLabel(
            self, text="Playfair Cipher", font=("Arial", 18, "bold")
        )
        self.title.pack(pady=15)

        self.input_label = ctk.CTkLabel(self, text="Input Text:")
        self.input_label.pack(anchor="w", padx=20)

        self.input_text = ctk.CTkTextbox(self, height=120)
        self.input_text.pack(fill="x", padx=20, pady=5)

        self.keyword_label = ctk.CTkLabel(self, text="Keyword:")
        self.keyword_label.pack(anchor="w", padx=20)

        self.keyword_entry = ctk.CTkEntry(self)
        self.keyword_entry.pack(fill="x", padx=20, pady=5)

        # Merging Option
        self.merge_label = ctk.CTkLabel(self, text="Merge Letter (I/J):")
        self.merge_label.pack(anchor="w", padx=20)

        self.merge_option = ctk.CTkOptionMenu(self, values=["I", "J"])
        self.merge_option.set("I")
        self.merge_option.pack(fill="x", padx=20, pady=5)

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(pady=15)

        self.encrypt_btn = ctk.CTkButton(
            self.button_frame, text="Encrypt", command=self.encrypt
        )
        self.encrypt_btn.pack(side="left", padx=10)

        self.decrypt_btn = ctk.CTkButton(
            self.button_frame, text="Decrypt", command=self.decrypt
        )
        self.decrypt_btn.pack(side="left", padx=10)

        self.output_label = ctk.CTkLabel(self, text="Output:")
        self.output_label.pack(anchor="w", padx=20)

        self.output_text = ctk.CTkTextbox(self, height=120)
        self.output_text.pack(fill="x", padx=20, pady=5)
        self.output_text.configure(state="disabled")

    def encrypt(self):
        text = self.input_text.get("1.0", "end").strip()
        keyword = self.keyword_entry.get().strip()
        merge_letter = self.merge_option.get()

        if not text or not keyword:
            messagebox.showerror("Error", "Text and Keyword required")
            return

        try:
            result = playfair.encrypt(text, keyword, merge_letter)
            self._display_output(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decrypt(self):
        text = self.input_text.get("1.0", "end").strip()
        keyword = self.keyword_entry.get().strip()
        merge_letter = self.merge_option.get()

        if not text or not keyword:
            messagebox.showerror("Error", "Text and Keyword required")
            return

        try:
            result = playfair.decrypt(text, keyword, merge_letter)
            self._display_output(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _display_output(self, result):
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result)
        self.output_text.configure(state="disabled")
