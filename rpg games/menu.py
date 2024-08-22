import pygame

# Initialize Pygame 
pygame.font.init()

# Create the screen first so you can use it to center the menu
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# The menu options
menu_font = pygame.font.SysFont(None, 36)
menu_items = ["Resume Game", "Quit","Setting"]
menu_rects = []

# Menu text fonts 
i = 0
while i < len(menu_items):
    item = menu_items[i]
    menu_text = menu_font.render(item, True, (255, 255, 255))
    menu_rect = menu_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + i * 40))
    menu_rects.append((menu_text, menu_rect))
    i += 1


# draw the menu screen 
def draw_menu(screen):
    screen.fill((0, 0, 0))  
    for menu_text, menu_rect in menu_rects:
        screen.blit(menu_text, menu_rect)
# drawing setting back ground (currently it will be black sicne I dont have a menue)
def draw_setting_screen(screen):
    screen.fill((0, 0, 0))  
    screen.blit(setting_surface, setting_rect)
# level selecting background
def draw_level_selection_screen(screen):
    screen.fill((0, 0, 0))  
    screen.blit(level_surface, level_rect)
# exepcting inputs
def handle_menu_events():
    i = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, (menu_text, menu_rect) in enumerate(menu_rects):
                if menu_rect.collidepoint(event.pos):
                    if i == 0:  
                        return True
                    if i == 2:
                        return "Quit"
                    if i == 3:
                        return "Settings"
    return None
# The options 
# option one for the settins 
setting_font = pygame.font.SysFont(None, 40)
setting_text = "Settings: Currently not available in the demo"
setting_surface = setting_font.render(setting_text, True, (255, 255, 255))
setting_rect = setting_surface.get_rect(center=(400, 320))
