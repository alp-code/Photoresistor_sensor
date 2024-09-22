import RPi.GPIO as gpio
import PCF8591 as pcf
import time 

TCpin = 17

def setup(): 
    gpio.setmode(gpio.BCM)
    gpio.setup(TCpin, gpio.IN)
    pcf.setup(0x48)
def loop():
    set_pin = -1
    while True:
        dig_pin = gpio.input(TCpin)
        if dig_pin == 1:
            value = pcf.read(1)
            print('Vrednost:', value)
            set_pin = 1
            time.sleep(1.2)
        elif set_pin != 0 and dig_pin == 0:
            print('Pritisni taster')
            set_pin = 0
def cleanup():
    gpio.cleanup()
 
if __name__ == "__main__":
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        cleanup()