import pygame

keys = {
    pygame.K_a: False,
    pygame.K_d: False,
    pygame.K_w: False,
    pygame.K_s: False
}

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key in keys:
                keys[event.key] = True
        if event.type == pygame.KEYUP:
            if event.key in keys:
                keys[event.key] = False
    return True

def move_player(player):
    if keys[pygame.K_a]:
        player.move(dx=-1)
    if keys[pygame.K_d]:
        player.move(dx=1)
    if keys[pygame.K_w]:
        player.move(dy=-1)
    if keys[pygame.K_s]:
        player.move(dy=1)
