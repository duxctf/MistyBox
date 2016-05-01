#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading = True
nState = 0

# Controle tag1 initieer check
from array import *
aTagChk1 = array ('i', [83,74,151,1])
aTagChk2 = array ('i', [103,74,151,1])

def state_zero ( int ):
		if uid[0] == aTagChk1[0] and uid[1] == aTagChk1[1] and uid[2] == aTagChk1[2] and uid[3] == aTagChk1[3]:
			print "match *********************state to 1 ***********************"
			return 1
		return 0


def state_one ( int ):
		if uid[0] == aTagChk2[0] and uid[1] == aTagChk2[1] and uid[2] == aTagChk2[2] and uid[3] == aTagChk2[3]:
			print "match ##############  back to zero **************************************"
			return 0
		return 1

def state_two ( int ):
		if uid[0] == aTagChk2[0] and uid[1] == aTagChk2[1] and uid[2] == aTagChk2[2] and uid[3] == aTagChk2[3]:
			print "match ##############  back to zero **************************************"
			return 0
		return 2

def state_three ( int ):
		if uid[0] == aTagChk2[0] and uid[1] == aTagChk2[1] and uid[2] == aTagChk2[2] and uid[3] == aTagChk2[3]:
			print "match ##############  back to zero **************************************"
			return 0
		return 3


# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
    	
	if nState == 0:
		nState = state_zero(0)
	elif nState == 1:
		nState = state_one(1)

	print "State is "+ str(nState)

        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
        if status == MIFAREReader.MI_OK:
            MIFAREReader.MFRC522_Read(8)
            MIFAREReader.MFRC522_StopCrypto1()
        else:
            print "Authentication error"


