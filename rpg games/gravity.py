import pygame

class GravityAffected(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity_y = 0

    def apply_gravity(self, gravity, screen_height):
        self.velocity_y += gravity
        self.rect.y += self.velocity_y
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.velocity_y = 0
    