import pygame
from sprite import cell, Virus  
import controls
from menu import draw_menu, handle_menu_events

pygame.init()

# Fullscreen setup
info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('RPG')

# Player gravity
gravity = 0.5

# Load player images
player_image = pygame.image.load('white_blood_cell.png')
attack_image = pygame.image.load('white_blood_cell_attack.png')
defense_image = pygame.image.load('white_blood_cell_attack.png')
healing_image = pygame.image.load('healing.png')

# Load virus images (same as player for now since I don't have another sprite)
virus_image = pygame.image.load('white_blood_cell.png')
virus_attack_image = pygame.image.load('white_blood_cell_attack.png')

# Initialize player instance
player1 = cell(200, 200, 3, player_image, attack_image, defense_image)

# Initialize enemy instance
enemy = Virus(600, 200, 3, virus_image, virus_attack_image)

# Create sprite group for all sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(enemy)

def draw_health_bar(surface, player):
    bar_width = 200
    bar_height = 20
    player_fill = (player.health / player.max_health) * bar_width

    if player.health > 50:
        player_color = (0, 255, 0)
    elif player.health > 20:
        player_color = (255, 165, 0)
    else:
        player_color = (255, 0, 0)

    pygame.draw.rect(surface, player_color, (50, 10, player_fill, bar_height))
    pygame.draw.rect(surface, (255, 255, 255), (50, 10, bar_width, bar_height), 2)

healing_active = False
game_state = "menu"  

run = True
clock = pygame.time.Clock()

while run:
    # Checking if the user choosen to open the game or not
    if game_state == "game":
        screen.fill((0, 0, 0))  # Fill the screen with black before drawing
        
        # Update all sprites
        all_sprites.update(gravity, SCREEN_HEIGHT)

        # Draw health bar
        draw_health_bar(screen, player1)

        if healing_active:
            screen.blit(healing_image, (50, 40))    

        # Draw all sprites
        all_sprites.draw(screen)
        
        # Handle movement
        run = controls.handle_events(player1, enemy)
        controls.move_player(player1)
        # Healing objects 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    healing_active = True
                if event.key == pygame.K_ESCAPE:
                    game_state = "menu"  
    # Menue option 
    elif game_state == "menu":
        draw_menu(screen)
        menu_action = handle_menu_events()
        if menu_action == True: 
            game_state = "game"



    pygame.display.update()
    clock.tick(60)

pygame.quit()
