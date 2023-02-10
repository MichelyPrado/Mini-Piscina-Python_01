#!/usr/bin/python3

def my_file():
	print(open('numbers.txt', 'r').read().replace(',', '\n'))

if __name__ == '__main__':
	my_file()
