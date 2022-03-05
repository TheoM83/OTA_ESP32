import PySimpleGUI as sg
from Database import Database
from decimal import Decimal

#PARAMETERS
Database_user = '....'
Database_password = '....'
Database_host = '127.0.0.1'
Database_name = 'esp32_maintainer'

#CODE

def deleteDevice(db, id, devices_id,layout1):
    for item in layout1[id+1]:
        item.update(visible=False)
    db.removeDevice(devices_id[id])

def deleteUpdate(db, id,updates_id, layout3):
    for item in layout3[id+2]:
        item.update(visible=False)
    db.removeUpdate(updates_id[id])

def unAuthorize(db, id, devices_id, visible_device_button):
    db.unAutorize(devices_id[id])
    visible_device_button[id].update(visible=False)

def authorize(db, id, devices_id,visible_device_button):
    db.autorize(devices_id[id])
    visible_device_button[id].update(visible=False)

def activate(db, id, updates_id,visible_updates_button):
    db.setAutomatic(updates_id[id])
    visible_updates_button[id].update(visible=False)

def deActivate(db, id, updates_id, visible_updates_button):
    db.removeAutomatic(updates_id[id])
    visible_updates_button[id].update(visible=False)

def uploadUpdate(db, Name, Version, Location, Path):
    db.insertUpdate(Location, Path, Name, Decimal(Version), False)

def updateDeviceLayout(devices, devices_id, visible_device_button):
    column = []
    layout = []
    row1 = []
    row1.append(sg.Text(" ", size=(4, 1)))
    row1.append(sg.Text("Name", size=(15, 1)))
    row1.append(sg.Text("ID", size=(15, 1)))
    row1.append(sg.Text("Authorization", size=(15, 1)))
    column.append(row1)
    i = -1
    for device in devices:
        i = i+1
        devices_id.append(device[0])
        row2 = []
        row2.append(sg.Button('X', key="DeleteDevice-"+str(i), size=(3, 1)))
        row2.append(sg.Text(str(device[1]), size=(15, 1)))
        row2.append(sg.Text(str(device[2]), size=(15, 1)))
        if device[3] == True:
            visible_device_button.append(sg.Button('Remove', key="Remove-"+str(i), size=(15, 1)))
            row2.append(visible_device_button[i])
        else:
            visible_device_button.append(sg.Button('Add', key="Add-"+str(i), size=(15, 1)))
            row2.append(visible_device_button[i])
        column.append(row2)
    layout = [[
        sg.Column(column, scrollable=True,  vertical_scroll_only=True, size=(800, 600)),
    ]]
    return layout, column

def updateActivityLayout(activities):
    column = []
    row1 = []
    row1.append(sg.Text("Time", size=(15, 1)))
    row1.append(sg.Text("Name", size=(15, 1)))
    row1.append(sg.Text("IP", size=(15, 1)))
    row1.append(sg.Text("ID", size=(15, 1)))
    row1.append(sg.Text("Version", size=(15, 1)))
    column.append(row1)
    for activity in activities:
        row2 = []
        row2.append(sg.Text(str(activity[4]), size=(15, 1)))
        row2.append(sg.Text(str(activity[0]), size=(15, 1)))
        row2.append(sg.Text(str(activity[2]), size=(15, 1)))
        row2.append(sg.Text(str(activity[1]), size=(15, 1)))
        row2.append(sg.Text(str(activity[3]), size=(15, 1)))
        column.append(row2)

    layout = [[
        sg.Column(column, scrollable=True,  vertical_scroll_only=True, size=(800, 600)),
    ]]
    return layout, column

