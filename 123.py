from colorama import init
# use Colorama to make Termcolor work on Windows too
init()
from colorama import Fore, Back, Style
print(Fore.BLACK)
print (Back.CYAN)
a=float (input ('введи первое число: '))
b=float (input ('введи второе число: '))
print (Back.GREEN)
what=input ("что ты хочешь выполнить +:")
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
else:
	print ('неверная операция')

