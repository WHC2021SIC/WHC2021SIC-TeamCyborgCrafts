from time import sleep
import Adafruit_ADS1x15
from syntacts import *

GAIN = 1
ADC_UPPER_LIMIT = 1300
NUM_CHANNELS = 7
NUM_ADC_CHANNELS = 4
SAMPLE_PERIOD = .25
FREQUENCY = 220
ADC1_ADDR = 0x49
ADC2_ADDR = 0x4B
BUS_NUM = 1

if __name__ == "__main__":
    # Create session instance
    s = Session()
    # Create instance for one of the ADCs
    adc1 = Adafruit_ADS1x15.ADS1015(address=ADC1_ADDR, busnum=BUS_NUM)
    adc2 = Adafruit_ADS1x15.ADS1015(address=ADC2_ADDR, busnum=BUS_NUM)
    s.open()

    # Create a base sine wave for motors
    base_wave = Sine(FREQUENCY)

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
            sequences[channel] = base_wave * Envelope(SAMPLE_PERIOD, scale_factor)
            print("Channel: {}, ADC: {}, Scale Factor: {}, Seq Len: {}".format(channel, adc_reading, scale_factor, sequences[channel].length))

        # Start playing for each channel
        for channel in range(NUM_CHANNELS):
            s.play(channel, sequences[channel])

        # Play until sequence is about over
        sleep(sequences[0].length*.9)