def updateUpdateLayout(updates, updates_id, visible_updates_button):
    column = []
    row1 = []
    row1.append(sg.Text(" ", size=(4, 1)))
    row1.append(sg.Text("Name", size=(15, 1), enable_events=True) )
    row1.append(sg.Text("Version", size=(15, 1)))
    row1.append(sg.Text("Location", size=(15, 1)))
    row1.append(sg.Text("Path", size=(15, 1)))
    row1.append(sg.Text("Automatic", size=(15, 1)))
    column.append(row1)

    row3 = []
    row3.append(sg.Text(" ", size=(4, 1)))
    row3.append(sg.InputText(size=(16, 1),key='-Name-'))
    row3.append(sg.InputText(size=(16, 1),key='-Version-'))
    row3.append(sg.InputText(size=(16, 1),key='-Location-'))
    row3.append(sg.InputText(size=(16, 1),key='-Path-'))
    row3.append(sg.Button('Upload', key="Upload", size=(15, 1)))
    column.append(row3)

    i = -1
    for update in updates:
        i = i+1
        row2 = []
        updates_id.append(update[0])
        row2.append(sg.Button('X', key="DeleteUpdate-"+str(i), size=(3, 1)))
        row2.append(sg.Text(str(update[1]), size=(15, 1)))
        row2.append(sg.Text(str(update[2]), size=(15, 1)))
        row2.append(sg.Text(str(update[3]), size=(15, 1)))
        row2.append(sg.Text(str(update[4]), size=(15, 1)))
        if update[5] == True:
            visible_updates_button.append(sg.Button('Deactivate', key="Deactivate-"+str(i), size=(15, 1)))
            row2.append(visible_updates_button[i])
        else:
            visible_updates_button.append(sg.Button('Activate', key="Activate-"+str(i), size=(15, 1)))
            row2.append(visible_updates_button[i])
        column.append(row2)
    layout = [[
        sg.Column(column, scrollable=True,  vertical_scroll_only=True, size=(800, 600)),
    ]]
    return layout, column
    
#Define Window
def GUI():

    db = Database(Database_user, Database_password, Database_host, Database_name)
    devices = db.listDevices()
    activities = db.listActivity()
    updates = db.listUpdates()

    devices_id = []
    updates_id = []
    visible_device_button = []
    visible_updates_button = []

    layout1 = []
    layout2 = []
    layout3 = []
    layout0 = [[
        sg.Text("Welcome\n \n")
    ]]

    layout1=updateDeviceLayout(devices, devices_id, visible_device_button)

    layout2=updateActivityLayout(activities)
        
    layout3=updateUpdateLayout(updates, updates_id,visible_updates_button )

    #Define Layout with Tabs         
    tabgrp = [[sg.TabGroup([[
    sg.Tab('Home', layout0),
    sg.Tab('Devices', layout1[0]),
    sg.Tab('Activities', layout2[0]),
    sg.Tab('Updates', layout3[0])
    ]], 
    tab_location='centertop',title_color='Black', tab_background_color='White',selected_title_color='Blue',selected_background_color='Grey', border_width=5,size=(800, 600)),sg.Button('REFRESH', size=(10,5))]]  
    
    window =sg.Window("OTA_Insider",tabgrp)
    #Read  values entered by user
    while True:             # Event Loop
        window.refresh()
        event, values = window.Read()
        if event in (None, 'Exit'):
            window.close()    
            return 1
        if callable(event):
            event()
        elif event[0:6] == 'Remove':
            id = int(event[7:])
            unAuthorize(db,id, devices_id, visible_device_button)
        elif event[0:3] == 'Add':
            id = int(event[4:])
            authorize(db,id,devices_id, visible_device_button)
        elif event[0:8] == 'Activate':
            id = int(event[9:])
            activate(db,id, updates_id, visible_updates_button)
        elif event[0:10] == 'Deactivate':
            id = int(event[11:])
            deActivate(db, id,updates_id, visible_updates_button)
        elif event[0:12] == 'DeleteDevice':
            id = int(event[13:])
            deleteDevice(db,id,devices_id, layout1[1])
        elif event[0:12] == 'DeleteUpdate':
            id = int(event[13:])
            deleteUpdate(db,id,updates_id, layout3[1])
        elif event[0:7] == 'REFRESH':
            window.close()  
            return 2
        elif event[0:6] == 'Upload':
            try:
                uploadUpdate(db, values['-Name-'],values['-Version-'],values['-Location-'],values['-Path-'])
            except:
                sg.Popup('You have made a mistake in your update', title='Error')

            
    #access all the values and if selected add them to a string

res = GUI()
while res == 2:
    res = GUI()