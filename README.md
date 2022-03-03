# OTA_ESP32

Creating a secure ESP32 OTA update manager and bootloader based on a Python server, MySQL and using TCP connections to communicate with the device

## Goal :
  - The GUI is easy to use and intuitive
  - The system is easy to set up and secure
  - The code is easy, coder-friendly, made to be upgraded

## Prerequisites :
  - Arduino IDE with the Crypto library
  - Python3 (with *mysql-connector-python*, *pysimplegui* and *pycryptodome*)
  - MYSQL server
  
## How to use :
  - Clone the project
  - Import the MYSQL database
  - Modify the Python Server.py and GUI.py parameters depending on your Mysql database authentification and execute them.
  - Modify the ESP32 parameters depending the device and networking informations you want and upload the code on your device
  - On the GUI, authorize the devices you want, add the updates and activate them.
  
## Known bugs :
  - Memory corruption can occur.

## Known vulnerabilities :
  - The binary update is not encrypted
  - The encrypted identification can be heard and repeated on another device