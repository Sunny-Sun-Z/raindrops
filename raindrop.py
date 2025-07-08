import pygame
import pygame.sprite
from settings import Settings

class Raindrop(pygame.sprite.Sprite):
    def __init__(self, rg):
        super().__init__()
        self.screen = rg.screen
        self.settings = rg.settings
        
        self.image =pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        
    def update(self):
        """Move the alien to the right."""   
        # self.x += self.settings.alien_speed
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
        
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)