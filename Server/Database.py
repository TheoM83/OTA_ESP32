import mysql.connector

class Database:

    def __init__(self):
        self.mydb = mysql.connector.connect(user='root', password='MyP4ssMySqL',
                                  host='127.0.0.1',
                                  database='esp32_maintainer')

    def close(self):
        mydb.close()

    def listDevices(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("select id, name, uid from device")
        myresult = mycursor.fetchall()
        return myresult

    def listUpdates(self):
        res = ""
        mycursor = self.mydb.cursor()
        mycursor.execute("select id, device_name, version, server_ip, server_location from update_location GROUP BY device_name ORDER BY device_name, version DESC")
        myresult = mycursor.fetchall()
        return myresult

    def removeUpdate(self, id):
        mycursor = self.mydb.cursor()
        sql = "delete from update_location where id = %s"
        val = ([id])
        mycursor.execute(sql, val)
        self.mydb.commit()
        
    def removeActivityDeviceId(self, id):
        mycursor = self.mydb.cursor()
        sql = "delete from device_activity where id_device = %s"
        val = ([id])
        mycursor.execute(sql, val)
        self.mydb.commit()
        
    def removeDevice(self, id):
        self.removeActivityDeviceId(id)
        mycursor = self.mydb.cursor()
        sql = "delete from device where id = %s"
        val = ([id])
        mycursor.execute(sql, val)
        self.mydb.commit()
        
    def removeActivity(self, id):
        mycursor = self.mydb.cursor()
        sql = "delete from device_activity where id = %s"
        val = ([id])
        mycursor.execute(sql, val)
        self.mydb.commit()
        
    def listActivity(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("select D.name, D.uid, A.ip, A.version, A.activity_date from device_activity A inner join device D ON (D.id= A.id_device) order by activity_date DESC")
        myresult = mycursor.fetchall()
        return myresult       

    def insertDevice(self, uid, deviceName):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO device (name, uid) VALUES (%s, %s)"
        val = (uid, deviceName)
        mycursor.execute(sql, val)
        self.mydb.commit()
        
    def insertUpdate(self, server_ip, server_location, device_name, version, automatic):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO update_location (server_ip, server_location, device_name, version, automatic) VALUES (%s, %s, %s, %s, %s)"
        val = (server_ip, server_location, device_name, version, automatic)
        mycursor.execute(sql, val)
        self.mydb.commit()
        
    def insertActivity(self, id_device, ip, version, activity_date):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO device_activity (id_device, ip, version, activity_date) VALUES (%s, %s, %s, %s)"
        val = (id_device, ip, version, activity_date)
        mycursor.execute(sql, val)
        self.mydb.commit()
        
    def verifyDevice(self, uid, deviceName):
        mycursor = self.mydb.cursor()
        sql = "select id, name, uid from device where name = %s and uid = %s"
        val = (uid, deviceName)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        if (len(myresult) > 0):
            return True
        return False
 

#   EXAMPLE
 
#db = Database()
#db.insertDevice("xxx","xxx")
#db.insertUpdate("127.0.0.1", "/xxx", "xxx", 1.1, False)
#db.insertActivity(1,"127.0.0.1",1, "2000-1-1" )
#print(db.verifyDevice("xxx", "xxx"))
#db.removeUpdate(1)
#db.removeActivity(1)
#db.removeActivityDeviceId(1)
#db.removeDevice(1)
#print(db.listDevices())
#print(db.listUpdates())
#print(db.listActivity())