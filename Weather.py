"""A class to draw the weather conditions to the screen."""
from pyowm import OWM

import Base_Text
import Settings


def temp_to_real_temp(temp):
    """Turn a temp value into the real value"""
    return round(1.447610490128196 * temp - 406.848621627794557, 1)


def get_weather():
    APIKEY = Settings.Settings().API_Key
    OpenWMap = OWM(APIKEY)
    Weather_Data = OpenWMap.weather_manager(). \
        weather_at_place(Settings.Settings().location)
    Forecast = Weather_Data.to_dict()['weather']

    return Forecast


class Weather(Base_Text.BaseText):
    """A class to draw the weather conditions to the screen."""
    def __init__(self, dash):
        super().__init__(dash)

    def refresh(self):
        """Refresh the weather conditoins"""
        self.text = self.get_all()
        self.text_rect.left = self.screen_rect.left + int(self.window_x / 256)
        self.text_rect.bottom = self.screen_rect.bottom - int(self.window_x /
                                                              160)
        return self.text

    def get_rain(self):
        """Get how much rain there is"""
        rain = get_weather()['precipitation_probability']
        if rain:
            return f"{rain}% Rain"
        else:
            return "No Rain"

    def get_cloudiness(self):
        """Get how many clouds there are"""
        clouds = get_weather()['clouds']
        return f"{get_weather()['clouds']}% Clouds"

    def get_temp(self):
        """Get the temperature"""
        temps = get_weather()['temperature']
        temp = temp_to_real_temp(temps['temp'])
        min_temp = temp_to_real_temp(temps['temp_min'])
        max_temp = temp_to_real_temp(temps['temp_max'])
        return f"Temp: {temp}˚C  |  Min/Max: {min_temp}˚ to {max_temp}˚"

    def get_all(self):
        """Get all weather values"""
        return f"{self.get_temp()}  |  {self.get_rain()}  |  \
{self.get_cloudiness()} "
