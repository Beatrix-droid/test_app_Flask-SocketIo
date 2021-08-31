import datetime
from datetime import date
import requests


current_weather_key = "e2b47a49d350e13324ce145b3150ff64"
forecast_weather_key = "4091bf2f13288d7db6dcbd810212f5d9"


#creating the current weather part of the app:


def get_current_weather(city_name, current_weather_key):

	URL= f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={current_weather_key}"
	url_link = requests.get(URL)

	current_weather_data = url_link.json()
	#print(current_weather_data)

	if current_weather_data["cod"] == "404":
		 return "City not found. Please re-enter the name of the city you'd wish to find the weather of."

	country = current_weather_data["sys"]["country"]
	city = current_weather_data["name"]

	kelvin_temp = current_weather_data["main"]["temp"]
	celsius_temp = round(int(kelvin_temp) - 273.15, 1)
	fahrenheit_temp = round((int(kelvin_temp) * (9/5)) - 459.67, 2)

	feels_like_temp = current_weather_data["main"]["feels_like"]
	feels_like_C = round(int(feels_like_temp) - 273.15, 1)
	feels_like_F = round((int(feels_like_temp) * (9/5)) - 459.67)

	sky_description = current_weather_data["weather"][0]["description"]
	today = date.today()
	todays_time = datetime.time()

	result = f"The temperature in {city} ({country}) is: {celsius_temp} celsius or {feels_like_F} fahrenheit. \n " \
			f"The perceived temperature is: {feels_like_C} celsius or {feels_like_F} fahrenheit.\n" \
			f"The sky is {sky_description}"

	return str(today) + " " + str(todays_time) + "\n " + result





def get_forecast(forcast_city, forecast_weather_key):

	forecast_URL = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?q={forcast_city}&appid={forecast_weather_key}"

	url_link = requests.get(forecast_URL)

	current_weather_data = url_link.json()
	#print(current_weather_data)

	if current_weather_data["cod"] == "404":
		 return "City not found. Please re-enter the name of the city you'd wish to find the weather of."

	country = current_weather_data["city"]["country"]
	city = current_weather_data["city"]["name"]

	kelvin_temp = current_weather_data["main"]["temp"]
	celsius_temp = round(int(kelvin_temp) - 273.15, 1)
	fahrenheit_temp = round((int(kelvin_temp) * (9/5)) - 459.67, 2)

	feels_like_temp = current_weather_data["main"]["feels_like"]
	feels_like_C = round(int(feels_like_temp) - 273.15, 1)
	feels_like_F = round((int(feels_like_temp) * (9/5)) - 459.67)

	sky_description = current_weather_data["weather"][0]["description"]
	today = date.today()
	todays_time = datetime.time()

	result = f"The temperature in {city} ({country}) will be: {celsius_temp} celsius or {feels_like_F} fahrenheit. \n " \
			f"The perceived temperature will be: {feels_like_C} celsius or {feels_like_F} fahrenheit.\n" \
			f"The sky will be {sky_description}"

	return str(today) + " " + str(todays_time) + "\n " + result



print(get_current_weather("Milan", current_weather_key))
print(get_forecast("Milan", forecast_weather_key))