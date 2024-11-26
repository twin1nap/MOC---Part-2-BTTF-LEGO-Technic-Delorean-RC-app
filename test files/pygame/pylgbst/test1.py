import pygame
import time
from sys import exit
from pylgbst import get_connection_bleak
from pylgbst.hub import TechnicHub  

pygame.init
screen = pygame.display.set_mode((210, 100))
pygame.display.set_caption("lego test 1")

conn_surf = pygame.Surface((100, 100))
conn_surf.fill("red")
motor_run_surf = pygame.Surface((100, 100))
motor_run_surf.fill("red")
connection = False
waited_frame = False
hub_mac = "90:84:2B:4A:12:8D"
conn = get_connection_bleak(hub_mac=hub_mac)
print(conn)

while True:
    for event  in pygame.event.get(): #gets events
        if event.type == pygame.QUIT: #if event is quit
            pygame.quit()
            hub.switch_off()
            exit() # exits the code
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                hub.port_CD.start_speed(1, 1)
                motor_run_surf.fill("green")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                hub.port_CD.stop()
                motor_run_surf.fill("red")

    screen.blit(conn_surf, (0, 0))
    screen.blit(motor_run_surf, (110, 0))
    if waited_frame == True:
        if connection == False:
            hub_mac = "90:84:2B:4A:12:8D"
            conn = get_connection_bleak(hub_mac=hub_mac)
            hub = TechnicHub(conn)
            time.sleep(1)
            connection = True
    else:
        print("waited")
        waited_frame = True

    if conn.is_alive:
        conn_surf.fill("green")

    pygame.display.update()
