import socket
import os
from time import sleep
from Database import Database
from Device import Device

#connecting to database
print("Connecting to database")
db = Database('root', 'MyP4ssMySqL','127.0.0.1','esp32_maintainer')

#binding and listening on the connection
print("Starting server")
s = socket.socket()         
s.bind(('0.0.0.0', 8090 ))
s.listen(0) 
print("Listening...")

#accepting connection and reading information
client, addr = s.accept()
content = client.recv(32)
content = content.decode("utf-8")
information = content.split("~")
IP = addr[0]

device = Device(information[0],information[1],information[2],IP)
device.setActivity(db)
print(device)

#check if the device is registered on the database
if device.isRegistered(db):
    print(" ->Device Registered")
    
    #check if the device is authorized
    if device.isAuthorized(db):
        print("  ->Device Authorized")

        #check available update
        updateInfo = device.hasUpdate(db)
        if updateInfo[0]:

            #check the version
            if updateInfo[3] > device.Version:
                print("   ->Version "+str(updateInfo[3])+" available")

                #check if it is a local file
                if updateInfo[1] == "127.0.0.1":
                    print("     ->Local upload")
                    f_location = updateInfo[2]
                    file = open(f_location,'rb')
                    size = os.path.getsize(f_location)
                    size = str(size)+'\n'
                    client.send(size.encode())

                    print('Sending', end='')
                    data = file.read(1024)
                    while (data):
                        print(".", sep='', end='', flush=True)
                        client.send(data)
                        data = file.read(1024)
                    file.close()
                    print("\nFirmware sent")
    else:
        print("not authorized")

else:
    device.addDevice(db)
client.close()
