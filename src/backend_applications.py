"""Code owned by jakob029.

Usage:
- Personal Use: You are free to use, modify, and distribute the software for personal purposes
                  without any obligations, provided there is no capital gain.

- Commercial Use: If you intend to use this software for commercial purposes (including but not
                    limited to integration, customization, or distribution in a commercial
                    product), you are required to compensate the owner. Please contact
                    jakob.eneroth@protonmail.com
"""

import json
import os
import random


class DefinitionTermValue:
    """Class structure to store and track set unit."""

    def __init__(self, term: str, definition: str, index: int) -> None:
        """Constructor.
        Args:
        ----
            term: Individual term.
            definition: Individual definition.
        """
        self.term = term
        self.definition = definition
        self.count = 0
        self.index = index


class QuizBackend:
    """Backend for the quiz application."""

    set_dict: dict
    definition_term_list: list = []
    non_completed_terms: list

    def __init__(self) -> None:
        """Constructor."""
        self._get_file_path()

        for term, definition in self.set_dict.items():
            index = len(self.definition_term_list)
            self.definition_term_list.append(DefinitionTermValue(term, definition, index))
            self.non_completed_terms = [i for i, _ in enumerate(self.definition_term_list)]

    def _get_file_path(self):
        """Get a selection of quiz to use from the user."""
        print("Welcome!\nAvalable training sets are:")
        print(os.listdir("./quizzes"))
        training_set = input("What set would you like to train on? ")
        with open(f"quizzes/{training_set}.json", "r", encoding="utf-8") as file:
            self.set_dict = json.load(file)

    def get_new_value(self) -> DefinitionTermValue | bool:
        """Retrieve a new term value combo to quiz."""
        if not self.non_completed_terms:
            return True

        index = random.choice(self.non_completed_terms)
        return self.definition_term_list[index]
