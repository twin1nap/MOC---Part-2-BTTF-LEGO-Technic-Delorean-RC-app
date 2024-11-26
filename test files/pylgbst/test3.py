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


hub.motor_A.start_speed(1)
time.sleep(2)
hub.motor_A.stop()
hub.motor_A.timed(2, 0.1)
hub.motor_A.angled(45, 0.5)
time.sleep(1)
hub.motor_A.angled(-45, 0.5)
hub.motor_A.goto_position(0)
time.sleep(1)
hub.motor_A.goto_position(45)
time.sleep(1)
hub.motor_A.goto_position(-45)
time.sleep(1)
hub.motor_A.goto_position(0)
hub.led.set_color(3)

speed = 1
while True:
    startStop = input()
    if startStop == "start":
        hub.motor_A.start_speed(float(speed))
    elif startStop == "stop":
        hub.motor_A.stop()
    elif startStop == "color":
        for index in range(11):
            hub.led.set_color(index)
    elif startStop == "set speed":
        speed = input("welke snelheid?  ")