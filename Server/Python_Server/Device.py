from datetime import datetime
from decimal import Decimal

class Device:

    def __init__(self, ID, Name, Version, IP):
        self.ID = ID
        self.Name = Name
        self.Version = Decimal(Version)
        self.IP = IP

    def addDevice(self, database):
        database.insertDevice(self.ID, self.Name, False)

    def isRegistered(self, database):
        return database.verifyDevice(self.ID)

    def isAuthorized(self, database):
        return database.isAuthorized(self.Name, self.ID)
        
    def hasUpdate(self, database):
        return database.hasUpdate(self.Name, self.Version)

    def setActivity(self, database):
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        id = database.uidToId(self.ID)
        database.insertActivity(id, self.IP, self.Version, formatted_date)

    def __str__(self):
        return f"ID : {self.ID} ; Name : {self.Name} ; Version : {self.Version} ; Last IP : {self.IP}"