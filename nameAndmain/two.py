import one
print("TOP LEVEL IN TWO.py")
one.func()

if __name__ == '__main__':
	print("TWO.py is being directly")
else:
	print("TWo.py has been imported")