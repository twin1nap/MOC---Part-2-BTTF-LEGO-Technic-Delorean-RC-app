from pylgbst.hub import MoveHub
from pylgbst import get_connection_bleak
import time

hub_mac = "90:84:2B:4A:12:8D"
conn = get_connection_bleak(hub_mac=hub_mac)
hub = MoveHub(conn)


# Check available ports
print(hub.peripherals)

# Example motor control (if supported on the Technic Hub)
motor = hub.peripherals[hub.PORT_A, hub.PORT_B]  # Replace PORT_A with your motor port
motor.start_speed(-1.0)  # Speed: -1.0 to 1.0
time.sleep(2)
motor.stop()