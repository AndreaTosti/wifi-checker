import os
from time import sleep
from pythonping import ping

# netsh wlan show profile
# netsh wlan show interfaces

SSID = "ssid"
NAME = "name"
INTERFACE = "interface"

# How frequently to check if wifi is slow. In seconds
FREQUENCY = 4

# Reconnect wifi if ping goes higher than PINGCHECK
PINGCHECK = 70

def enable():
    connectStr = "netsh wlan connect ssid=%s name=%s interface=%s" % (SSID,NAME,INTERFACE)
    os.system(connectStr)

def disable():
    os.system("netsh wlan disconnect")

# Returns True if wifi is acceptable
def check():
    response_list = ping('8.8.8.8', size=40, count=10)
    return response_list.rtt_avg_ms < PINGCHECK

# If ping increases above PINGCHECK, disable then re-enable
while True:
    if not check():
        disable()
        sleep(.5)
        enable()
    sleep(FREQUENCY)
