#!/usr/bin/python3

# This code waits 10 seconds, then takes a picture and save it with a timestamp.
# The code will then open the picture and check if an April tag has been detected. 
# Environment: Code on raspberry pi 4b+ with raspberry pi camera on board

# Import required libraries
import time, datetime
from picamera2 import Picamera2, Preview
import os, glob
import apriltag
import cv2
import board
import busio
import adafruit_vl6180x


def range_finder():
    # init i2c board i/o
    i2c = busio.I2C(board.SCL, board.SDA)
    # init sensor
    sensor = adafruit_vl6180x.VL6180X(i2c)
    # continuously get range data from sensor and display in terminal every second
    distance_mm = sensor.range
    print("Distance: {0}mm".format(distance_mm))
    time.sleep(1.0)


def take_pic():
    # Setup
    picam = Picamera2()
    config = picam.create_preview_configuration()
    picam.configure(config)
    
    print("[INFO] Loading image view...")
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
    
def detect_apriltag():
    list_files = glob.glob('/home/pi/Documents/pictures/*.png')
    last_file = max(list_files, key=os.path.getctime)

    # load in img and convert to grayscale
    print("[INFO] Loading last image taken")
    #image = cv2.imread(args["image"])
    image = cv2.imread(last_file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # define AprilTag detector options (here for family tag36h11) and detect AprilTag in input image
    print("[INFO] detecting in AprilTags")
    options = apriltag.DetectorOptions(families="tag36h11")
    detector = apriltag.Detector(options)
    results = detector.detect(gray)
    print("[INFO] {} total AprilTags detected".format(len(results)))

    # loop over the AprilTag detection results
    for r in results:
        # extract the bounding box (x, y)-coordinates for the AprilTag
        # and convert each of the (x, y)-coordinate pairs to integers
        (ptA, ptB, ptC, ptD) = r.corners
        ptB = (int(ptB[0]), int(ptB[1]))
        ptC = (int(ptC[0]), int(ptC[1]))
        ptD = (int(ptD[0]), int(ptD[1]))
        ptA = (int(ptA[0]), int(ptA[1]))
        # draw the bounding box of the AprilTag detection
        cv2.line(image, ptA, ptB, (0, 255, 0), 2)
        cv2.line(image, ptB, ptC, (0, 255, 0), 2)
        cv2.line(image, ptC, ptD, (0, 255, 0), 2)
        cv2.line(image, ptD, ptA, (0, 255, 0), 2)
        # draw the center (x, y)-coordinates of the AprilTag
        (cX, cY) = (int(r.center[0]), int(r.center[1]))
        cv2.circle(image, (cX, cY), 5, (0, 0, 255), -1)
        # draw the tag family on the image
        tagFamily = r.tag_family.decode("utf-8")
        cv2.putText(image, tagFamily, (ptA[0], ptA[1] - 15),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        print("[INFO] tag family: {}".format(tagFamily))
        #range_finder()
    # show the output image after AprilTag detection
    range_finder()
    cv2.imshow("Image", image)
    time.sleep(5)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    while True:
        print("[INFO] Starting program")
        take_pic()
        print("[INFO] Picture taken was saved")
        detect_apriltag()