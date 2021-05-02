"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random


def main():
    first_integer = random.randint(MIN_VALUE, MAX_VALUE)
    second_integer = random.randint(MIN_VALUE, MAX_VALUE)
    correct_answer = first_integer + second_integer
    print("What is " + str(first_integer) + " + " + str(second_integer) + "?")

    user_answer = int(input("Your answer: "))

    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Incorrect. The expected answer is", correct_answer)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
