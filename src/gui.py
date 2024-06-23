import tkinter as tk
from backend_applications import QuizBackend, DefinitionTermValue
import time

class GuiInterface:
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
        self.DEFINITION_LABEL = tk.Label(self.root_window, text="Quizz prog", font=("Arial", 20))
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
        self.QUESTION = self.quiz_backend.get_new_value()
        self.DEFINITION_LABEL.config(text=self.QUESTION.term)

    def _reset_output(self):
        self.root_window.update()
        time.sleep(1.5)
        self.lbl.config(text=f"")
        self.root_window.update()

    def _correct_answer(self):
        self.lbl.config(text="That was correct!")
        self._reset_output()
        self._next_question()

    def _submit_answer(self):
        user_input = self.ans_entry.get()
        self.entry_var.set("")
        if user_input.lower() == self.QUESTION.definition.lower():
            self._correct_answer()
            return

        self.lbl.config(text=f"Incorrect, the correct answer is {self.QUESTION.definition}")
        self._reset_output()