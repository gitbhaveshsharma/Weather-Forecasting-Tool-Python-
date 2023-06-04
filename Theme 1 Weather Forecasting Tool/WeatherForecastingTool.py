# Path: WeatherForecastingTool.py
# import requests module
import requests
import json
# make a function
def weather_forecast():
    # define api key
    api_key = "f530943c607ff3bf9b35d29a2bccd810"
    # define base url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # define city name
    city_name = input("Enter city name : ")
    # complete url
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    # get method of requests module
    # return response object
    response = requests.get(complete_url)
    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()
    # now x contains list of nested dictionaries
    # we know dictionary contain key value pair
    # check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
        # store the value of "main"
        # key in variable y
        y = x["main"]
        # store the value corresponding
        # to the "temp" key of y
        # convert temperature from Kelvin (K) to Celsius (°C)
        current_temperature = y["temp"] - 273.15
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]
        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]
        # store the value of "weather"
        # key in variable z
        z = x["weather"]
        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]
# print following values into add °C symbol in current_temperature and add % symbol in current_humidity
        print(" Temperature (in °C) = " +
              # print in round and add °C symbol
                str(round(current_temperature, 2)) + "°C" +
                "\n atmospheric pressure (in hPa unit) = " +
                str(current_pressure) + "mb" +
                "\n humidity (in percentage) = " +
                str(current_humidity) + "%" +
                "\n description = " +
                str(weather_description))
    else:
        print(" City Not Found ")
# Driver program
if __name__ == "__main__":
    weather_forecast()