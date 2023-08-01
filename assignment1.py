# Enter your API key here
api_key = "Your_API_Key"


base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

# city is not found
if x["cod"] != "404":

	y = x["main"]

	current_weather = y["weather"]

	current_pressure = y["pressure"]

	current_windspeed = y["wind speed"]

	# store the value of "weather"
	# key in variable z
	z = x["weather"]

	# store the value corresponding
	# to the "description" key at
	# the 0th index of z
	weather_description = z[0]["description"]

	# print following values
	print(" Temperature (in kelvin unit) = " +
					str(current_weather) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_windspeed) +
		"\n description = " +
					str(weather_description))

else:
	print(" City Not Found ")
