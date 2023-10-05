# RaspberryPi-Sensor-Control
These programs have been implemented on a RaspberryPi 4 b. <br> The Raspberry Pi had two motors, a distance sensor adafruit vl6180x, and a RaspberryPi camera connected to it. <br>

# Gui.py
This code is a GUI interface to control both motors and the adafruit ditance sensor. <br>
You will need a screen to use it. Connect it directly to the raspberry pi or connect remotely to the raspberry pi to visualise the GUI. <br>
Make sure the motors are connected to the right ports defined in the code. <br>
<br>

# TagDetect_Distance.py
This code works with a Raspberry Pi camera and the distance sensor adafruit vl6180x <br>
Every 10 seconds, a picture will be taken with the camera. It is then saved with its timestamp as a name. <br>
The picture will then be open and the code will check if an AprilTag from the family tag36h11 is in the picture. <br>
If an AprilTag has been detected, a bounding box will be created around it and the distance sensor will is activated to see how far the AprilTag is. <br>
The picture with the bounding box will be shown for 5 sec and the distance range will be printed on the terminal. <br>
<br>
Note: A different family of AprilTag can be used. You need to change it in the code (L 64). <br>
<br>

# raspcam_pic.py
This code works with a Raspberry Pi camera. <br>
It will wait 3 seconds then take a picture. <br>
The picture will be saved as its timestamp for a name. <br>
<br>

# vl6180.py
This code works with distance sensor adafruit vl6180x. <br>
It will continuously run the distance sensor every second and print the distance on the terminal. <br>
<br>

# montor_control.py
This code controls a DC motor using a keyboard. <br>
Every move command will take 2 seconds. <br>
<br>
# raspcam_stream.py
This code uses the Raspberry Pi camera to take a video for 10 seconds. <br>
You can stream for longer by modifying L 19.
