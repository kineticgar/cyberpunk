#!/usr/bin/env python

import glob
import serial
import subprocess
import sys


###########################################################################
# SERIAL_PORT_PREFIX
#
# Append the device number to obtain the serial port path
# (e.g. /dev/ttyACM0).
###########################################################################
SERIAL_PORT_PREFIX = '/dev/ttyACM'
 

###########################################################################
# LEONARDO_SEARCH_STRING
#
# Device is an Arduino Leonardo if the output of GET_DEVICE_PROPS_CMD
# contains this string.
###########################################################################
LEONARDO_SEARCH_STRING = 'Arduino Leonardo'


###########################################################################
# GET_DEVICE_PROPS_CMD
#
# Command to print the device's information.
#
# %s - Device path (e.g. '/dev/ttyACM0')
###########################################################################
GET_DEVICE_PROPS_CMD = 'udevadm info -q all -n %s --attribute-walk'
# https://unix.stackexchange.com/questions/77476/point-usb-phone-to-specific-dev-ttyacm-using-udev


###########################################################################
# main()
#
# Reset all attached Arduino Leonardos by opening and closing their serial
# port.
###########################################################################

def main():
  # Enumerate devices
  devices = glob.glob(SERIAL_PORT_PREFIX + '*')
  for device in devices:
    # Get device information
    deviceInfo = subprocess.check_output(GET_DEVICE_PROPS_CMD % device, shell=True)
    # Check if the device is an Arduino Leonardo
    if LEONARDO_SEARCH_STRING in deviceInfo:
      # Open and close the serial port
      # http://paulswasteland.blogspot.com/2013/04/arduino-leonardo-in-linux-with-arduino.html
      ser = serial.Serial(port=device, \
                          baudrate=1200, \
                          parity=serial.PARITY_NONE, \
                          stopbits=serial.STOPBITS_ONE, \
                          bytesize=serial.EIGHTBITS)
      ser.isOpen()
      ser.close()


if __name__ == '__main__':
  main()

