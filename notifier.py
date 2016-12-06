"""
Author: Rada Berar
Date: 06.December.2016
Simple COM port monitor to display COM port of newly connected devices.

Written for python 2 grammar.
"""

from time import sleep
from os import popen
from balloontip import balloon_tip

title = "COM port change"
message = ""

serial_devices = []

while True:
    message = ""
    for dev_name in serial_devices:
        if dev_name not in response:
            message += '\n' + dev_name + ' removed.'
            serial_devices.remove(dev_name)

    if message != "":
        balloon_tip(title, message)

    message = ""
    response = popen("mode").read()

    for line in response.split('\n'):
        temp = line.split('device')

        if len(temp) > 1:
            if ':' in temp[1]:
                dev_name = temp[1].split(':')[0]
                if 'COM' in dev_name:
                    # valid device name
                    if dev_name not in serial_devices:
                        serial_devices.append(dev_name)
                        message += '\n' + dev_name + ' connected.'

    if message != "":
        balloon_tip(title, message)
    else:
        sleep(1)



























