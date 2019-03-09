'''
Subset
'''
def subset(nums):
	nums = sorted(nums)
	results = []
	dfs(nums,0,[],results)
	return results

def dfs(nums,i,temp,results):
	results.append(list(temp))
	for i in range(i,len(nums)):
		temp.append(nums[i])
		dfs(nums,i+1,temp,results)
		temp.pop()


def main():
    test = [1,2]
    result = 0
    result = subset(test)
    
    print(result)


if __name__ == "__main__":
    main()