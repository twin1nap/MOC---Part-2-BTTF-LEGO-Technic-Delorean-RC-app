import logging
import ctypes
from pylgbst import get_connection_bleak
from pylgbst.hub import TechnicHub, EncodedMotor, COLOR_NONE
import time

#logging.basicConfig(level=logging.INFO)

hub_mac = "90:84:2B:4A:12:8D"
conn = get_connection_bleak(hub_mac=hub_mac)
hub = TechnicHub(conn)

#hub.switch_off()
hub.led.set_color(COLOR_NONE)
#hub.port_CD.start_speed(0.1, 0)


def callback(angle):
    print("angle: %s" % angle)
    if angle > 0 or angle < 0:
        hub.port_C.goto_position(0)
        #ctypes.windll.user32.LockWorkStation()
        #hub.port_CD.start_speed(0, 0.1)
        #time.sleep(1)
        #hub.port_C.unsubscribe(callback)
        #hub.switch_off()

angle =  hub.port_C.subscribe(callback, mode=EncodedMotor.SENSOR_ANGLE)
while True:
    if 5 == 6:
        print("what!")
