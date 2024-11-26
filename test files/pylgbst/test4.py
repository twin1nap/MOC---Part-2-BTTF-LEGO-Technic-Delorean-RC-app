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



hub.motor_A.goto_position(0)
hub.led.set_color(3)
hub.motor_A.goto_position(45)
time.sleep(1)
hub.motor_A.goto_position(0, degrees_secondary=None, speed=0.5)
time.sleep(1)
hub.motor_A.goto_position(45)
hub.motor_A.goto_position(0, degrees_secondary=None, speed=0.001)
hub.motor_A.goto_position(360)
hub.motor_A.goto_position(0)
hub.motor_A.goto_position(0, degrees_secondary=None, speed=0.001)

rotations = [0, 45, 360, 0, 90, 0, 20, 30, 0, 90, 180, 270, 360, 0, 123, 0]
print("starting(", rotations, ")")
for index in range(len(rotations)):
    print(rotations[index])
    hub.motor_A.goto_position(rotations[index], degrees_secondary=None, speed=0.1)
    time.sleep(1)

while True:
    inp = input()
    hub.motor_A.goto_position(int(inp), degrees_secondary=None, speed=0.1)
    if inp == "stop":
        break
for speeds in range(101):
    hub.motor_A.start_speed(speeds/100)
    print(speeds)
time.sleep(3)
hub.motor_A.stop()