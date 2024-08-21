import pygame

# Initialize Pygame 
pygame.font.init()


# The menu options
menu_font = pygame.font.SysFont(None, 36)
menu_items = ["Resume Game", "Quit"]
menu_rects = []


# Menue text fonts 
for i, item in enumerate(menu_items):
    menu_text = menu_font.render(item, True, (255, 255, 255))
    menu_rect = menu_text.get_rect(center=(400, 320 + i * 40))
    menu_rects.append((menu_text, menu_rect))
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
    return None
