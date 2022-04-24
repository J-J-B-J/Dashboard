"""A file to manage the screen background."""
import pygame.image

import Base_Text
import Date_Time


night = "Images/Night.jpeg"
sunrise = "Images/Sunrise.jpeg"
day = "Images/Day.jpeg"
sunset = "Images/Sunset.jpeg"
times = {"12a": night, "1a": night, "2a": night, "3a": night, "4a": night,
         "5a": sunrise, "6a": sunrise, "7a": sunrise, "8a": sunrise, "9a": day,
         "10a": day, "11a": day, "12p": day, "1p": day, "2p": day, "3p": day,
         "4p": sunset, "5p": sunset, "6p": sunset, "7p": sunset, "8p": night,
         "9p": night, "10p": night, "11p": night}


def get_image(time: str):
    """Get the image file"""
    hour = time[:2].rstrip(":")
    am_pm = time[-2:-1]
    short_time = hour + am_pm
    try:
        return times[short_time]
    except KeyError:
        return day


class Background(Base_Text.BaseText):
    """A class to manage the screen background."""
    def __init__(self, dash):
        super().__init__(dash)
        self.image = pygame.image.load(get_image(Date_Time.get_time()))
        self.image = pygame.transform.scale(self.image, self.dash.screen_size)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.screen_rect.center

    def refresh(self):
        """Refresh the image"""
        self.image = pygame.image.load(get_image(Date_Time.get_time()))
        self.image = pygame.transform.scale(self.image, self.dash.screen_size)
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.screen_rect.center

    def blit_me(self):
        """Blit the image to the screen"""
        self.refresh()
        self.screen.blit(self.image, self.image_rect)
