#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading = True
nState = 0

# Controle tag1 initieer check
from array import *
aTagChkDogA = array ('i', [83,74,151,1])
aTagChkDogB = array ('i', [103,74,151,1])
aTagChkRoomA = array ('i', [19,74,151,1])
aTagChkRoomB = array ('i', [103,20,151,1])
aTagChkPatchWorkA = array ('i', [99,74,151,1])
aTagChkPatchWorkB = array ('i', [103,20,12,1])

def state_zero ( int ):
		if uid[0] == aTagChkDogA[0] and uid[1] == aTagChkDogA[1] and uid[2] == aTagChkDogA[2] and uid[3] == aTagChkDogA[3]:
			print "match *********************state to 1: Dog A identified ***********************"
			return 1
		if uid[0] == aTagChkDogB[0] and uid[1] == aTagChkDogB[1] and uid[2] == aTagChkDogB[2] and uid[3] == aTagChkDogB[3]:
			print "match *********************state to 5: Dog B identified ***********************"
			return 5
		return 0

def state_one ( int ):
		if uid[0] == aTagChkRoomA[0] and uid[1] == aTagChkRoomA[1] and uid[2] == aTagChkRoomA[2] and uid[3] == aTagChkRoomA[3]:
			print "match *********************state to 2: Room A identified ***********************"
			return 2
		if uid[0] == aTagChkRoomB[0] and uid[1] == aTagChkRoomB[1] and uid[2] == aTagChkRoomB[2] and uid[3] == aTagChkRoomB[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkDogB[0] and uid[1] == aTagChkDogB[1] and uid[2] == aTagChkDogB[2] and uid[3] == aTagChkDogB[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkPatchWorkB[0] and uid[1] == aTagChkPatchWorkB[1] and uid[2] == aTagChkPatchWorkB[2] and uid[3] == aTagChkPatchWorkB[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkPatchWorkA[0] and uid[1] == aTagChkPatchWorkA[1] and uid[2] == aTagChkPatchWorkA[2] and uid[3] == aTagChkPatchWorkA[3]:
			print "match ##############  back to zero **************************************"
			return 0
		return 1

def state_two ( int ):
		if uid[0] == aTagChkPatchWorkA[0] and uid[1] == aTagChkPatchWorkA[1] and uid[2] == aTagChkPatchWorkA[2] and uid[3] == aTagChkPatchWorkA[3]:
			print "match *********************state to 3: Show the Flag A ***********************"
			return 3
		if uid[0] == aTagChkRoomB[0] and uid[1] == aTagChkRoomB[1] and uid[2] == aTagChkRoomB[2] and uid[3] == aTagChkRoomB[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkRoomA[0] and uid[1] == aTagChkRoomA[1] and uid[2] == aTagChkRoomA[2] and uid[3] == aTagChkRoomA[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkDogB[0] and uid[1] == aTagChkDogB[1] and uid[2] == aTagChkDogB[2] and uid[3] == aTagChkDogB[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkDogA[0] and uid[1] == aTagChkDogA[1] and uid[2] == aTagChkDogA[2] and uid[3] == aTagChkDogA[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkPatchWorkB[0] and uid[1] == aTagChkPatchWorkB[1] and uid[2] == aTagChkPatchWorkB[2] and uid[3] == aTagChkPatchWorkB[3]:
			print "match ##############  back to zero **************************************"
			return 0
		return 2

def state_three ( int ):
		if uid[0] == aTagChkPatchWorkA[0] and uid[1] == aTagChkPatchWorkA[1] and uid[2] == aTagChkPatchWorkA[2] and uid[3] == aTagChkPatchWorkA[3]:
			print "@@@@@@@@@@@@@@@@@@@@@  SHOW FLAG A @@@@@@@@@@@@@@@@@@@@@"
			return 3
		if uid[0] == aTagChkRoomB[0] and uid[1] == aTagChkRoomB[1] and uid[2] == aTagChkRoomB[2] and uid[3] == aTagChkRoomB[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkRoomA[0] and uid[1] == aTagChkRoomA[1] and uid[2] == aTagChkRoomA[2] and uid[3] == aTagChkRoomA[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkDogB[0] and uid[1] == aTagChkDogB[1] and uid[2] == aTagChkDogB[2] and uid[3] == aTagChkDogB[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkDogA[0] and uid[1] == aTagChkDogA[1] and uid[2] == aTagChkDogA[2] and uid[3] == aTagChkDogA[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkPatchWorkB[0] and uid[1] == aTagChkPatchWorkB[1] and uid[2] == aTagChkPatchWorkB[2] and uid[3] == aTagChkPatchWorkB[3]:
			print "match ##############  back to zero **************************************"
			return 0
		return 0

def state_five ( int ):
		if uid[0] == aTagChkRoomB[0] and uid[1] == aTagChkRoomB[1] and uid[2] == aTagChkRoomB[2] and uid[3] == aTagChkRoomB[3]:
			print "match *********************state to 6: Room B identified ***********************"
			return 6
		if uid[0] == aTagChkRoomA[0] and uid[1] == aTagChkRoomA[1] and uid[2] == aTagChkRoomA[2] and uid[3] == aTagChkRoomA[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkDogA[0] and uid[1] == aTagChkDogA[1] and uid[2] == aTagChkDogA[2] and uid[3] == aTagChkDogA[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkPatchWorkB[0] and uid[1] == aTagChkPatchWorkB[1] and uid[2] == aTagChkPatchWorkB[2] and uid[3] == aTagChkPatchWorkB[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkPatchWorkA[0] and uid[1] == aTagChkPatchWorkA[1] and uid[2] == aTagChkPatchWorkA[2] and uid[3] == aTagChkPatchWorkA[3]:
			print "match ##############  back to zero **************************************"
			return 0
		return 5

def state_six ( int ):
		if uid[0] == aTagChkPatchWorkB[0] and uid[1] == aTagChkPatchWorkB[1] and uid[2] == aTagChkPatchWorkB[2] and uid[3] == aTagChkPatchWorkB[3]:
			print "match *********************state to 7: Show the Flag B ***********************"
			return 7
		if uid[0] == aTagChkRoomB[0] and uid[1] == aTagChkRoomB[1] and uid[2] == aTagChkRoomB[2] and uid[3] == aTagChkRoomB[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkRoomA[0] and uid[1] == aTagChkRoomA[1] and uid[2] == aTagChkRoomA[2] and uid[3] == aTagChkRoomA[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkDogB[0] and uid[1] == aTagChkDogB[1] and uid[2] == aTagChkDogB[2] and uid[3] == aTagChkDogB[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkDogA[0] and uid[1] == aTagChkDogA[1] and uid[2] == aTagChkDogA[2] and uid[3] == aTagChkDogA[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkPatchWorkA[0] and uid[1] == aTagChkPatchWorkA[1] and uid[2] == aTagChkPatchWorkA[2] and uid[3] == aTagChkPatchWorkA[3]:
			print "match ##############  back to zero **************************************"
			return 0
		return 6

def state_seven ( int ):
		if uid[0] == aTagChkPatchWorkB[0] and uid[1] == aTagChkPatchWorkB[1] and uid[2] == aTagChkPatchWorkB[2] and uid[3] == aTagChkPatchWorkB[3]:
			print "@@@@@@@@@@@@@@@@@@@@@  SHOW FLAG B @@@@@@@@@@@@@@@@@@@@@"
			return 7
		if uid[0] == aTagChkRoomB[0] and uid[1] == aTagChkRoomB[1] and uid[2] == aTagChkRoomB[2] and uid[3] == aTagChkRoomB[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkRoomA[0] and uid[1] == aTagChkRoomA[1] and uid[2] == aTagChkRoomA[2] and uid[3] == aTagChkRoomA[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkDogB[0] and uid[1] == aTagChkDogB[1] and uid[2] == aTagChkDogB[2] and uid[3] == aTagChkDogB[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkDogA[0] and uid[1] == aTagChkDogA[1] and uid[2] == aTagChkDogA[2] and uid[3] == aTagChkDogA[3]:
			print "match ##############  back to zero **************************************"
			return 0
		if uid[0] == aTagChkPatchWorkA[0] and uid[1] == aTagChkPatchWorkA[1] and uid[2] == aTagChkPatchWorkA[2] and uid[3] == aTagChkPatchWorkA[3]:
			print "match ##############  back to zero **************************************"
			return 0
		return 0


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
	elif nState == 2:
		nState = state_two(2)
	elif nState == 3:
		nState = state_three(3)
	elif nState == 5:
		nState = state_five(5)
	elif nState == 6:
		nState = state_six(6)
	elif nState == 7:
		nState = state_seven(7)

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


