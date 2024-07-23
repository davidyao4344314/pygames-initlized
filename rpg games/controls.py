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
    pygame.K_l: False
}

def handle_events(player1, enemy):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key in keys:
                keys[event.key] = True
            if event.key == pygame.K_k:
                player1.melee_attack(enemy)
            if event.key == pygame.K_l:
                player1.ranged_attack()
        if event.type == pygame.KEYUP:
            if event.key in keys:
                keys[event.key] = False
    return True

def move_player(player1):
    dx, dy = 0, 0
    if keys[pygame.K_a]:
        dx = -1
    if keys[pygame.K_d]:
        dx = 1
    if keys[pygame.K_w] or keys[pygame.K_SPACE]:
        dy = -1
    if keys[pygame.K_s]:
        dy = 1
    player1.move(dx, dy)
