#Calculator v1

from colorama import init
from colorama import Fore, Back, Style
init()
print( Back.YELLOW )
what = input("Что делаем? (+,-,*,/): " )
print( Back.RED )
a = float( input("веди первое число: ") )
b = float( input("веди второе число: ") )

print( Back.CYAN )

if what == "+":
	c = a + b
	print("Результат: " + str(c))

elif what == "-":
	c = a - b
	print("Результат: " + str(c))

elif what == "*":
	c = a * b
	print("Результат: " + str(c))

elif what == "/":
	c = a / b
	print("Результат: " + str(c))

else:
	print( Back.BLACK )
	print("Error")
input ()


