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
    try:
        time = str(dt.now())
    except Exception:
        return "Connection Error!"
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


def get_date():
    """
    Get a neatly formatted time
    :return: formatted time
    """
    try:
        date = str(dt.now())
    except Exception:
        return "Connection Error!"
    month = date[5:7]
    day = date[8:10]
    month = month.lstrip("0")
    day = day.lstrip("0")
    month_names = {"1": "Jan", "2": "Feb", "3": "Mar", "4": "Apr", "5": "May",
                   "6": "Jun", "7": "Jul", "8": "Aug", "9": "Sep", "10": "Oct",
                   "11": "Nov", "12": "Dec"}
    day_names = {"1": "st", "2": "nd", "3": "rd", "21": "st", "22": "nd",
                 "23": "rd", "31": "st"}
    if day in day_names.keys():
        full_day = str(day) + day_names[day]
    else:
        full_day = str(day) + "th"
    full_month = month_names[month]
    date = f"{full_day} of {full_month}"
    return date


def get_date_time():
    """
    Get the date and the time in one lot
    :return: date and time, formatted
    """
    return get_date() + " | " + get_time()


class Time(Base_Text.BaseText):
    """A class to draw the time to the screen"""
    def __init__(self, dash):
        super().__init__(dash)
        self.last_sound_played = current_time.time()

    def refresh(self):
        """Refresh the time"""
        self.text = get_date_time()
        self.text_rect.left = self.screen_rect.left + int(self.window_x / 256)
        self.text_rect.top = self.screen_rect.top + int(self.window_y / 160)
