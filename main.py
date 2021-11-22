#Libraries import
import datetime
import requests, json
import timeit

#Variables
chatbot = "Petya"
date = "Monday"
weather = "stormy"
username = " "
api_key = "68a26517df75494a2a654940bd7343ba"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
joke_tuple = ("")

#Functions
def kelvinToCelsius(kelvin):
    return kelvin - 273.15

#Main Code
print("Hello! I'm " + chatbot +"! I'm a basic Python Chatbot!")
username = input("What's your name? ")
print(username + "! " + "The weather is " + weather + " today! I do not recommend you going out!")
while True:
  userinput = input("")
  print(username + ": " + userinput)
  if "weather" in userinput:
    city_name = input("Enter city name : ")
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
      y = x["main"]
      kelvin = y["temp"]
      current_pressure = y["pressure"]
      current_humidity = y["humidity"]
      z = x["weather"]
      cels = round(kelvinToCelsius(kelvin))
      weather_description = z[0]["description"]
      print(" Temperature = " + str(cels) + "\n Atmospheric pressure (in hPa unit) = " + str(current_pressure) + "\n Humidity (in percentage) = " + str(current_humidity) + "\n Description = " + str (weather_description))
    else:
      print(" City Not Found ")
  elif "time is it" in userinput:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
  elif 

    