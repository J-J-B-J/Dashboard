"""A class to draw the time to the screen."""
from datetime import datetime as dt

import pygame.font

import Base_Text


def get_time():
    """
    Get a neatly formatted time
    :return: formatted time
    """
    time = str(dt.now())
    time = time[11:16]
    time = time.lstrip('0')
    hour = time[:2].rstrip(':')
    hour = int(hour)
    if 0 < hour < 12:
        time += " am"
    elif hour == 12:
        time += " pm"
    elif hour == 0:
        time += " am"
    else:
        time = str(int(time[:2]) - 12) + time[2:]
        time += " pm"
    return time


class Time(Base_Text.BaseText):
    """A class to draw the time to the screen"""
    def __init__(self, dash):
        super().__init__(dash)

    def refresh(self):
        """Refresh the time"""
        self.text = get_time()
        self.text_rect.left = self.screen_rect.left + int(self.window_x / 256)
        self.text_rect.top = self.screen_rect.top + int(self.window_y / 160)
