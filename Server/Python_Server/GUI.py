import socket
import os
import PySimpleGUI as sg
from time import sleep
from Database import Database
from Device import Device

#connecting to database
db = Database('root', 'MyP4ssMySqL','127.0.0.1','esp32_maintainer')

devices = db.listDevices()
activities = db.listActivity()
updates = db.listUpdates()

def test(x):
    print(x)

#define layout
layout1 = []
key = -1
for device in devices:
    key = key + 1
    row = []
    row.append(sg.Text(str(device[1])))
    row.append(sg.Text(str(device[2])))
    if device[3] == True:
        row.append(sg.Text("Authorized"))
        row.append(sg.Button('Remove'))
    else:
        row.append(sg.Text("Not Authorized"))
        row.append(sg.Button('Add'))
    layout1.append(row)

layout2=[]
for activity in activities:
    layout2.append([sg.Text(str(activity))])
layout3= []
for update in updates : 
    layout3.append([sg.Text(str(update))])

#Define Layout with Tabs         
tabgrp = [[sg.TabGroup([[
    sg.Tab('Devices', layout1, title_color='Red'),
    sg.Tab('Activities', layout2,title_color='Blue'),
    sg.Tab('Updates', layout3,title_color='Black')
    ]], 
    tab_location='centertop',title_color='Black', tab_background_color='White',selected_title_color='Blue',selected_background_color='Grey', border_width=5), 
    sg.Button('Close')]]  
        
#Define Window
window =sg.Window("OTA_Insider",tabgrp)
#Read  values entered by user
while True:             # Event Loop
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    if callable(event):
        event()
    if event == 'Remove':
        print(device[1])
#access all the values and if selected add them to a string
window.close()    