# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 21:11:08 2021

@author: hsbbd
"""

import tkinter as tk
from tkinter import ttk
from time import sleep
import syntacts as s 
import os
import Adafruit_ADS1x15
import threading
from PIL import Image, ImageTk

LARGEFONT = ("Verdana", 30)


GAIN = 1
SAMPLE_PERIOD = 1
FREQUENCY = 220
ADC_UPPER_LIMIT = 1300
NUM_CHANNELS = 7
NUM_ADC_CHANNELS = 4
SAMPLE_PERIOD = .25
FREQUENCY = 220
ADC1_ADDR = 0x49
ADC2_ADDR = 0x4B
BUS_NUM = 1

sess = s.Session()

num_mapping_dict = {'1': [0, 1, 1, 0, 0, 0, 0],
                    '2': [1, 1, 0, 1, 1, 0, 1],
                    '3': [1, 1, 1, 1, 0, 0, 1],
                    '4': [0, 1, 1, 0, 0, 1, 1],
                    '5': [1, 0, 1, 1, 0, 1, 1],
                    '6': [1, 0, 1, 1, 1, 1, 1],
                    '7': [1, 1, 1, 0, 0, 0, 0],
                    '8': [1, 1, 1, 1, 1, 1, 1],
                    '9': [1, 1, 1, 0, 0, 1, 1],
                    '0': [1, 1, 1, 1, 1, 1, 0]}

letter_mapping_dict = {'A': [1, 1, 1, 0, 1, 1, 1],
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


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("VTTV")

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Craft, Train, Train1, Train2, Games, Game1, Game2):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Welcome to", font=LARGEFONT)
        label1 = ttk.Label(self, text="VTTV", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        label.grid(row=0, column=0, padx=20, pady=10, columnspan=3)
        label1.grid(row=1, column=0, padx=20, pady=10, columnspan=3)
        button1 = ttk.Button(self, text="Craft",
                             command=lambda: controller.show_frame(Craft))

        # putting the button in its place by
        # using grid
        button1.grid(row=2, column=1, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Train",
                             command=lambda: controller.show_frame(Train))

        # putting the button in its place by
        # using grid
        button2.grid(row=3, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Games",
                             command=lambda: controller.show_frame(Games))

        # putting the button in its place by
        # using grid
        button3.grid(row=4, column=1, padx=10, pady=10)



# second window frame page1
class Craft(tk.Frame):
    def home_handler(self, controller):
        startCraft(False)
        controller.show_frame(StartPage)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #exec(open("craft.py").read())
        label = ttk.Label(self, text ="Craft", font = LARGEFONT)
        label.grid(row = 0, column=0, padx = 90, pady = 10)

                # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Start",
                            command = lambda : startCraft(True))

        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 0, padx = 90, pady = 10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Stop",
                            command = lambda : startCraft(False))

        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 0, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Home",
                            command = lambda : self.home_handler(controller))

        # putting the button in its place by
        # using grid
        button3.grid(row = 3, column = 0, padx = 10, pady = 10)



# third window frame page2
class Train(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text ="Train", font = LARGEFONT)
        label.grid(row = 0, column=0, padx = 90, pady = 10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Numbers",
                             command=lambda: controller.show_frame(Train1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=0, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Letters",
                             command=lambda: controller.show_frame(Train2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=0, padx=10, pady=10)

        button3 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button3.grid(row=3, column=0, padx=10, pady=10)


class Train1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Numbers", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        self.btn = [0 for x in range(9)]

        # for x in range(8):
        #     number = str(x+1);
        #     self.btn[x] = ttk.Button(self, text=number, command = lambda: user_input(number, num_mapping_dict))
        #     self.btn[x].grid(column=x, row=1, padx=10, pady=10)

        button1 = ttk.Button(self, text="1", command=lambda: user_input('1', num_mapping_dict))

        button1.grid(row=1, column=0, padx=10, pady=10)

        button2 = ttk.Button(self, text="2", command=lambda: user_input('2', num_mapping_dict))

        button2.grid(row=1, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="3", command=lambda: user_input('3', num_mapping_dict))

        button3.grid(row=1, column=2, padx=10, pady=10)

        button4 = ttk.Button(self, text="4", command=lambda: user_input('4', num_mapping_dict))

        button4.grid(row=2, column=0, padx=10, pady=10)

        button5 = ttk.Button(self, text="5", command=lambda: user_input('5', num_mapping_dict))

        button5.grid(row=2, column=1, padx=10, pady=10)

        button6 = ttk.Button(self, text="6", command=lambda: user_input('6', num_mapping_dict))

        button6.grid(row=2, column=2, padx=10, pady=10)

        button7 = ttk.Button(self, text="7", command=lambda: user_input('7', num_mapping_dict))

        button7.grid(row=3, column=0, padx=10, pady=10)

        button8 = ttk.Button(self, text="8", command=lambda: user_input('8', num_mapping_dict))

        button8.grid(row=3, column=1, padx=10, pady=10)

        button9 = ttk.Button(self, text="9", command=lambda: user_input('9', num_mapping_dict))

        button9.grid(row=3, column=2, padx=10, pady=10)
        # button to show frame 3 with text
        # layout3
        button10 = ttk.Button(self, text="Home",
                              command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button10.grid(row=4, column=1, padx=10, pady=10)


class Train2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Letters", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)

        letter_var = tk.StringVar()

        letter_entry = tk.Entry(self, textvariable=letter_var, font=('calibre', 10, 'normal'))

        letter_entry.grid(row=1, column=0, padx=10, pady=10)

        button1 = ttk.Button(self, text="Submit",
                             command=lambda: submit())

        button1.grid(row=2, column=0, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=3, column=0, padx=10, pady=10)

        def submit():
            letter = letter_var.get()
            user_input(letter, letter_mapping_dict)


class Games(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Whack a Mole",
                             command=lambda: controller.show_frame(Game1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Simon Vibes",
                             command=lambda: controller.show_frame(Game2))

        # putting the button in its place by
        # using grid
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button3.grid(row=3, column=1, padx=10, pady=10)


class Game1(tk.Frame):

        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        



        label = ttk.Label(self, text="Whack A Mole", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        self.btn = [0 for x in range(9)]

        # for x in range(8):
        #     number = str(x+1);
        #     self.btn[x] = ttk.Button(self, text=number, command = lambda: user_input(number, num_mapping_dict))
        #     self.btn[x].grid(column=x, row=1, padx=10, pady=10)


        button1 = ttk.Button(self, command=lambda:ChangeLabelText(button1))
        button1.grid(row=1, column=0, padx=10, pady=10)

        button2 = ttk.Button(self,command=lambda: user_input('2', num_mapping_dict))

        button2.grid(row=1, column=1, padx=10, pady=10)

        button3 = ttk.Button(self, command=lambda: user_input('3', num_mapping_dict))

        button3.grid(row=1, column=2, padx=10, pady=10)

        button4 = ttk.Button(self, command=lambda: user_input('4', num_mapping_dict))

        button4.grid(row=2, column=0, padx=10, pady=10)

        button5 = ttk.Button(self,  command=lambda: user_input('5', num_mapping_dict))

        button5.grid(row=2, column=1, padx=10, pady=10)

        button6 = ttk.Button(self,  command=lambda: user_input('6', num_mapping_dict))

        button6.grid(row=2, column=2, padx=10, pady=10)

        button7 = ttk.Button(self, command=lambda: user_input('7', num_mapping_dict))

        button7.grid(row=3, column=0, padx=10, pady=10)

        button8 = ttk.Button(self, command=lambda: user_input('8', num_mapping_dict))

        button8.grid(row=3, column=1, padx=10, pady=10)

        button9 = ttk.Button(self, command=lambda: user_input('9', num_mapping_dict))

        button9.grid(row=3, column=2, padx=10, pady=10)
        # button to show frame 3 with text
        # layout3
        button10 = ttk.Button(self, text="Home",
                              command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button10.grid(row=4, column=1, padx=10, pady=10)


class Game2(tk.Frame):
    def __init__(self, parent, controller):
        # Create session instance

        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Simon Vibes", font=LARGEFONT)
        label.grid(row=0, column=0, padx=10, pady=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=1, column=0, padx=10, pady=10)


def print_mapping(value, char_mapping_dict):
    if value.isalnum() and value in char_mapping_dict:
        array = char_mapping_dict[value]
        print(" " + str(array[0]) + " ")
        print(str(array[5]) + " " + str(array[1]))
        print(" " + str(array[6]) + " ")
        print(str(array[4]) + " " + str(array[2]))
        print(" " + str(array[3]) + " ")
    else:
        print("Couldn't print: " + str(value))


def user_input(value, char_mapping_dict):
    global sess
    sess.open()
    # Create a base sine wave for motors
    base_wave = s.Sine(FREQUENCY)
    sequence = base_wave * s.Envelope(SAMPLE_PERIOD, 1)
    # while 1:
    try:
        usrinput = value
        # str(input("Type a number between 0-9 you want to read with your tongue: "))
        usrinput = usrinput.upper()
        print(usrinput)
        if len(usrinput) == 1 and usrinput.isalnum() and usrinput in char_mapping_dict:
            print_mapping(usrinput, char_mapping_dict)
            playable_channels = char_mapping_dict[usrinput]
            for channel in range(len(playable_channels)):
                if playable_channels[channel]:
                    print("Would play sequence for channel: " + str(channel))
                    sess.play(channel, sequence)
            # Wait while sequence plays for SAMPLE_PERIOD seconds
            sleep(sequence.length * .9)
        else:
            print("Couldn't process input: " + str(usrinput))


    except ValueError:
       print("invalid input")
    sess.close()

kill_thread = True
thread = None

def thread_function():

    global kill_thread
    global sess

    # Create instance for one of the ADCs
    adc1 = Adafruit_ADS1x15.ADS1015(address=ADC1_ADDR, busnum=BUS_NUM)
    adc2 = Adafruit_ADS1x15.ADS1015(address=ADC2_ADDR, busnum=BUS_NUM)
    sess.open()

    # Create a base sine wave for motors
    base_wave = s.Sine(FREQUENCY)

    # Instantiate ADC Readings and Holders for sequences for each one of the channels/sensors
    sequences = [None] * NUM_CHANNELS
    while True:
        # For each channel get an ADC reading, generate a scale factor, create a sequence, and log data
        for channel in range(NUM_CHANNELS):
            if channel < NUM_ADC_CHANNELS:
                adc_obj = adc1
                adc_channel = channel
            else:
                adc_obj = adc2
                adc_channel = channel % NUM_ADC_CHANNELS
            adc_reading = adc_obj.read_adc(adc_channel, gain=GAIN)
            if adc_reading > ADC_UPPER_LIMIT:
                adc_reading = ADC_UPPER_LIMIT

            scale_factor = adc_reading/ADC_UPPER_LIMIT
            # Attack, Sustain, Release
            # sequences[channel] = base_wave * ASR(SAMPLE_PERIOD/3, SAMPLE_PERIOD/3, SAMPLE_PERIOD/3, scale_factor)
            # Square envelope
            sequences[channel] = base_wave * s.Envelope(SAMPLE_PERIOD, scale_factor)
            print("Channel: {}, ADC: {}, Scale Factor: {}, Seq Len: {}".format(channel, adc_reading, scale_factor, sequences[channel].length))

        # Start playing for each channel
        for channel in range(NUM_CHANNELS):
            sess.play(channel, sequences[channel])

        # Play until sequence is about over
        sleep(sequences[0].length*.9)

        if kill_thread:
            print("Exiting loop")
            break

    sess.close()
       

def startCraft(play):
    global kill_thread
    global thread
    if play is True:
        print('start')
        kill_thread = False
        thread = threading.Thread(target=thread_function, args=())
        thread.start()
    else:
        print("stop")
        kill_thread = True
        thread.join()




def ChangeLabelText(m):
    m.config(text = 'You pressed the button!')


# Driver Code
app = tkinterApp()
app.mainloop()
