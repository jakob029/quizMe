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
import random
import time
import os
import datetime
import yaml

SETTINGS = {}


def correct_ans(set_dict: dict, descr: str, first_time: bool) -> None:
    if first_time:
        del set_dict[descr]
    print("Coorect!")
    time.sleep(1)
    os.system("cls || clear")


def quiz_on_dict(set_dict: dict, settings) -> int:
    total_amount_errors = 0
    while set_dict:
        os.system("cls || clear")
        descr = random.choice(list(set_dict))
        print("Description: ", descr)
        ans = input("Word: ")
        if ans.lower() == set_dict[descr].lower():
            correct_ans(set_dict, descr, True)
        else:
            while True:
                total_amount_errors += 1
                os.system("cls || clear")
                print("That was wrong, the correct ans is: ", set_dict[descr])
                print(f"Your said {ans}")
                if settings["auto_continue_on_wrong_answer"] is False:
                    input("Press enter to continue")
                else:
                    time.sleep(settings["auto_continue_on_wrong_answer"])
                os.system("cls || clear")
                print("Description: ", descr)
                try:
                    ans = input("Word: ")
                except Exception as exc:
                    pass  # Unsloved BUGG
                if ans.lower() == set_dict[descr].lower():
                    correct_ans(set_dict, descr, False)
                    break
                if ans.lower() == "c#":
                    correct_ans(set_dict, descr, True)
                    total_amount_errors -= 1
                    break
    return total_amount_errors


def quiz(training_set: str, settings) -> None:
    training_set = training_set.replace(" ", "-")
    file = open(f"quizzes/{training_set}.json", "r")
    set_dict = json.load(file)
    file.close()
    no_of_errors = quiz_on_dict(set_dict, settings)
    print(f"Good job!\nYou completed the task with {no_of_errors} error/s!")


def run_cli() -> None:
    print("Welcome!\nAvalable training sets are:")
    print(os.listdir("./quizzes"))
    training_set = input("What set would you like to train on? ")
    with open("configs/settings.yaml", "r") as file:
        settings = yaml.safe_load(file)
    while True:
        now = datetime.datetime.now()
        quiz(training_set, settings)
        print("Good job! You completed the quizz in: ", datetime.datetime.now() - now)
        if input("Play again? ")[0].lower() != "y":
            break
