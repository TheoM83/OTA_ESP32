import os
import socket
import threading
from Device import Device
from Database import Database
from Encryption import Encryption

#PARAMETERS
Database_user = 'root'
Database_password = 'MyP4ssMySqL'
Database_host = '127.0.0.1'
Database_name = 'esp32_maintainer'

AES_key = "0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78, 0x78";

#CODE
enc = Encryption(AES_key)

def acceptClient(client, addr, db):
    try:
        content = client.recv(32)
        content = enc.decrypt(content)
        content = content.decode()
        information = content.split("/")
        information = information[0]
        information = information.split("~")
        IP = addr[0]

        device = Device(information[0],information[1],information[2],IP)
        print(device)

        #check if the device is registered on the database
        if device.isRegistered(db):
            print(" ->Device Registered")
            device.setActivity(db)
            
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
                        if updateInfo[1] == ("127.0.0.1" or "localhost" or "local"):
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
                            print("Remote uploads not available for now !")
                            #Code :)
                    else:
                        print("No update available")
            else:
                print("Not authorized")

        else:
            print("Registering device")
            device.addDevice(db)
    except:
        print("Error")


def Server():

    #connecting to database
    print("Connecting to database")
    db = Database(Database_user, Database_password, Database_host, Database_name)

    #binding and listening on the connection
    print("Starting server")
    s = socket.socket()         
    s.bind(('0.0.0.0', 8090 ))
    s.listen(0) 
    print("Listening...")

    #accepting connection and reading information
    while True :
        client, addr = s.accept()
        threading.Thread(target=acceptClient, args=(client, addr, db)).run()
    
Server()
