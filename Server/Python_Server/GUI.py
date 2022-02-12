from asyncio.windows_events import NULL
import PySimpleGUI as sg
from Database import Database
from decimal import Decimal

db = Database('root', 'MyP4ssMySqL','127.0.0.1','esp32_maintainer')
devices = db.listDevices()
activities = db.listActivity()
updates = db.listUpdates()

window = None

layout1 = []
layout2 = []
layout3 = []

devices_id = []
updates_id = []
visible_device_button = []
visible_updates_button = []

def deleteDevice(id):
    for item in layout1[id+1]:
        item.update(visible=False)
    db.deleteDevice(devices_id[id])

def deleteUpdate(id):
    for item in layout3[id+2]:
        item.update(visible=False)
    db.deleteDevice(updates_id[id])

def unAuthorize(id):
    db.unAutorize(devices_id[id])
    visible_device_button[id].update(visible=False)

def authorize(id):
    db.autorize(devices_id[id])
    visible_device_button[id].update(visible=False)

def activate(id):
    db.setAutomatic(updates_id[id])
    visible_updates_button[id].update(visible=False)

def deActivate(id):
    db.removeAutomatic(updates_id[id])
    visible_updates_button[id].update(visible=False)

def uploadUpdate(Name, Version, Location, Path):
    db.insertUpdate(Location, Path, Name, Decimal(Version), False)

def updateDeviceLayout():
    layout = []
    row1 = []
    row1.append(sg.Text(" ", size=(4, 1)))
    row1.append(sg.Text("Name", size=(15, 1)))
    row1.append(sg.Text("ID", size=(15, 1)))
    row1.append(sg.Text("Authorization", size=(15, 1)))
    layout.append(row1)
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
        layout.append(row2)
    return layout

def updateActivityLayout():
    layout = []
    row1 = []
    row1.append(sg.Text("Time", size=(15, 1)))
    row1.append(sg.Text("Name", size=(15, 1)))
    row1.append(sg.Text("IP", size=(15, 1)))
    row1.append(sg.Text("ID", size=(15, 1)))
    row1.append(sg.Text("Version", size=(15, 1)))
    layout.append(row1)
    for activity in activities:
        row2 = []
        row2.append(sg.Text(str(activity[4]), size=(15, 1)))
        row2.append(sg.Text(str(activity[0]), size=(15, 1)))
        row2.append(sg.Text(str(activity[2]), size=(15, 1)))
        row2.append(sg.Text(str(activity[1]), size=(15, 1)))
        row2.append(sg.Text(str(activity[3]), size=(15, 1)))
        layout.append(row2)
    return layout

def updateUpdateLayout():
    layout = []
    row1 = []
    row1.append(sg.Text(" ", size=(4, 1)))
    row1.append(sg.Text("Name", size=(15, 1), enable_events=True) )
    row1.append(sg.Text("Version", size=(15, 1)))
    row1.append(sg.Text("Location", size=(15, 1)))
    row1.append(sg.Text("Path", size=(15, 1)))
    row1.append(sg.Text("Automatic", size=(15, 1)))
    layout.append(row1)

    row3 = []
    row3.append(sg.Text(" ", size=(4, 1)))
    row3.append(sg.InputText(size=(16, 1),key='-Name-'))
    row3.append(sg.InputText(size=(16, 1),key='-Version-'))
    row3.append(sg.InputText(size=(16, 1),key='-Location-'))
    row3.append(sg.InputText(size=(16, 1),key='-Path-'))
    row3.append(sg.Button('Upload', key="Upload", size=(15, 1)))
    layout.append(row3)

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
        layout.append(row2)

    return layout

layout1=updateDeviceLayout()

layout2=updateActivityLayout()
    
layout3=updateUpdateLayout()

#Define Layout with Tabs         
tabgrp = [[sg.TabGroup([[
    sg.Tab('Devices', layout1, title_color='Red'),
    sg.Tab('Activities', layout2,title_color='Blue'),
    sg.Tab('Updates', layout3,title_color='Black')
    ]], 
    tab_location='centertop',title_color='Black', tab_background_color='White',selected_title_color='Blue',selected_background_color='Grey', border_width=5,size=(700, 550)),sg.Button('REFRESH', size=(10,5))]]  
        
#Define Window
def GUI():
    window =sg.Window("OTA_Insider",tabgrp)
    #Read  values entered by user
    while True:             # Event Loop
        window.refresh()
        event, values = window.Read()
        if event in (None, 'Exit'):
            window.close()    
            break
        if callable(event):
            event()
        elif event[0:6] == 'Remove':
            id = int(event[7:])
            unAuthorize(id)
        elif event[0:3] == 'Add':
            id = int(event[4:])
            authorize(id)
        elif event[0:8] == 'Activate':
            id = int(event[9:])
            activate(id)
        elif event[0:10] == 'Deactivate':
            id = int(event[11:])
            deActivate(id)
        elif event[0:12] == 'DeleteDevice':
            id = int(event[13:])
            deleteDevice(id)
        elif event[0:12] == 'DeleteUpdate':
            id = int(event[13:])
            deleteUpdate(id)
        elif event[0:7] == 'REFRESH':
            window.close()    
            break
        elif event[0:6] == 'Upload':
            uploadUpdate(values['-Name-'],values['-Version-'],values['-Location-'],values['-Path-'])
            
    #access all the values and if selected add them to a string

GUI()