# tutorial: https://www.youtube.com/watch?v=AY9MnQ4x3zk&t=306s
import pygame
from sys import exit # imports the exit command from system

pygame.init() # makes screen
screen = pygame.display.set_mode((800, 400)) # displays screen(width, height)
pygame.display.set_caption("test screen") # set sthe screen name
clock = pygame.time.Clock() # makes clock the pygame clock

#screen.fill("blue") # sets background color
test_surface = pygame.Surface((100, 200)) # creates a surface(like a div in html)(width, height)
test_surface.fill("Red") # fils test_surface with the color blue

while True:
    for event  in pygame.event.get(): #gets events
        if event.type == pygame.QUIT: #if event is quit
            pygame.quit()
            exit() # exits the code
            
    screen.blit(test_surface, (200, 100)) #blit is block image transfer(putting an surface on a surface)(surface, position(width, height))
    pygame.display.update() # update the screen
    clock.tick(60) # set max fps to 60