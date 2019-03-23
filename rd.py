# Using Android IP Webcam video .jpg stream (tested) in Python2 OpenCV3

import urllib
import cv2
import numpy as np
import time
import subprocess
import urllib
import cam_find
import socket
import bluetooth
# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.43.1:8080/shot.jpg'

def searchitem(): 
    imgResp = urllib.urlopen(url)
    
    # Numpy to convert into a array
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    
    # Finally decode the array to OpenCV usable format ;) 
    img = cv2.imdecode(imgNp,-1)
	
	
	# put the image on screen
    cv2.imshow('IPWebcam',img)
    cv2.imwrite('input.jpg',img)
    #To give the processor some less stress
    #time.sleep(0.1) 

    # Quit if q is pressed
    obj = cam_find.find_object()
    subprocess.call('echo '+obj+'|festival --tts', shell=True)
    time.sleep(2)
    return obj

while True:
    # Use urllib to get the image from the IP camera
    print("waiting for voice command")
    server_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port=1
    server_socket.bind(("",port))
    server_socket.listen(1)
    client_socket,address=server_socket.accept()
    print("connection accepted",address)
    data=client_socket.recv(1024)
    print("received:%s"%data)
    if(data=='search'):
        print("item to search")
        time.sleep(1)
        server_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        port=1
        server_socket.bind(("",port))
        server_socket.listen(1)
        client_socket,address=server_socket.accept()
        print("connection accepted",address)
        data1=client_socket.recv(1024)
        print("received:%s"%data1)
        obj=searchitem()
        print (obj)
    if(obj==data1):
        print("item found")
        subprocess.call(["sudo","espeak","item found"])
    else:
        print("item not found")
        subprocess.call(["sudo","espeak","item not found"])
        
                   
              
