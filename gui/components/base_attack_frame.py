import customtkinter as ctk


class BaseAttackFrame(ctk.CTkFrame):

    def __init__(self, parent, title_text="Attack Panel"):
        super().__init__(parent)

        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Title
        self.title_label = ctk.CTkLabel(
            self, text=title_text, font=("Arial", 20, "bold")
        )
        self.title_label.grid(row=0, column=0, pady=10)

        # Ciphertext Input
        self.input_label = ctk.CTkLabel(self, text="Ciphertext")
        self.input_label.grid(row=1, column=0, sticky="w", padx=20)

        self.input_text = ctk.CTkTextbox(self, height=120)
        self.input_text.grid(row=2, column=0, sticky="ew", padx=20, pady=5)

        # Run Button
        self.run_button = ctk.CTkButton(
            self, text="Run Attack", command=self.run_attack
        )
        self.run_button.grid(row=3, column=0, pady=10)

        # Results
        self.output_label = ctk.CTkLabel(self, text="Results")
        self.output_label.grid(row=4, column=0, sticky="w", padx=20)

        self.output_text = ctk.CTkTextbox(self)
        self.output_text.grid(row=5, column=0, sticky="nsew", padx=20, pady=5)

        self.grid_rowconfigure(5, weight=1)

    # Child classes must implement this method to perform the specific attack logic
    def run_attack(self):
        raise NotImplementedError("Subclasses must implement run_attack()")

    # Common error dialog box
    def show_error(self, message):
        dialog = ctk.CTkToplevel(self)
        dialog.title("Error")
        dialog.geometry("320x150")
        dialog.grab_set()

        label = ctk.CTkLabel(dialog, text=message, wraplength=280)
        label.pack(pady=25, padx=20)

        button = ctk.CTkButton(dialog, text="OK", command=dialog.destroy)
        button.pack(pady=10)
