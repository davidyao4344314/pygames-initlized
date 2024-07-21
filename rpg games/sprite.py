import pygame
from gravity import GravityAffected

"""
Create the main character class 'cell' that inherits from GravityAffected
"""
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

    """
    Update player based on gravity and update player image based on attack or not
    """
    def update(self, gravity, screen_height):
        self.apply_gravity(gravity, screen_height)
        if self.is_attacking:
            self.attack_timer -= 1
            if self.attack_timer <= 0:
                self.is_attacking = False
                self.image = self.original_image

    """
    This function is for attacking the enemy
    """
    def melee_attack(self, target):
        if not self.is_attacking:
            self.is_attacking = True
            self.attack_timer = self.attack_duration
            self.image = self.attack_image
            # Calculate and apply damage to the target
            target.take_damage(20)

    """
    This function is for ranged attack
    """
    def ranged_attack(self):
        print("Ranged attack")

    """
    This function is for taking damage
    """
    def take_damage(self, damage):
        self.health -= damage
        print(f"Cell takes {damage} damage. Health is now {self.health}.")
        if self.health <= 0:
            print("Cell is dead.")
            self.kill()

"""
Create the enemy class 'Virus' that inherits from GravityAffected
"""
class Virus(GravityAffected):
    def __init__(self, x, y, scale, virus_image, attack_image):
        super().__init__()
        self.original_image = pygame.transform.scale(virus_image, (int(virus_image.get_width()), int(virus_image.get_height() * scale)))
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

    """
    Update virus based on gravity and update virus image based on attack or not
    """
    def update(self, gravity, screen_height):
        self.apply_gravity(gravity, screen_height)
        if self.is_attacking:
            self.attack_timer -= 1
            if self.attack_timer <= 0:
                self.is_attacking = False
                self.image = self.original_image

    """
    This function is for attacking the enemy
    """
    def melee_attack(self, target):
        if not self.is_attacking:
            self.is_attacking = True
            self.attack_timer = self.attack_duration
            self.image = self.attack_image
            # Calculate and apply damage to the target
            target.take_damage(20)

    """
    This function is for ranged attack
    """
    def ranged_attack(self):
        print("Ranged attack")

    """
    This function is for taking damage
    """
    def take_damage(self, damage):
        self.health -= damage
        print(f"Virus takes {damage} damage. Health is now {self.health}.")
        if self.health <= 0:
            print("Virus is dead.")
            self.kill()
