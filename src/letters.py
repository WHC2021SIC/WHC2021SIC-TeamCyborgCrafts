
from time import sleep
from syntacts import *



GAIN = 1
SAMPLE_PERIOD = 1
FREQUENCY = 220

char_mapping_dict = {'A': [1, 1, 1, 0, 1, 1, 1],
                     'B': [1, 1, 1, 1, 1, 1, 1],
                     'C': [1, 0, 0, 1, 1, 1, 0],
                     'D': [0, 1, 1, 1, 1, 0, 1],
                     'E': [1, 0, 0, 1, 1, 1, 1],
                     'F': [1, 0, 0, 0, 1, 1, 1],
                     'G': [1, 0, 1, 1, 1, 1, 1],
                     'H': [0, 0, 1, 0, 1, 1, 1],
                     'I': [0, 1, 1, 0, 0, 0, 0],
                     'J': [0, 1, 1, 1, 1, 0, 0],
                     'K': [0, 1, 1, 0, 1, 1, 0],
                     'L': [0, 0, 0, 1, 1, 1, 0],
                     'M': [1, 0, 0, 1, 0, 0, 0],
                     'N': [0, 0, 1, 0, 1, 0, 1],
                     'O': [1, 1, 1, 1, 1, 1, 0],
                     'P': [1, 1, 0, 0, 1, 1, 1],
                     'Q': [1, 1, 1, 0, 0, 1, 1],
                     'R': [0, 0, 0, 0, 1, 0, 1],
                     'S': [1, 0, 1, 1, 0, 1, 1],
                     'T': [0, 0, 0, 1, 1, 1, 1],
                     'U': [0, 1, 1, 1, 1, 1, 0],
                     'V': [0, 1, 0, 1, 0, 1, 0],
                     'W': [1, 0, 0, 1, 0, 0, 1],
                     'X': [0, 1, 1, 0, 1, 1, 0],
                     'Y': [0, 1, 1, 1, 0, 1, 1],
                     'Z': [1, 1, 0, 1, 1, 0, 1]}


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

    print("Welcome to the Cyborg Crafts' training module - recognizing letters with your tongue!")
    while 1:
        try:
            usrinput = str(input("Type a letter between A-Z you want to read with your tongue: "))
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
