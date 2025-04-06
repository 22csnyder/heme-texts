#!../.venv/bin/python
##Example usage
# python ./scripts/hw_mrvn.py "Brave, daring, chivalrous, and sometimes a bit reckless."

from dotenv import load_dotenv
import dotenv

dotenv_file = "/Users/christophersnyder/Projects/heme-texts/.env"
load_dotenv(dotenv_path=dotenv_file)

example_student = "Brave, daring, chivalrous, and sometimes a bit reckless."

import marvin
import argparse

parser = argparse.ArgumentParser(description="Classify a student into a Hogwarts house")
parser.add_argument("student", type=str, help="Description of the student")


def ai_hat(student_description):
    house = marvin.classify(
        student_description,
        labels=["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"],
    )
    return house


ai_hat(example_student)


def main(student_description):
    house = ai_hat(student_description)
    return house


if __name__ == "__main__":
    args = parser.parse_args()
    print(main(args.student))
