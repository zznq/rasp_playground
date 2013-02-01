#!/usr/bin/env python

import RPi.GPIO as GPIO, feedparser, time, config

MAIL_NOTIFICATION_LIMIT = 1
MAIL_CHECK_FREQ = 60

GPIO.setmode(GPIO.BCM)

GREEN_LED = 18
RED_LED = 23

GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

#store username and password in config.py file that is not included in repo
USERNAME = config.USERNAME
PASSWORD = config.PASSWORD

feed_url = "https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom"

hasNew = False

while True:
	parser = feedparser.parse(feed_url)

	newCount = int(parser['feed']['fullcount'])

	hasNew = (newCount >= MAIL_NOTIFICATION_LIMIT)

	print "You have ", newCount, " new emails"
 
	GPIO.output(GREEN_LED, hasNew)
	GPIO.output(RED_LED, not hasNew)

	time.sleep(MAIL_CHECK_FREQ)
