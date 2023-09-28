#!/usr/bin/env python3

"""A simple claculator in python"""

def calculator():
	a, operator, c =input("Enter numbers: ").split()

	a = int(a)
	c = int(c)

	if operator == "+":
		print("{}".format(a+c))
	elif operator == "-":
		print("{}".format(a-c))
	elif operator == "/":
		print("{}".format(a/c))
	elif operator == "x":
		print("{}".format(a*c))
	elif operator == "**":
		print("{}".format(a**c))
	else:
		print("Use appropriate symbols")

if __name__ == "__main__":
	calculator()
