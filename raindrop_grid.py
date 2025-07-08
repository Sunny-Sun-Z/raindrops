import pygame
import sys
from raindrop import Raindrop
from settings import Settings


class RaindropGrid:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Rain Drops')
        self.raindrops = pygame.sprite.Group()
        self.raindrops = pygame.sprite.Group()
        self._create_grid()
        
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._update_screen()
            self._update_raindrops() 
            self.clock.tick(60)        
        
            
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
          
        self.raindrops.draw(self.screen)
        pygame.display.flip()  
        
    def _update_raindrops(self):
        """Update the position of all raindrops in the grid."""
        self._check_grid_edges()
        self.raindrops.update()
        
        
    def _create_grid(self):
        """Create the grid of raindrops."""
        # Create an raindrop and keep adding raindrops until there's no room left.
        # Spacing between raindrops is one raindrop width and one raindrop height.
        # Make an raindrop.
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        
        self.raindrops.add(raindrop)
        # raindrop_width = raindrop.rect.width

        # current_x = raindrop_width
        current_x, current_y = raindrop_width, raindrop_height
        while current_y < (self.settings.screen_height - 3 * raindrop_height):
            while current_x < (self.settings.screen_width - 2 * raindrop_width):
                self._create_raindrop(current_x, current_y)
                current_x += 2 * raindrop_width
                      
             # Finished a row; reset x value, and increment y value.
            current_x = raindrop_width
            current_y += 2 * raindrop_height
            
                                    
    def _create_raindrop(self, x_position, y_position):
        """Create an Raindrop and place it in the row."""
        new_raindrop = Raindrop(self)
        new_raindrop.x = x_position
        new_raindrop.rect.y = y_position
        new_raindrop.rect.x = x_position
        self.raindrops.add(new_raindrop)
     
    def _check_grid_edges(self):
        """Respond appropriately if any raindrops have reached an edge."""
        for raindrop in self.raindrops.sprites():
            if raindrop.check_edges():
                self._change_grid_direction()
                break
            
    def _change_grid_direction(self):   
        """Drop the entire grid and change the grid's direction."""
        for raindrop in self.raindrops.sprites():
             raindrop.rect.y += self.settings.grid_drop_speed
        self.settings.grid_direction *= -1
     
if __name__ == '__main__':
    rd = RaindropGrid()
    rd.run_game()