from gui.components.base_attack_frame import BaseAttackFrame
from core.attacks import caesar_brute


class CaesarAttackPanel(BaseAttackFrame):

    def __init__(self, parent):
        super().__init__(parent, title_text="Caesar Brute Force Attack")

    def run_attack(self):
        ciphertext = self.input_text.get("1.0", "end").strip()

        if not ciphertext:
            self.show_error("Ciphertext is required.")
            return

        self.output_text.delete("1.0", "end")

        try:
            results = caesar_brute.brute_force(ciphertext)

            for result in results:
                shift = result["shift"]
                direction = result["direction"]
                plaintext = result["plaintext"]

                self.output_text.insert(
                    "end", f"Shift {shift} ({direction}):\n{plaintext}\n\n"
                )

        except Exception as e:
            self.show_error(str(e))
