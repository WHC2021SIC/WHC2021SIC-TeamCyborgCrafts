
from time import sleep
from syntacts import *
from ship import Minesweeper, Battleship, Destroyer, Submarine
from grid import Grid, OccupantType
from weapon import Cannon, Laser
from enum import Enum


GAIN = 1
SAMPLE_PERIOD = 1
FREQUENCY = 220


char_mapping_dict = {'1': [0, 1, 1, 0, 0, 0, 0],
                     '2': [1, 1, 0, 1, 1, 0, 1],
                     '3': [1, 1, 1, 1, 0, 0, 1],
                     '4': [0, 1, 1, 0, 0, 1, 1],
                     '5': [1, 0, 1, 1, 0, 1, 1],
                     '6': [1, 0, 1, 1, 1, 1, 1],
                     '7': [1, 1, 1, 0, 0, 0, 0],
                     '8': [1, 1, 1, 1, 1, 1, 1],
                     '9': [1, 1, 1, 0, 0, 1, 1],
                     '0': [1, 1, 1, 1, 1, 1, 0]}


def print_mapping(value):
    if value.isalnum() and value in char_mapping_dict:
        array = char_mapping_dict[value]
        print(" " + str(array[0]) + " ")
        print(str(array[5]) + " " + str(array[1]))
        print(" " + str(array[6]) + " ")
        print(str(array[4]) + " " + str(array[2]))
        print(" " + str(array[3]) + " ")
    else:
        print("Couldn't print: " + str(value))


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
    sequence = base_wave * Envelope(SAMPLE_PERIOD, 1)

    print("Welcome to the Cyborg Crafts' training module - recognizing numbers with your tongue!")
    while 1:
        try:
            usrinput = str(input("Type a number between 0-9 you want to read with your tongue: "))
            usrinput = usrinput.upper()
            print(usrinput)
            if len(usrinput) == 1 and usrinput.isalnum() and usrinput in char_mapping_dict:
                print_mapping(usrinput)
                playable_channels = char_mapping_dict[usrinput]
                for channel in range(len(playable_channels)):
                    if playable_channels[channel]:
                        print("Would play sequence for channel: " + str(channel))
                        s.play(channel, sequence)
                # Wait while sequence plays for SAMPLE_PERIOD seconds
                sleep(sequence.length * .9)
            else:
                print("Couldn't process input: " + str(usrinput))


        except ValueError:
          print("invalid input")
