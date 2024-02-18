import RPi.GPIO as GPIO
import time

# Pin numbers for the LEDs
led_pins = [12, 11, 10, 8, 24, 26, 13, 3]

def setup():
    GPIO.setmode(GPIO.BOARD)
    for pin in led_pins:
        GPIO.setup(pin, GPIO.OUT)


def shift_leds():
    # start blinking from the first led
    for i in range(len(led_pins)):
        GPIO.output(led_pins[i], GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(led_pins[i], GPIO.HIGH)
        
    # start blinking from the last led
    n = 7
    for i in range(len(led_pins)):
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
