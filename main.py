# ax^2+bx+c=0

from math import sqrt
from os import system


def solve_two_drage(a, b, c):
	try:

		delta = (b**2)-(4*a*c)

		if delta > 0:
			x1 = -b+sqrt(delta)/2*a

			x2= -b-sqrt(delta)/ 2*a

			print(x1,x2)




		elif delta==0:
			x= -b/2*a

			print(x)


		else:

			print("delta<0")

	except (ValueError, TypeError):
		print("your values has incorrect")





a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))

solve_two_drage(a,b,c)

system("pause")
