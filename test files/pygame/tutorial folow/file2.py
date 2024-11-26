# tutorial: https://www.youtube.com/watch?v=AY9MnQ4x3zk&t=306s  1:15:56
import pygame
from sys import exit # imports the exit command from system

pygame.init() # makes screen
screen =pygame.display.set_mode((800, 400)) # displays screen(width, height)
pygame.display.set_caption("test screen") # set sthe screen name
clock = pygame.time.Clock() # makes clock the pygame clock
test_font = pygame.font.Font("font/Pixeltype.ttf", 50) # creates font(font type, font size)(None is the pygame standard font.)
game_active = True

sky_surface =pygame.image.load("graphics/Sky.png").convert() # loads an image from the provided path and converst it to something pygame can handle more easy
ground_surface = pygame.image.load("graphics/ground.png").convert()

score_surfase = test_font.render("my game", False, (64, 64, 64)) # (text to display, smooth edges of text, color)
score_rect = score_surfase.get_rect(center = (400, 50))

snail_surfase = pygame.image.load("graphics/snail/snail1.png").convert_alpha() #coverts it with keeping no background color
snail_rect = snail_surfase.get_rect(midbottom = (600, 300)) # makes a rectangle where the topleft coordinates ar at (80, 200)

player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

while True:
    for event  in pygame.event.get(): #gets events
        if event.type == pygame.QUIT: #if event is quit
            pygame.quit() #quits the program
            exit() # exits the code
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    print("collition")
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800

    if game_active:
        screen.blit(sky_surface, (0, 0)) #blit is block image transfer(putting an surface on a surface)(surface, position(width, height))
        screen.blit(ground_surface, (0, 300))
        #pygame.draw.rect(screen, "blue", score_rect) #one for the aditional border and the other for filling it in
        pygame.draw.rect(screen, "#c0e8ec", score_rect) #drawing a rectangle(surface to draw on, color, rectangle to draw, width, border radius)
        #pygame.draw.rect(screen, "#c0e8ec", score_rect, 10) #drawing a rectangle(surface to draw on, color, rectangle to draw, width, border radius)
        screen.blit(score_surfase, score_rect)

        snail_rect.x -= 4
        if snail_rect.right <= 0:
            snail_rect.right = 800
        screen.blit(snail_surfase, snail_rect)

        # player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        #collition:
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill("yellow")

    #keys= pygame.key.get_pressed()
    #if keys [pygame.K_SPACE]:
    #    print("jump")

    #if player_rect.colliderect(snail_rect): #if an int is 0 and in an if(or while or for) then its False instead of 0
    #   print("collision")

    #mouse_pos = pygame.mouse.get_pos() #mouse_pos is the mouse position
    #if player_rect.collidepoint((mouse_pos)): # checks if the mousepos is inside the player_rec
    #    print(pygame.mouse.get_pressed()) # print the pressed mouse buttons
        
        #print("collition")

    pygame.display.update() # update the screen
    clock.tick(60) # set max fps to 60
    