import json
import os
import random

class QuizBackend:

    set_dict: dict
    definition_term_list: list = []

    def __init__(self) -> None:
        self._get_file_path()

        for term, definition in self.set_dict.items():
            self.definition_term_list.append(
                DefinitionTermValue(term, definition)
            )

    def _get_file_path(self):
        print("Welcome!\nAvalable training sets are:")
        print(os.listdir("./quizzes"))
        training_set = input("What set would you like to train on? ")
        file = open(f"quizzes/{training_set}.json", "r")
        self.set_dict = json.load(file)
        file.close()

    def get_new_value(self):
        return random.choice(self.definition_term_list)


class DefinitionTermValue:
    def __init__(self, term: str, definition: str) -> None:
        self.term = term
        self.definition = definition
        self.count = 0
