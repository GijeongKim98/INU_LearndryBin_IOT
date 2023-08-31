# 버튼을 이용해 블루투스 값 불러오기 

import RPi.GPIO as GPIO
import time
from bluetooth import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(, GPIO.IN)
number = 0

while True:
    value = GPIO.input(24)
    
    if value == True:
        server_socket= BluetoothSocket(RFCOMM)

        port = 1
        server_socket.bind(("", port))
        server_socket.listen(1)

        client_socket, address = server_socket.accept()
        print("Accepted connection from ", address)

        client_socket.send("bluetooth connected!")

        
        data = client_socket.recv(1024)
        data = data.decode('utf-8').rstrip()

        client_socket.close()
        server_socket.close()
        break

f = open("/home/pi/Desktop/id", 'w')

f.write(data)

f.close()







