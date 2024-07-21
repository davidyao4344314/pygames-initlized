import pygame
from sprite import cell, Virus  
import controls

pygame.init()

# Initializing player screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('RPG')

# Player gravity
gravity = 0.5

# Load player images
player_image = pygame.image.load('white_blood_cell.png')
attack_image = pygame.image.load('white_blood_cell_attack.png')

# Load virus images (same as player for now since i don't have another sprite)
virus_image = pygame.image.load('white_blood_cell.png')
virus_attack_image = pygame.image.load('white_blood_cell_attack.png')

# Initialize player instance
player1 = cell(200, 200, 3, player_image, attack_image)

# Initialize enemy instance
enemy = Virus(600, 200, 3, virus_image, virus_attack_image)

# Create sprite group for all sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(enemy)

run = True
clock = pygame.time.Clock()

while run:
    screen.fill((0, 0, 0))  # Fill the screen with black before drawing(as if right now since i don't have a back ground)
    
    # Update every sprites
    all_sprites.update(gravity, SCREEN_HEIGHT)
    
    # Draw every sprites
    all_sprites.draw(screen)
    
    run = controls.handle_events(player1, enemy)
    controls.move_player(player1)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
