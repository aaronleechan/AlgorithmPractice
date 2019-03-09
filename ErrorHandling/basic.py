def add(n1,n2):
	print(n1+n2)


try:
	#want to attempt this code
	add(1,2)
	add(1,2,3,4,5)
except Exception as e:# catch *all* exceptions:
	print(e)
else: # it will come when there is no error
	print("Add went well")

