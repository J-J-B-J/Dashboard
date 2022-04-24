"""A base text superclass"""
import pygame

import Settings


class BaseText:
    """A base text superclass"""
    def __init__(self, dash):
        self.text = "Hello, World!"

        self.settings = Settings.Settings()

        self.dash = dash
        self.screen = dash.screen
        self.screen_rect = dash.screen.get_rect()
        self.text_colour = (22, 112, 240)
        self.bg_colour = (200, 200, 200)

        self.window_size = pygame.display.get_window_size()
        self.window_x = self.window_size[0]
        self.window_y = self.window_size[1]
        font_size = int(self.window_y / 14)
        self.font = pygame.font.SysFont(None, font_size)
        self.time_image = None
        self.time_rect = None

        self.text_image = self.font.render(self.text, True, self.text_colour,
                                           self.bg_colour)

        self.text_rect = self.text_image.get_rect()

        self.refresh()

    def refresh(self):
        """Refresh the text"""
        pass

    def prep_me(self):
        """Make an image of the text"""
        self.text_image = self.font.render(self.text, True, self.text_colour,
                                           self.bg_colour)

        self.text_rect = self.text_image.get_rect()

        self.refresh()

    def blit_me(self):
        """Show the text on the screen"""
        self.prep_me()
        self.screen.blit(self.text_image, self.text_rect)
