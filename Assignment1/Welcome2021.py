from karel.stanfordkarel import *

"""
File: Welcome2021.py
--------------------
When you finish writing this file, Karel should be able to place 20 beepers,
then 21 beepers, and end facing East to the right of the 21 beepers.
"""


def main():
    put_beeper_20_times()
    put_beeper_21_times()


def put_beeper_20_times():
    for i in range(20):
        put_beeper()
    move()


def put_beeper_21_times():
    for i in range(21):
        put_beeper()
    move()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('3x3.w')
