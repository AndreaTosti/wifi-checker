try:
    import httplib
except:
    import http.client as httplib

import os
from time import sleep

# netsh wlan show profile
# netsh wlan show interfaces

SSID = "ssid"
NAME = "name"
INTERFACE = "interface"

# How frequently to check if wifi is down. In seconds
FREQUENCY = 4

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def enable():
    os.system("netsh interface set interface Wi-Fi ENABLED")
    connectStr = "netsh wlan connect ssid=%s name=%s interface=%s" % (SSID,NAME,INTERFACE)
    print(connectStr)
    os.system(connectStr)

def disable():
    os.system("netsh interface set interface Wi-Fi DISABLED")

def have_internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False
    
# If wifi goes down, diconnect then reconnect
while True:
    cls()
    print("Connessione OK" if have_internet() else "Nessuna connessione verso %s, \nSe vuoi scegliere una rete diversa, chiudi questa finestra\n" % (NAME))
    if not have_internet():
        disable()
        sleep(.5)
        enable()
    sleep(FREQUENCY)
