from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""


def main():
    repair_all_damages()


def repair_all_damages():
    # pre: facing east
    while front_is_clear():
        turn_left()
        repair_one_col()
        move_four_steps()
    turn_left()
    repair_one_col()
    # post: facing east


def repair_one_col():
    # pre: facing east
    check_beeper()
    turn_around()
    back_to_first_row()
    turn_left()
    # post: facing east


def check_beeper():
    while front_is_clear():
        place_beeper()
        move()
    place_beeper()


def place_beeper():
    if no_beepers_present():
        put_beeper()


def turn_around():
    for i in range(2):
        turn_left()


def back_to_first_row():
    while front_is_clear():
        move()


def move_four_steps():
    for i in range(4):
        if front_is_clear():
            move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program('SampleQuad1.w')
