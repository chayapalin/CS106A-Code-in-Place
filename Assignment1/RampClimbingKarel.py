from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""


def main():
    draw_diagonal_line()


def draw_diagonal_line():
    # pre: facing east
    while front_is_clear():
        put_beeper()
        move_up()
        move_forward()
    # post: facing east
    # fencepost
    put_beeper()


def move_up():
    # pre: facing east
    turn_left()
    move()
    turn_right()
    # post: facing east


def turn_right():
    for i in range(3):
        turn_left()


def move_forward():
    # pre: facing east
    for i in range(2):
        move()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('RampKarel1.w')
