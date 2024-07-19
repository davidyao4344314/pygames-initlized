# sprite.py

import pygame

class cell(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, player_image):
        super().__init__()
        self.image = pygame.transform.scale(player_image, (int(player_image.get_width()), int(player_image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.health = 100

    def move(self, dx=0, dy=0):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
