import pygame
from gravity import GravityAffected

"""
Create the main character class 'cell' that inherits from GravityAffected
"""
class cell(GravityAffected):
    def __init__(self, x, y, scale, player_image, attack_image, defense_image):
        super().__init__()
        self.original_image = pygame.transform.scale(player_image, (int(player_image.get_width() * scale), int(player_image.get_height() * scale)))
        self.attack_image = pygame.transform.scale(attack_image, (int(attack_image.get_width() * scale), int(attack_image.get_height() * scale)))
        self.defense_image = pygame.transform.scale(defense_image, (int(defense_image.get_width() * scale), int(defense_image.get_height() * scale)))
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.health = 100
        self.max_health = 100  
        self.is_attacking = False
        self.attack_duration = 10
        self.attack_timer = 0
        self.is_defending = False
        self.defense_duration = 20
        self.defense_timer = 0
        self.defense_reduction = 0.5  

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

        if self.is_defending:
            self.defense_timer -= 1
            if self.defense_timer <= 0:
                self.is_defending = False
                self.image = self.original_image

    """
    This function is for attacking the enemy
    """
    def melee_attack(self, target):
        if not self.is_attacking:
            self.is_attacking = True
            self.attack_timer = self.attack_duration
            self.image = self.attack_image
            target.take_damage(20)

    """
    This function is for ranged attack
    """
    """
    def ranged_attack(self):
        print("Ranged attack")
    """

    """
    This function is for taking damage
    """
    def take_damage(self, damage):
        if self.is_defending:
            damage *= self.defense_reduction
        self.health -= damage
        print(f"Cell takes {damage} damage. Health is now {self.health}.")
        if self.health <= 0:
            print("Cell is dead.")
            self.kill()

    """This function is for drawing the health bar 
    """
    def draw_health_bar(self, surface):
        bar_width = 200  
        bar_height = 20  
        player_fill = (self.health / self.max_health) * bar_width

        if self.health > 50:
            player_color = (0, 255, 0)  
        elif self.health > 20:
            player_color = (255, 165, 0)  
        else:
            player_color = (255, 0, 0)  

        # Draw the health bar at the top of the screen
        pygame.draw.rect(surface, player_color, (50, 10, player_fill, bar_height))
        pygame.draw.rect(surface, (255, 255, 255), (50, 10, bar_width, bar_height), 2)


"""
Create the enemy class 'Virus' that inherits from GravityAffected
"""
class Virus(GravityAffected):
    def __init__(self, x, y, scale, virus_image, attack_image):
        super().__init__()
        self.original_image = pygame.transform.scale(virus_image, (int(virus_image.get_width() * scale), int(virus_image.get_height() * scale)))
        self.attack_image = pygame.transform.scale(attack_image, (int(attack_image.get_width() * scale), int(attack_image.get_height() * scale)))
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.health = 100
        self.max_health = 100  
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
            target.take_damage(20)
            
    """This function is for drawing the health bar 
    """
    def draw_health_bar(self, surface):
        bar_width = 50  
        bar_height = 5  
        fill = (self.health / self.max_health) * bar_width

        if self.health > 50:
            color = (0, 255, 0)  
        elif self.health > 20:
            color = (255, 165, 0)  
        else:
            color = (255, 0, 0)  

        bar_x = self.rect.x + (self.rect.width - bar_width) // 2
        bar_y = self.rect.y - 10  

        pygame.draw.rect(surface, color, (bar_x, bar_y, fill, bar_height))
        pygame.draw.rect(surface, (255, 255, 255), (bar_x, bar_y, bar_width, bar_height), 2)

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
    """
    Adding a healing 
    """
    def healing(self):
        self.health += 20