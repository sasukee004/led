import RPi.GPIO as GPIO
import time

LedPin = 40  # pin 40
GPIO.setmode(GPIO.BOARD)  # Numbers pins by physical location
GPIO.setup(LedPin, GPIO.OUT)  # Set pin mode as output

# Set the LED to off initially
GPIO.output(LedPin, GPIO.HIGH)

try:
    while True:
        print('...led on')
        GPIO.output(LedPin, GPIO.LOW)  # LED on
        time.sleep(0.5)
        
        print('led off...')
        GPIO.output(LedPin, GPIO.HIGH)  # LED off
        time.sleep(0.5)

except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the following code will be executed.
    GPIO.output(LedPin, GPIO.HIGH)  # LED off
    GPIO.cleanup()
