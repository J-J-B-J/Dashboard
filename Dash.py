"""Main program for dash."""
import pygame
from sys import exit
import time

import Settings
import Date_Time
import Weather


class Dashboard:
    """Class to manage the dash."""
    def __init__(self):
        self.settings = Settings.Settings()

        pygame.init()

        self.screen_size = pygame.display.get_desktop_sizes()[0]
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.toggle_fullscreen()
        pygame.display.set_allow_screensaver(False)
        pygame.display.set_caption("Dashboard")
        pygame.mouse.set_visible(False)
        if self.settings.dark:
            self.bg_colour = (50, 50, 50)
        else:
            self.bg_colour = (238, 238, 238)

        self.time = Date_Time.Time(self)
        self.weather = Weather.Weather(self)

    def run(self):
        """Run the main loop for the dashboard."""
        change = True
        old_time = Date_Time.get_date_time()
        old_weather = self.weather.refresh()
        weather_check_time = time.time()

        while True:
            time.sleep(5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

            current_time = Date_Time.get_date_time()
            if current_time != old_time:
                old_time = current_time
                change = True

            if time.time() >= weather_check_time + 600:
                weather_check_time = time.time()
                weather = self.weather.refresh()
                if weather != old_weather:
                    old_weather = weather
                    change = True

            if change:
                self.screen.fill(self.bg_colour)
                self.weather.blit_me()
                self.time.blit_me()
                pygame.display.flip()
                change = False


dash = Dashboard()
dash.run()
