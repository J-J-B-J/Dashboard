"""A class to draw the time to the screen."""
from datetime import datetime as dt

import pygame.font
import time as current_time

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
        self.last_sound_played = current_time.time()

    def refresh(self):
        """Refresh the time"""
        self.text = get_time()
        if self.text[2:4] == "00" and current_time.time() >= \
                self.last_sound_played + 120:
            pygame.mixer.music.load("C Major.mp3")
            pygame.mixer.music.play()
        self.text_rect.left = self.screen_rect.left + int(self.window_x / 256)
        self.text_rect.top = self.screen_rect.top + int(self.window_y / 160)
