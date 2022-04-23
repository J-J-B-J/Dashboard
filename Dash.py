"""Main program for dash."""
import pygame
from sys import exit
from Time import *


class Dashboard:
    """Class to manage the dash."""
    def __init__(self):
        pygame.init()

        self.screen_size = pygame.display.get_desktop_sizes()[0]
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.toggle_fullscreen()

        self.time = Time()

    def run(self):
        """Run the main loop for the dashboard."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()


dash = Dashboard()
dash.run()
