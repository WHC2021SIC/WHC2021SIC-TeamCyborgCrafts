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

    print("Welcome to the Cyborg Crafts' training module - recognizing letters with your tongue!")
    while 1:
        try:
            usrinput = int(input("Type a letter between A-Z you want to read with your tongue: "))
            print(usrinput)
        except ValueError:
          print("invalid input")
        continue
        if usrinput == A:
            s.play[0]
        if usrinput == B:
            s.play[1]
        if usrinput == C:
            s.play[2]
        if usrinput == D:
            s.play[3]
        if usrinput == E:
            s.play[4]
        if usrinput == F:
            s.play[5]
        if usrinput == G:
            s.play[6]
        if usrinput == H:
            s.play[7]
        if usrinput == I:
            s.play[8]
        if usrinput == J:
            s.play[9]
        if usrinput == K:
            s.play[10]
        if usrinput == L:
            s.play[11]
        if usrinput == M:
            s.play[12]
        if usrinput == N:
            s.play[13]
        if usrinput == O:
            s.play[14]
        if usrinput == P:
            s.play[15]
        if usrinput == Q:
            s.play[16]
        if usrinput == R:
            s.play[17]
        if usrinput == S:
            s.play[18]
        if usrinput == T:
            s.play[19]
        if usrinput == U:
            s.play[20]
        if usrinput == V:
            s.play[21]
        if usrinput == W:
            s.play[22]
        if usrinput == X:
            s.play[23]
        if usrinput == Y:
            s.play[24]
        if usrinput == Z:
            s.play[25]
        else:
            print("Invalid input")



