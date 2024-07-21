# initliazing pygame 
import pygame
from sprite import cell  
import controls

pygame.init()
#initalzing player screan 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('RPG')

# Player gravity
gravity = 0.5

# Load player images
player_image = pygame.image.load('white_blood_cell.png')
attack_image = pygame.image.load('white_blood_cell_attack.png')

# Initialize player instance
player1 = cell(200, 200, 3, player_image, attack_image)  

run = True
clock = pygame.time.Clock()

while run:
    screen.fill((0, 0, 0))  # Fill the screen with black before drawing
    screen.blit(player1.image, player1.rect)
    
    run = controls.handle_events(player1)
    controls.move_player(player1)

    player1.update(gravity, SCREEN_HEIGHT)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
