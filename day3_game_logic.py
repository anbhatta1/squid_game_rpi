import RPi.GPIO as GPIO
import time

RED_PIN = 17
GREEN_PIN = 27
BUTTON_PIN = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Game Started!")

try:
    while True:

        # GREEN LIGHT
        print("GREEN LIGHT - You can move!")
        GPIO.output(GREEN_PIN, GPIO.HIGH)
        GPIO.output(RED_PIN, GPIO.LOW)

        time.sleep(3)

        # RED LIGHT
        print("RED LIGHT - Stop!")
        GPIO.output(GREEN_PIN, GPIO.LOW)
        GPIO.output(RED_PIN, GPIO.HIGH)

        time.sleep(3)

except KeyboardInterrupt:
    GPIO.cleanup()