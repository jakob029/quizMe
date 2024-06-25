"""Code owned by jakob029.

Usage:
- Personal Use: You are free to use, modify, and distribute the software for personal purposes without any obligations, provided there is no capital gain.

- Commercial Use: If you intend to use this software for commercial purposes (including but not limited to integration, customization, or distribution in a commercial product), you are required to compensate the owner (Name/Contact) for such usage. Please contact jakob.eneroth@protonmail.com to negotiate terms of compensation and obtain necessary permissions.
"""

import tkinter as tk
from backend_applications import QuizBackend, DefinitionTermValue
import time


class GuiInterface:
    """Graphical interface management class."""

    DEFINITION_LABEL: tk.Label
    QUESTION: DefinitionTermValue

    def __init__(self, quiz_backend: QuizBackend) -> None:
        """Define window variables."""
        self.quiz_backend = quiz_backend

        self.root_window = tk.Tk()
        self.root_window.geometry("800x500")
        self.root_window.title("Quizz prog")

        self.build_interface()
        self.root_window.mainloop()

    def build_interface(self):
        """Set up the default UI interface."""
        self.DEFINITION_LABEL = tk.Label(
            self.root_window, text="Quizz prog", font=("Arial", 20)
        )
        self.DEFINITION_LABEL.pack(padx=20, pady=20)

        self.entry_var = tk.StringVar()
        self.ans_entry = tk.Entry(textvariable=self.entry_var)
        self.ans_entry.pack()

        self.button = tk.Button(
            self.root_window, text="Submit answer", command=self._submit_answer
        )
        self.button.pack()

        self.lbl = tk.Label(self.root_window, text="")
        self.lbl.pack()

        self._next_question()

    def _next_question(self):
        """Set up the a new question in the UI."""
        self.QUESTION = self.quiz_backend.get_new_value()
        self.DEFINITION_LABEL.config(text=self.QUESTION.term)

    def _reset_output(self, sleep_interval: float = 1.5):
        """Reset the output label after given time interval."""
        self.root_window.update()
        time.sleep(sleep_interval)
        self.lbl.config(text=f"")
        self.root_window.update()

    def _correct_answer(self):
        """Set up next stage when correct answer is given."""
        self.lbl.config(text="That was correct!")
        self._reset_output()
        self._next_question()

    def _submit_answer(self):
        """Submit answer used for pushing the submit button."""
        user_input = self.ans_entry.get()
        self.entry_var.set("")
        if user_input.lower() == self.QUESTION.definition.lower():
            self._correct_answer()
            return

        self.lbl.config(
            text=f"Incorrect, the correct answer is {self.QUESTION.definition}"
        )
        self._reset_output()
