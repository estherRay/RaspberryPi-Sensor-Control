#!/usr/bin/python3

# This code enable user to control DC motor. You can drive it clockwise, counter-c, stop it, end signal to it (clean).
# When code starts, you will have those options and need to type in the according key on terminal.
# Once you have pressed a key to drive motor, it will drive for X seconds.

# Author: Esther Rayssiguie

# Import required libraries
import RPi.GPIO as GPIO
import keyboard
import time

#Pins for motor
MotorA = 16
MotorB = 18
MotorE = 22		#Enable signal for motor

def setup():
    # GPIO numbering
    GPIO.setmode(GPIO.BOARD)	#OR GPIO.BSM ???
    # All pins as outputs
    GPIO.output(MotorA,GPIO.OUT)
    GPIO.output(MotorB, GPIO.OUT)
    GPIO.output(MotorE, GPIO.OUT)


def forward():
    #Turning clockwise
    print("Driving Motor Forward")
    GPIO.output(MotorA, GPIO.HIGH)
    GPIO.output(MotorB, GPIO.LOW)
    GPIO.output(MotorE, GPIO.HIGH)	#Enable is on
    
    sleep(2)
    
def backward():
    #Turning counter-clockwise
    print("Driving Motor Backward")
    GPIO.output(MotorA, GPIO.LOW)
    GPIO.output(MotorB, GPIO.HIGH)
    GPIO.output(MotorE, GPIO.HIGH)	#Enable is on
    
    sleep(2)
    
def stop():
    print("Stopping motor")
    GPIO.output(MotorE, GPIO.LOW)	#Enable is off
    
def destroy():
    GPIO.cleanup()
    
if __name__ == '__main__':
    setup()
    print("[INFO] To control the motor, type: 'f' forward; 'b' backward; 's' stop; 'end' end signal")
    
    if keyboard.is_pressed("f"):
        forward()
    if keyboard.is_pressed("b"):
        backward()
    if keyboard.is_pressed("s"):
        stop()
    if keyboard.is_pressed("end"):
        destroy()
    
        