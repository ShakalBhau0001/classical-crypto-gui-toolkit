import customtkinter as ctk
from gui.components.base_attack_frame import BaseAttackFrame
from core.attacks import rail_fence_brute


class RailFenceAttackPanel(BaseAttackFrame):

    def __init__(self, parent):
        super().__init__(parent, title_text="Rail Fence Brute Force Attack")

        # Insertion of Max Rails input
        self.rails_label = ctk.CTkLabel(self, text="Max Rails")
        self.rails_label.grid(row=3, column=0, sticky="w", padx=20)

        self.rails_entry = ctk.CTkEntry(self)
        self.rails_entry.insert(0, "10")
        self.rails_entry.grid(row=4, column=0, sticky="ew", padx=20, pady=5)

        # Moving run button down
        self.run_button.grid(row=5, column=0, pady=10)

        # Moving output section down
        self.output_label.grid(row=6, column=0, sticky="w", padx=20)
        self.output_text.grid(row=7, column=0, sticky="nsew", padx=20, pady=5)

        self.grid_rowconfigure(7, weight=1)

    def run_attack(self):
        ciphertext = self.input_text.get("1.0", "end").strip()
        max_rails_value = self.rails_entry.get().strip()

        if not ciphertext:
            self.show_error("Ciphertext is required.")
            return

        if not max_rails_value.isdigit():
            self.show_error("Max Rails must be a positive number.")
            return

        max_rails = int(max_rails_value)

        if max_rails < 2:
            self.show_error("Max Rails must be at least 2.")
            return

        self.output_text.delete("1.0", "end")

        try:
            results = rail_fence_brute.brute_force(ciphertext, max_rails)

            for result in results:
                rails = result["rails"]
                plaintext = result["plaintext"]

                self.output_text.insert("end", f"Rails {rails}:\n{plaintext}\n\n")

        except Exception as e:
            self.show_error(str(e))

