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

# Load virus images (same as player for now)
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

# Define menu options
menu_font = pygame.font.SysFont(None, 36)
menu_items = ["Resume Game", "Settings", "Level Selection"]
menu_rects = []

# Define the setting 
setting_font = pygame.font.SysFont(None, 40)
setting_text = "Settings: Currently not available in demo"
setting_surface = setting_font.render(setting_text, True, (255, 255, 255))
setting_rect = setting_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
# define the level slection fonts
level_font = pygame.font.SysFont(None, 40)
level_text = "Level Selection: Currently not available in demo"
level_surface = level_font.render(level_text, True, (255, 255, 255))
level_rect = level_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

for i, item in enumerate(menu_items):
    menu_text = menu_font.render(item, True, (255, 255, 255))
    menu_rect = menu_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + i * 40))
    menu_rects.append((menu_text, menu_rect))

def draw_menu():
    screen.fill((0, 0, 0))  
    for menu_text, menu_rect in menu_rects:
        screen.blit(menu_text, menu_rect)

def draw_setting_screen():
    screen.fill((0, 0, 0))  
    screen.blit(setting_surface, setting_rect)

def draw_level_selection_screen():
    screen.fill((0, 0, 0))
    screen.blit(level_surface, level_rect)

run = True
paused = False
#Defining the current screan
current_screen = "menu"
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if current_screen == "menu":
                    paused = not paused
                    if paused:
                        # to fix the issue that the character keep moving foward even though they are no key are pressed
                        controls.keys = {key: False for key in controls.keys}
                else:
                    current_screen = "menu"
        if event.type == pygame.MOUSEBUTTONDOWN and paused and current_screen == "menu":
            for i, (menu_text, menu_rect) in enumerate(menu_rects):
                if menu_rect.collidepoint(event.pos):
                    # resume game
                    if i == 0:
                        paused = False
                        controls.keys = {key: False for key in controls.keys}
                        #setting
                    elif i == 1:
                        current_screen = "settings"
                        # level selection
                    elif i == 2:
                        current_screen = "level_selection"

    if not paused:
        screen.fill((0, 0, 0))
        all_sprites.update(gravity, SCREEN_HEIGHT)
        all_sprites.draw(screen)
        run = controls.handle_events(player1, enemy)
        controls.move_player(player1)
    else:
        if current_screen == "menu":
            draw_menu()
        elif current_screen == "settings":
            draw_setting_screen()
        elif current_screen == "level_selection":
            draw_level_selection_screen()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
