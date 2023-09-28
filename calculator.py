#!/usr/bin/env python3
""" Ngaira Edwin Wisiuva  SCT 211-0543/2022"""
"""A simple claculator in python"""

def calculator():
	while True:
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
