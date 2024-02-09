# Game.py
import pygame

class Game:
    def __init__(self):
        pygame.init

        # Init size
        self.screen_width = 800
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Windows Name
        pygame.display.set_caption("Snake Game")

    def run(self):
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Background
            self.screen.fill('black')

            pygame.display.flip()
        
        pygame.quit()