import pygame
from gravity import GravityAffected

class cell(GravityAffected):
    def __init__(self, x, y, scale, player_image, attack_image):
        super().__init__()
        self.original_image = pygame.transform.scale(player_image, (int(player_image.get_width()), int(player_image.get_height() * scale)))
        self.attack_image = pygame.transform.scale(attack_image, (int(attack_image.get_width()), int(attack_image.get_height() * scale)))
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.health = 100
        self.is_attacking = False
        self.attack_duration = 10
        self.attack_timer = 0

    def move(self, dx=0, dy=0):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def update(self, gravity, screen_height):
        self.apply_gravity(gravity, screen_height)
        if self.is_attacking:
            self.attack_timer -= 1
            if self.attack_timer <= 0:
                self.is_attacking = False
                self.image = self.original_image

    def melee_attack(self):
        if not self.is_attacking:
            self.is_attacking = True
            self.attack_timer = self.attack_duration
            self.image = self.attack_image

"""
    def ranged_attack(self):
        print("Ranged attack")
"""
