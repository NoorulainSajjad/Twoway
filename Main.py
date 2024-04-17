import RP1.GPIO as GPIO 3 from time import sleep



red_one = 3


red_two = 11



yellow_one = 5

yellow_two = 13


green_one = 7



green two 15

street lights = 36

GPIO.setmode (GPIO.BOARD)

GPIO.setup(red_one, GPIO.OUT) GPIO.setup(yellow_one, GPIO.OUT)

GPIO.setup(green_one, GPIO.OUT)

GPIO.setup(red_two, GPIO.OUT)

GPIO.setup(yellow_two, GPIO.OUT)

GPIO.setup(green_two, GPIO.OUT)

GPIO.setup(street lights, GPIO.OUT)

GPIO.output(street_lights, True)

while True:
GPIO.output (red_one, True)

GPIO.output (red_two, False)

GPIO.output(green_two, True)
sleep(3)

GPIO.output(red_one, False)

GPIO.output(green_two, False)

GPIO.output(yellow_one, True)

GPIO.output (yellow_two, True)

sleep(1)

GPIO.output(yellow_one, False)

GPIO.output(yellow_two, False)

GPIO.output(red_two, True) GPIO.output(green_one, True)

sleep(3)

GPIO.output(red_two, False)

GPIO.output (green_one, False)

GPIO.output (yellow_one, True)

GPIO.output(yellow_two, True)

sleep(1)

GPIO.output (yellow_one, False) GPIO.output (yellow_two, False)