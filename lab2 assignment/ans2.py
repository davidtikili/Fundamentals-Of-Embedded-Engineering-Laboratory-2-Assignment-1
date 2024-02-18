import RPi.GPIO as GPIO
import time

# Pin numbers for the LEDs
led_pins1 = [12, 11, 13, 3, 10, 26, 8, 24 ]

led_pins = [[12, 3], [11, 13], [10, 26], [8, 24]]
def setup():
    GPIO.setmode(GPIO.BOARD)
    for pin in led_pins1:
        GPIO.setup(pin, GPIO.OUT)


def shift_leds():
    # start blinking from the last two leds
    for i in range (len(led_pins)):

        GPIO.output(led_pins[i], GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_pins[i], GPIO.HIGH)

    # Continue blinking from midlle two leds
    n = 3
    for i in range (4):
        while n >= 0:

            GPIO.output(led_pins[n], GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(led_pins[n], GPIO.HIGH)
            n -= 1
    
    

def main():
    try:
        setup()
        while True:
           
            # Shift LEDs back and forth
            shift_leds()

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
