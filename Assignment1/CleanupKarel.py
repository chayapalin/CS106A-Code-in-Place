from karel.stanfordkarel import *

"""
File: CleanupKarel.py
--------------------
When you finish writing this file, CleanupKarel should be able to pick up all beepers from the first row of any sized world.
"""


def main():
    clean_up()


def clean_up():
    while front_is_clear():
        safe_pick()
        move()
    safe_pick()


def safe_pick():
    if beepers_present():
        pick_beeper()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('Cleanup1.w')
