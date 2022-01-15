import pyowm
from colorama import init
from colorama import Fore, Back, Style

owm = pyowm.OWM('0be0de8b3dfcdecb0d25517208677e8d', language = "ru")
print(Back.GREEN)
place = input("В каком городе ви?: ")

observation = owm.weather_at_place(place)
w = observation.get_weather()



temp = w.get_temperature("celsius")["temp"]
print(Back.YELLOW)
print("В городе " + place + " сейчас " + w.get_detailed_status())
print(Back.CYAN)
print("Температура сейчас в вашем городе: " + str(temp))

if temp < 10:
	print(Back.BLUE)
	print("Сейчас холодна на улице, одивайся потеплей!")

elif temp < 20:
	print(Back.GREEN)
	print("Температура нормальная одивайся как хочеш :)")

elif temp < 30:
	print(Back.CYAN)
	print("Температура хорошая иди прогуляйся по улице :)")

elif temp < 40:
	print(Back.RED)
	print("На улице пекло сиди в дома под кандицианером")



