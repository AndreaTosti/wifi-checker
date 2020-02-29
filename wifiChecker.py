import os
from time import sleep

# netsh wlan show profile
# netsh wlan show interfaces

SSID = "ssid"
NAME = "name"
INTERFACE = "interface"

# How frequently to check if wifi is down. In seconds
FREQUENCY = 4

def enable():
    connectStr = "netsh wlan connect ssid=%s name=%s interface=%s" % (SSID,NAME,INTERFACE)
    os.system(connectStr)

def disable():
    os.system("netsh wlan disconnect")

# Returns True if ping is successful
def check():
    return os.system("ping 8.8.8.8") == 0

# If wifi goes down, diconnect then reconnect
while True:
    if not check():
        disable()
        sleep(.5)
        enable()
    sleep(FREQUENCY)
