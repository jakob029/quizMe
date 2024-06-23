from cli_interface import run_cli
import argparse
from gui import GuiInterface
from backend_applications import QuizBackend


def setup_flags():
    parser = argparse.ArgumentParser(prog="OpenQuizz")
    parser.add_argument("-c", "--cli", action="store_true", required=False)

    return parser.parse_args()


def main():
    args = setup_flags()

    init_quiz_backend = QuizBackend()

    if args.cli:
        run_cli()
    else:
        GuiInterface(init_quiz_backend)

if __name__ == "__main__":
    main()