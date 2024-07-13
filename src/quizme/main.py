"""Code owned by jakob029.

Usage:
- Personal Use: You are free to use, modify, and distribute the software for personal purposes
                  without any obligations, provided there is no capital gain.

- Commercial Use: If you intend to use this software for commercial purposes (including but not
                    limited to integration, customization, or distribution in a commercial
                    product), you are required to compensate the owner. Please contact
                    jakob.eneroth@protonmail.com
"""

import argparse
from src.quizme.cli_interface import run_cli
from src.quizme.gui import GuiInterface
from src.quizme.backend_applications import QuizBackend


def setup_flags():
    """Set up argument flags."""
    parser = argparse.ArgumentParser(prog="OpenQuizz")
    parser.add_argument("-c", "--cli", action="store_true", required=False)

    return parser.parse_args()


def main():
    """Run the program using given flag arguments."""
    args = setup_flags()

    init_quiz_backend = QuizBackend()

    if args.cli:
        run_cli()
    else:
        GuiInterface(init_quiz_backend)


if __name__ == "__main__":
    main()
