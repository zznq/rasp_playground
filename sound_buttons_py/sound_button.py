#!/usr/bin/env python

from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

def play_sound(src):
	os.system('mpg321 -q -g 15 ' + src + ' &')

while True:
	if(GPIO.input(23) == False):
		play_sound('lion.mp3')
	if(GPIO.input(24) == False):
		play_sound('golf.mp3')
	if(GPIO.input(25) == False):
		play_sound('vader.mp3')

	sleep(1)
