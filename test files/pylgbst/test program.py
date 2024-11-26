# made in python 3.13.0

from pylgbst import get_connection_auto
from pylgbst.hub import MoveHub
import time

print("\nthis program is made in python 3.13.0")



conn = get_connection_auto()  # ! don't put this into `try` block
try:
    hub = MoveHub(conn)
finally:
    conn.disconnect()

# You can now interact with the hub, for example, controlling a motor:
hub.motor_A.start_speed(0.2)
time.sleep(2)
hub.motor_A.stop()  # Stop the motor
