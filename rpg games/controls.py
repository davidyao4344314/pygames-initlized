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
    pygame.K_UP: False
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
    # When the player presses A to move left
    if keys[pygame.K_a]:
        player.move(dx=-1)
    # When the player presses D to move right
    if keys[pygame.K_d]:
        player.move(dx=1)
    # When the player presses W to jump
    if keys[pygame.K_w] or keys[pygame.K_SPACE]:
        player.move(dy=-1)
    # Player can also move with the arrow keys
    if keys[pygame.K_LEFT]:
        player.move(dx=-1)
    if keys[pygame.K_RIGHT]:
        player.move(dx=1)
    if keys[pygame.K_UP]:
        player.move(dy=-1)
