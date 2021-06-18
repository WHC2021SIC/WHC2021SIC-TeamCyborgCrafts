# Player enters placement (row, column, orientation) of ships on their grid
# Player enters attack
from time import sleep
from syntacts import *
from ship import Minesweeper, Battleship, Destroyer, Submarine
from grid import Grid, OccupantType
from weapon import Cannon, Laser
from enum import Enum


GAIN = 1
SAMPLE_PERIOD = .25
FREQUENCY = 220


if __name__ == "__main__":
    """
    Takes and processes user input for number
    :return: number to vibe sequence
    """
    # Create session instance
    s = Session()
    s.open()
    # Create a base sine wave for motors
    base_wave = Sine(FREQUENCY)

    print("Welcome to the Cyborg Crafts' training module - recognizing number with your tongue!")
    while 1:
        try:
            usrinput = int(input("Type a number between 0-9 you want to read with your tongue: "))
            print(usrinput)
        except ValueError:
          print("invalid input")
        continue
        if usrinput == 0:
            s.play[0]
        if usrinput == 1:
            s.play[1]
        if usrinput == 2:
            s.play[2]
        if usrinput == 3:
            s.play[3]
        if usrinput == 4:
            s.play[4]
        if usrinput == 5:
            s.play[5]
        if usrinput == 6:
            s.play[6]
        if usrinput == 7:
            s.play[7]
        if usrinput == 8:
            s.play[8]
        if usrinput == 9:
            s.play[9]
        else:
            print("Invalid input")



