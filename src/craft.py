from time import sleep
import Adafruit_ADS1x15
from syntacts import *

GAIN = 1
ADC_UPPER_LIMIT = 1300
NUM_CHANNELS = 4
SAMPLE_PERIOD = .25
FREQUENCY = 220

if __name__ == "__main__":
    # Create session instance
    s = Session()
    # Create instance for one of the ADCs
    adc1 = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)
    s.open()

    # Create a base sine wave for motors
    base_wave = Sine(FREQUENCY)

    # Instantiate ADC Readings and Holders for sequences for each one of the channels/sensors
    adc_readings = [0] * NUM_CHANNELS
    sequences = [None] * NUM_CHANNELS
    while True:
        # For each channel get an ADC reading, generate a scale factor, create a sequence, and log data
        for channel in range(NUM_CHANNELS):
            adc_reading = adc1.read_adc(channel, gain=GAIN)
            if adc_reading > ADC_UPPER_LIMIT:
                adc_readings[channel] = ADC_UPPER_LIMIT
            else:
                adc_readings[channel] = adc_reading

            scale_factor = adc_reading/ADC_UPPER_LIMIT
            # Attack, Sustain, Release
            # sequences[channel] = base_wave * ASR(SAMPLE_PERIOD/3, SAMPLE_PERIOD/3, SAMPLE_PERIOD/3, scale_factor)
            # Square envelope
            sequences[channel] = base_wave * Envelope(SAMPLE_PERIOD, scale_factor)
            print("Channel: {}, ADC: {}, Scale Factor: {}, Seq Len: {}".format(channel, adc_reading, scale_factor, sequences[channel].length))

        # Start playing for each channel
        for channel in range(NUM_CHANNELS):
            s.play(channel, sequences[channel])

        # Play until sequence is about over
        sleep(sequences[0].length*.9)
