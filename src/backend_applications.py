"""Code owned by jakob029.

Usage:
- Personal Use: You are free to use, modify, and distribute the software for personal purposes without any obligations, provided there is no capital gain.

- Commercial Use: If you intend to use this software for commercial purposes (including but not limited to integration, customization, or distribution in a commercial product), you are required to compensate the owner. Please contact jakob.eneroth@protonmail.com to negotiate terms of compensation and obtain necessary permissions.
"""

import json
import os
import random


class DefinitionTermValue:
    """Class structure to store and track set unit."""

    def __init__(self, term: str, definition: str) -> None:
        """Constructor.
        Args:
        ----
            term: Individual term.
            definition: Individual definition.
        """
        self.term = term
        self.definition = definition
        self.count = 0


class QuizBackend:
    """Backend for the quiz application."""

    set_dict: dict
    definition_term_list: list = []

    def __init__(self) -> None:
        """Constructor."""
        self._get_file_path()

        for term, definition in self.set_dict.items():
            self.definition_term_list.append(DefinitionTermValue(term, definition))

    def _get_file_path(self):
        """Get a selection of quiz to use from the user."""
        print("Welcome!\nAvalable training sets are:")
        print(os.listdir("./quizzes"))
        training_set = input("What set would you like to train on? ")
        file = open(f"quizzes/{training_set}.json", "r")
        self.set_dict = json.load(file)
        file.close()

    def get_new_value(self) -> DefinitionTermValue:
        """Retrieve a new term value combo to quiz."""
        return random.choice(self.definition_term_list)
