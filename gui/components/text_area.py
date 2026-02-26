import customtkinter as ctk


class TextArea(ctk.CTkFrame):
    def __init__(self, parent, label_text):
        super().__init__(parent)

        ctk.CTkLabel(self, text=label_text).pack(anchor="w", padx=5)

        self.textbox = ctk.CTkTextbox(self, height=150)
        self.textbox.pack(fill="both", expand=True, padx=5, pady=5)

    def get(self):
        return self.textbox.get("1.0", "end").strip()

    def set(self, value):
        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", value)
