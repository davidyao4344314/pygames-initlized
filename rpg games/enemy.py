import pygame

class Target(pygame.sprite.Sprite):
    def __init__(self, x, y, health):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()  
