#!/usr/bin/python3

def my_var():
	v1 = 42
	v2 = "42"
	v3 = "quarante-deux"
	v4 = 42.0
	v5 = True
	v6 = [42]
	v7 = {42: 42}
	v8 = (42,)
	v9 = set()
	print (f"{v1} has a type {type(v1)}")
	print (f"{v2} has a type {type(v2)}")
	print (f"{v3} has a type {type(v3)}")
	print (f"{v4} has a type {type(v4)}")
	print (f"{v5} has a type {type(v5)}")
	print (f"{v6} has a type {type(v6)}")
	print (f"{v7} has a type {type(v7)}")
	print (f"{v8} has a type {type(v8)}")
	print (f"{v9} has a type {type(v9)}")

if __name__ == '__main__':
	my_var()