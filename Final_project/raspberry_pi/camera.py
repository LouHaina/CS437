from picamera import PiCamera
import time
import serial
import os

val=""

camera = PiCamera()
camera.rotation = 180 
camera.resolution=(1920,1080)

bluetoothSerial = serial.Serial( "/dev/rfcomm0", baudrate=9600 )  
print("Waiting on data from Arduino: ")
try:
    while True:
        RXData = (bluetoothSerial.readline()).strip().decode("utf-8") 
        val= RXData
        if val=="1":
            camera.start_preview()
            time.sleep(2)
            camera.capture("/home/pi/Desktop/final_project/picture/CarPicture.jpg") 
            camera.stop_preview() 

        if RXData=="quit": 
            n=False

        else:
            print (RXData) 
                
except:
      print("Bluetooth Device Disconnected") 