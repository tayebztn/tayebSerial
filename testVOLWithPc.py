#! /usr/bin/python
# File name:

# This file to test the serial communication with the jetson
import serial
import time
#from os import POSIX

from serial.serialutil import STOPBITS_ONE, Timeout

# Setup the serial port
jetsonPort = serial.Serial(
    port='COM6',  # jetson : '/dev/ttyTHSO'
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=0.25,
    # exclusive=True
)

time.sleep(1)   # Wait to initialize

# Make sure to open the port
if not jetsonPort.is_open:
    try:
        jetsonPort.open
    except Exception as exception_error:
        print("Could not open the serial port")
        print("Error: " + str(exception_error))

# Try to send and receive messages
try:
    # flush the port

    # write a message
    rawMessage = "YLD, 12, 23, 34, 45, 56, 67,"
    rawMessage = rawMessage + str(len(rawMessage)) + ('\r\n')
    jetsonPort.write(rawMessage.encode())
    print("Message sent")

    # Listen to incoming messages
    while True:
        if jetsonPort.inWaiting() > 0:
            line = jetsonPort.readline()
            print("Message received")
            print(line)
            break

except Exception as exception_error:
    print("Could not open the serial port")
    print("Error: " + str(exception_error))
