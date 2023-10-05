#!/usr/bin/python3

# This code records a video for 10 seconds then save it.
# Environment: Code on raspberry pi 4b+ with raspberry pi camera on board

# Import required libraries
import time
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder

# Setup
picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)
encoder = H264Encoder(10000000) # video coding format

# Stard recording, it will record for 10 seconds, save the video, and then stop this code
picam2.start_recording(encoder, 'test.h264')
time.sleep(10)
picam2.stop_recording()