"""A settings class"""
import json
import os


class Settings:
    """A class to manage settings"""
    def __init__(self):
        try:
            with open("UserData/UserData.json") as open_file:
                self.user_data = json.load(open_file)
            self.API_Key = self.user_data["API KEY"]
            self.location = self.user_data["Location"]
        except FileNotFoundError:
            self.reset_api_key_and_location()
        except KeyError:
            self.reset_api_key_and_location()

    def reset_api_key_and_location(self):
        """Reset the api key and location"""
        print("\nYour API key and location are incorrect or don't exist!")
        print("To get an API key:")
        print("1. Go to https://openweathermap.org and create an account.")
        print("2. Go to https://home.openweathermap.org/api_keys and copy your\
 API Key")
        self.user_data = {
            "API KEY": input("Please enter your API key: "),
            "Location": input("What is your location: ")
        }
        try:
            os.mkdir("UserData")
        except FileExistsError:
            pass
        with open("UserData/UserData.json", "w") as open_file:
            json.dump(self.user_data, open_file)
