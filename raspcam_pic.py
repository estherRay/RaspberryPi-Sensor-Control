#!/usr/bin/python3

# This code waits 3 seconds, then takes a picture and save it with a timestamp.
# Environment: Code on raspberry pi 4b+ with raspberry pi camera on board

# Import required libraries
import time
import datetime
from picamera2 import Picamera2, Preview
import os

# Setup
picam = Picamera2()
config = picam.create_preview_configuration()
picam.configure(config)

# Open software and start
picam.start_preview(Preview.QTGL)
picam.start()

# After 10 sec, take a picture and save it
time.sleep(3)
# Get timestamp
dt = datetime.datetime.now().strftime("%d.%m.%Y-%H:%M")
# Paths where images are saved
os.chdir("/home/pi/Documents/pictures/")
# image name is timestamp
picam.capture_file(dt + ".png")


# Close program
picam.close()