# This code is a GUI interface to control 2 motors and an adafruit ditance sensor
# You will need a screen to use it. Connect it directly to the raspberry pi or connect remotely to the raspberry pi to visualise the GUI.
# Environment: tested on a Raspberry Pi 4
# Sensors used: motors, distance sensor adafruit
# Make sure the motors are connected to the right ports

import tkinter as tk
import RPi.GPIO as GPIO
from time import sleep
import busio
import board
import adafruit_vl6180x

# Initialise the motors ###########
#Pin for interface motor
Motor1A = 16
Motor1B = 18
Motor1E = 22
#Pin for gripper motor
Motor2G = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# All pins as outputs
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)
GPIO.setup(Motor2G, GPIO.OUT)

# Init GUI
panel = tk.Tk()
panel.title("Motors Control and Distance Sensor")
panel.geometry("450x170")
    
# MOTOR INTERFACE FUNCTIONS ########   
#Turning clockwise
def forward():
    print("[INFO] Driving Motor Forward")
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)	#Enable is on
    sleep(2)
    
#Turning counter-clockwise
def backward():
    print("[INFO] Driving Motor Backward")
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)	#Enable is on
    sleep(2)

# Stop Motor 
def stop():
    print("[INFO] Stopping Motor")
    GPIO.output(Motor1E, GPIO.LOW)	#Enable is off
    sleep(2)
    
# GRIPPER FUNCTIONS ########
# Open gripper
def open_grip():
    pwm=GPIO.PWM(Motor2G, 50)
    print("[INFO] Opening Gripper")
    pwm.start(1)
    pwm.ChangeDutyCycle(6.5)
    sleep(0.2)

# Close gripper
def close_grip():
    pwm=GPIO.PWM(Motor2G, 50)
    print("[INFO] Closing Gripper")
    pwm.start(1)
    pwm.ChangeDutyCycle(7.5)
    sleep(0.5)

def stop_grip():
    print("[INFO] Stoping Gripper")
    pwm=GPIO.PWM(Motor2G, 50)
    pwm.stop()
    
# DISTANCE SENSOR ########
def range_finder():
    # init i2c board i/o
    i2c = busio.I2C(board.SCL, board.SDA)
    # init sensor
    sensor = adafruit_vl6180x.VL6180X(i2c)
    # continuously get range data from sensor and display in terminal every second
    distance_mm = sensor.range
    print("Distance: {0}mm".format(distance_mm))

# DESTROY GPIO ########
def destroy_all():
    print("[INFO] EXIT")
    GPIO.cleanup()
    sleep(0.5)
    panel.destroy()
    
# Create interface ########
# Motor interface buttons
open_btn = tk.Button(panel, text="Open Motor", command=forward)
open_btn.grid(row=2, column=0)
close_btn = tk.Button(panel, text="Close Motor", command=backward)
close_btn.grid(row=4, column=0)
stop_btn = tk.Button(panel, text="Stop Motor", command=stop)
stop_btn.grid(row=6, column=0)

# Gripper buttons
open_grip_btn = tk.Button(panel, text="Open Gripper", command=open_grip)
open_grip_btn.grid(row=2, column=2)
close_grip_btn = tk.Button(panel, text="Close Gripper", command=close_grip)
close_grip_btn.grid(row=4, column=2)
stop_grip_btn = tk.Button(panel, text="Stop Gripper", command=stop_grip)
stop_grip_btn.grid(row=6, column=2)

# Distance button
distance_btn = tk.Button(panel, text="Get Distance", command=range_finder)
distance_btn.grid(row=0, column=1)

# Destroy and exit button
exit_btn = tk.Button(panel, text="Destroy GPIO signal and EXIT", command=destroy_all)
exit_btn.grid(row=8, column=1)
    
    
