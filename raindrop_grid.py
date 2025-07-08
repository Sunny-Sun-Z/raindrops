import pygame
import sys
from settings import Settings


class RaindropGrid:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Rain Drops')
        

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._update_screen()
            self.clock.tick(60)        
        
            
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()    
    
    # def _update_raindrops(self):
        
        
if __name__ == '__main__':
    rd = RaindropGrid()
    rd.run_game()