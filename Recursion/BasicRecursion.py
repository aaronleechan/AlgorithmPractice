def printFun(test):
	if(test < 1):
		return
	else:
		printFun(test-1)
		print(test)
		return

def fun1(x,y):
	if( x == 0):
		print(y)
		return y
	else: 
		return fun1(x-1,x+y)


def fun2(v):
	if v == 0:
		return
	n = v/2
	print(n)
	fun2(n)
	printf("%d", n%2)




# test = 3

# printFun(3)
# print("**********end of printFun*************************")
# fun1(5,10)
# print("**********end of fun1*************************")
lintcode22([[1,1],2,[1,1]])
