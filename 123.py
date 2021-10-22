#импортирование колорама для изменения цвета букв и заднего фона
from colorama import init
# use Colorama to make Termcolor work on Windows too
init()
from colorama import Fore, Back, Style
#задний фон и цвет букв
print(Fore.BLACK)
print (Back.CYAN)
#ввод первого числа
a=float (input ('введи первое число: '))
#ввод второго числа
b=float (input ('введи второе число: '))
#задний фон результата зеленый
print (Back.GREEN)
#переменная которая спрашивает какую операцию провести
what=input ("что ты хочешь выполнить +;/;*;-:")
#различные операции в зависимости от значения if
if what=='+':
	c=a+b
	print ('резултат'+ str(c))
elif what == '-' :
	c=a-b
	print ('результат '+ str(c))
elif what =="/":
	c=a/b
	print ('результат '+ str(c))
elif what =="*":
	c=a*b
	print ('результат '+ str(c))
#вывод при неверно выбраном what
else:
	print ('неверная операция')

