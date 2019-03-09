def flatten(test):
	stack = [test]
	flatten_list = []

	while stack:
		top = stack.pop()
		if isinstance(top,list):
			for elem in reversed(top):
				stack.append(elem)
		else:
			flatten_list.append(top)

	return flatten_list

def permutaton(test):
	print("Come in here")
	if test is None:
		return []

	if test is []:
		return [[]]

	result = []
	testpermutation(result, [], sorted[test])
	return result

def testpermutation(result,temp,test):
	print("permutaton permutaton permutaton")

		if test == []:
			result += [temp]
		else:
			for i in range(len(test)):
				print("Hello world")
				testpermutation(result,temp+[nums[i]], nums[:i] + nums[i+1:])






# test1 = [[1,1],2,[1,1]]
test2 = [1]
test3 = [1,2,3]
test4 = [1,2,3,4]
# flatten(test1)
permutaton(test2)
print("***************************")
permutaton(test3)
print("***************************")
permutaton(test4)