#!/usr/bin/env python

# imports
import pysnmp
import paramiko
import sys
import telnetlib
import time

# varsDEVICE_IP
CON_TIMEOUT = 10
DEVICE_NAME = 'pynet-rtr1'
DEVICE_IP = '184.105.247.70'
DEVICE_PORT = 23
DEVICE_USER_PROMPT = 'Username'
DEVICE_USER = 'pyclass'
DEVICE_PASSWORD_PROMPT = 'Password'
DEVICE_PASSWORD = '88newclass'
COMMAND_PROMPT = '#'
COMMAND = 'show ip int brief'

# connect
device_connection = telnetlib.Telnet(DEVICE_IP,DEVICE_PORT,CON_TIMEOUT)
device_connection.read_until(DEVICE_USER_PROMPT)
time.sleep(1)
device_connection.write(DEVICE_USER + '\n')
device_output = device_connection.read_very_eager()
device_connection.read_until(DEVICE_PASSWORD_PROMPT)
time.sleep(1)
device_connection.write(DEVICE_PASSWORD + '\n')
device_output = device_connection.unti(COMMAND_PROMPT)

# execute command
device_output = device_connection.read_very_eager()
device_connection.write(COMMAND + '\n')
device_output = device_connection.unti(COMMAND_PROMPT)

# close connection
device_connection.close()

# output results of command
print device_output

