
def TwoSum(v,t):
	
	hashValue={}
	for i in range (len(v)):
		if t - v[i] in hashValue:
			return [hashValue[t-v[i]],i]
		hashValue[v[i]] = i
	return [-1,-1]



def main():
    test1 = [2,7,11,15]
    target = 9
    print(TwoSum(test1,target))


if __name__ == "__main__":
    main()