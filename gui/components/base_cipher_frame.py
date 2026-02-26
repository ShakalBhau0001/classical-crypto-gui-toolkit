import customtkinter as ctk
from .text_area import TextArea
from .action_buttons import ActionButtons


class BaseCipherFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # Input Area
        self.input_area = TextArea(self, "Input")
        self.input_area.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 5))

        # Key section
        self.key_frame = ctk.CTkFrame(self)
        self.key_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

        # Action Buttons
        self.buttons = ActionButtons(
            self,
            encrypt_callback=self.encrypt_action,
            decrypt_callback=self.decrypt_action,
        )
        self.buttons.grid(row=2, column=0, pady=5)

        # Output Area
        self.output_area = TextArea(self, "Output")
        self.output_area.grid(row=3, column=0, sticky="nsew", padx=10, pady=(5, 10))

    # To be overridden method of child classes
    def encrypt_action(self):
        pass

    def decrypt_action(self):
        pass
