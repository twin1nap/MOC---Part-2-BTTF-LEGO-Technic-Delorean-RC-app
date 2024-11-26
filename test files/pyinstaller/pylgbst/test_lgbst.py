import logging 
from pylgbst import get_connection_bleak
from pylgbst.hub import TechnicHub  
import time

#logging.basicConfig(level=logging.INFO)
hub_mac = "90:84:2B:4A:12:8D"
print("\n"*10)
conn = get_connection_bleak(hub_mac=hub_mac)
hub = TechnicHub(conn)

hub.led.set_color(3)
hub.port_CD.start_speed(0.1, -0.1)
time.sleep(5)
hub.port_CD.stop()
hub.led.set_color(10)
hub.led.set_color(8)
hub.led.set_color(10)
hub.led.set_color(8)
hub.led.set_color(10)
hub.switch_off()
