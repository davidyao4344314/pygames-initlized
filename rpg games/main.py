import pygame
from sprite import cell

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('RPG')

# Load player image
player_image = pygame.image.load('white_blood_cell.png')

# Initialize player instance
player1 = cell(200, 200, 3, player_image)

run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    player1.move(0, 0)  # Example move call, update as needed

    screen.fill((0, 0, 0))
    screen.blit(player1.image, player1.rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
