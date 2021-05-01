from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""


def main():
    move_and_pickup()
    put_piece()
    return_to_the_position()


def move_and_pickup():
    move()
    move()
    pick_beeper()


def put_piece():
    move()
    turn_left()
    move()
    move()
    put_beeper()


def return_to_the_position():
    turn_around()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    turn_around()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('Puzzle.w')
