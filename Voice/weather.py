# import requests
#
# api_address = 'http://api.openweathermap.org/data/2.5/weather?q=Dhaka&appid=7ed5d716646a3e4c917e9f67f4681679'
# json_data = requests.get(api_address).json()
#
# def temp():
#     temperature = round(json_data["main"]["temp"] - 273.15, 1)  # Corrected key to "temp", and converted to Celsius
#     return temperature
#
# def des():
#     description = json_data["weather"][0]["description"]
#     return description

# print(temp())
# print(des())
