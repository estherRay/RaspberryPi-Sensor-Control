#!/usr/bin/python3

# This code prints on the terminal the distance the
#    distance sensor is measuring every second.
#
# Environment: code on raspberry pi 4b+, specific to sensor vl6180x adafruit.
# Connection from sensor to raspberry pi:
#		VIN : 1  3.3V DC power
#		GND : 9  Ground
#		SCL : 5  SDL
#		SDA : 3  SDA
# Author: Esther Rayssiguie

# Import required libraries
import time
import board
import busio
import adafruit_vl6180x

# init i2c board i/o
i2c = busio.I2C(board.SCL, board.SDA)
# init sensor
sensor = adafruit_vl6180x.VL6180X(i2c)

def range_finder():
    # continuously get range data from sensor and display in terminal every second
    distance_mm = sensor.range
    print("Distance: {0}mm".format(distance_mm))
    time.sleep(1.0)
    
if __name__ == '__main__':
    while True:
        range_finder()