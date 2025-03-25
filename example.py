import network
import urequests
import time
import os

from firebasertdb import *

WIFI_SSID = "YOUR_WIFI_SSID" 
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"
FIREBASE_URL = "https://YOUR_FIREBASE_REALTIME_DB_NAME.firebaseio.com"

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    
    print("Connecting to WiFi...", end="")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
    print("\nConnected! IP:", wlan.ifconfig()[0])

# Main program
connect_wifi()

fbrtdb = FirebaseRTDB(FIREBASE_URL)

fbrtdb.write(path="path/to/object", data={"sensors" : {"temperature": 25, "humidity": 60}})

data = fbrtdb.read(path="path/to/object")
print("Read Data:", data)

# Example: Update temperature to 30
fbrtdb.update("sensors", {"temperature" : 30})

fbrtdb.delete("test123")
