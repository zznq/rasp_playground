#!/usr/bin/env python

import RPi.GPIO as GPIO, feedparser, time

MAIL_NOTIFICATION_LIMIT = 1
MAIL_CHECK_FREQ = 60

GPIO.setmode(GPIO.BCM)

GREEN_LED = 18
RED_LED = 23

GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

USERNAME = "username"
PASSWORD = "password"

feed_url = "https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom"

hasNew = False

while True:
	parser = feedparser.parse(feed_url)

	newCount = int(parser['feed']['fullcount'])

	hasNew = newCount >= MAIL_NOTIFICATION_LIMIT

	print "Has New Mail: ", hasNew
 
	GPIO.output(GREEN_LED, hasNew)
	GPIO.output(RED_LED, not hasNew)

	time.sleep(MAIL_CHECK_FREQ)
