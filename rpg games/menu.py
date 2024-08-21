import pygame

# Initialize Pygame 
pygame.font.init()

# Define menu options
menu_font = pygame.font.SysFont(None, 36)
menu_items = ["Resume Game"]
menu_rects = []

# The options 
# option one for the settins 
setting_font = pygame.font.SysFont(None, 40)
setting_text = "Settings: Currently not available in the demo"
setting_surface = setting_font.render(setting_text, True, (255, 255, 255))
setting_rect = setting_surface.get_rect(center=(400, 320))
# opiton two for the level selections
level_font = pygame.font.SysFont(None, 40)
level_text = "Level Selection: Currently not available in demo"
level_surface = level_font.render(level_text, True, (255, 255, 255))
level_rect = level_surface.get_rect(center=(400, 320))
# Definiing the menue text font 
for i, item in enumerate(menu_items):
    menu_text = menu_font.render(item, True, (255, 255, 255))
    menu_rect = menu_text.get_rect(center=(400, 320 + i * 40))
    menu_rects.append((menu_text, menu_rect))
# draw the menu screen 
def draw_menu(screen):
    screen.fill((0, 0, 0))  
    for menu_text, menu_rect in menu_rects:
        screen.blit(menu_text, menu_rect)
# drawing setting back ground (currently it will be black sicne I don't have a menue)
def draw_setting_screen(screen):
    screen.fill((0, 0, 0))  
    screen.blit(setting_surface, setting_rect)
# level selecting background
def draw_level_selection_screen(screen):
    screen.fill((0, 0, 0))  
    screen.blit(level_surface, level_rect)
# exepcting inputs
def handle_menu_events():
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
    return None
