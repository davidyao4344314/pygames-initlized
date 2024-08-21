import pygame

# Initialize all keys to False to ensure they are not running all the time
keys = {
    pygame.K_a: False,
    pygame.K_d: False,
    pygame.K_w: False,
    pygame.K_s: False,
    pygame.K_SPACE: False,
    pygame.K_LEFT: False,
    pygame.K_RIGHT: False,
    pygame.K_UP: False,
    pygame.K_k: False,
    pygame.K_l: False,
    pygame.K_ESCAPE: False
}

def handle_events(player, enemy):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key in keys:
                keys[event.key] = True
            if event.key == pygame.K_k:
                player.melee_attack(enemy)
            if event.key == pygame.K_l:
                player.defend()
        if event.type == pygame.KEYUP:
            if event.key in keys:
                keys[event.key] = False
        if event.key == pygame.K_ESCAPE:
            return "menue" 
    return True
"""
Acepiting input for the controls
"""
def move_player(player):
    dx = 0
    dy = 0
    if keys[pygame.K_a]:
        dx = -1
    if keys[pygame.K_d]:
        dx = 1
    if keys[pygame.K_w] or keys[pygame.K_SPACE]:
        dy = -1
    if keys[pygame.K_LEFT]:
        dx = -1
    if keys[pygame.K_RIGHT]:
        dx = 1
    if keys[pygame.K_UP]:
        dy = -1
    player.move(dx, dy)
