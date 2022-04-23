"""A class to draw the time to the screen."""
from datetime import datetime as dt


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
    if hour < 13:
        time += " am"
    else:
        time = str(int(time[:2])-12) + time[2:]
        time += " pm"
    return time
