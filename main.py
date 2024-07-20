# main.py

import pygame
from sprite import cell
import controls

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('RPG')

# Load player image
player_image = pygame.image.load('white_blood_cell.png')

# Initialize player instance
player1 = cell(200, 200, 3, player_image)

run = True
clock = pygame.time.Clock()

while run:
    screen.fill((0, 0, 0))  # Fill the screen with black before drawing
    screen.blit(player1.image, player1.rect)
    
    run = controls.handle_events()
    controls.move_player(player1)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
