import socket

class Park:

    devices = [];
    
    def load(self):
        return
        
    def append(self, Device):
        self.devices.append(Device)
        
    def filterName(self, Name):
        res = []
        for device in self.devices:
            if device.Name == Name:
                res.append(device)
        return res
            
        
    def filterVersion(self, Version):
        res = []
        for device in self.devices:
            if device.Version == Version:
                res.append(device)
        return res
        
    def __str__(self):
        res = ""
        for device in self.devices:
            res = res + f"{device}\n\r"
        return res
 
class Device:

    def __init__(self, ID, Name, Version, IP):
        self.ID = ID
        self.Name = Name
        self.Version = Version
        self.IP = IP
        
    def verify(self):
        return
        
    def __str__(self):
        return f"ID : {self.ID} ; Name : {self.Name} ; Version : {self.Version} ; Last IP : {self.IP}"


print("Starting server")
s = socket.socket()         
s.bind(('0.0.0.0', 8090 ))
s.listen(0)                 

print("Loading device park")
park = Park()
park.load()

print("Listening...")
content = ""
while True:
    client, addr = s.accept()
    content = client.recv(32)
    content = content.decode("utf-8")
    ID = content
    
    content = client.recv(32)
    content = content.decode("utf-8")
    Name = content
    
    content = client.recv(32)
    content = content.decode("utf-8")
    Version = content
    
    IP = addr[0]
    
    device = Device(ID,Name,Version,IP)
    device.verify()
    
    park.append(device)
    print(park)

print("Closing connection")
client.close()

