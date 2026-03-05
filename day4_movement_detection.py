import RPi.GPIO as GPIO
import time
import random

RED_PIN = 17
GREEN_PIN = 27
BUTTON_PIN = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Red Light Green Light Game Started")

try:
    while True:

        # GREEN LIGHT
        print("GREEN LIGHT - Move!")
        GPIO.output(GREEN_PIN, GPIO.HIGH)
        GPIO.output(RED_PIN, GPIO.LOW)

        time.sleep(random.randint(2,4))

        # RED LIGHT
        print("RED LIGHT - Don't move!")
        GPIO.output(GREEN_PIN, GPIO.LOW)
        GPIO.output(RED_PIN, GPIO.HIGH)

        start_time = time.time()

        while time.time() - start_time < 3:
            if GPIO.input(BUTTON_PIN) == GPIO.LOW:
                print("Player moved during RED LIGHT! Eliminated!")

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()