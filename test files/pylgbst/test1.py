from pylgbst.hub import MoveHub
from pylgbst import get_connection_bleak
import time

# Attempt to auto-detect and connect to the Technic Hub
hub_mac = "90:84:2B:4A:12:8D"
conn = get_connection_bleak(hub_mac=hub_mac)
hub = MoveHub(conn)

# Print detected peripherals
for device in hub.peripherals:
    print(device)

hub.motor_A.start_speed(0)
time.sleep(2)
hub.motor_A.stop()