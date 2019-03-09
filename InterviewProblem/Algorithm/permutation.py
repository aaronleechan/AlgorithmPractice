'''
Permutation
'''

def permute(nums):
	results = []
	dfs(nums,[],results)
	return results

def dfs(nums,temp,results):

	# print(len(temp),len(nums))

	if len(temp) == len(nums):
		results.append(temp[:])
		return

	for i in range(0,len(nums)):
		if nums[i] not in temp:
			temp.append(nums[i])
			dfs(nums,temp,results)
			temp.pop()


def permute2(nums):
	if len(nums) == 0:
		return [[]]
	results = []
	nums.sort()
	visited = [[False] for i in range(len(nums))]
	dfs2(nums,[],results,visited)
	return results

def dfs2(nums,temp,results,visited):
	if len(temp) == len(nums):
		print({"***************": temp[:]})
		results.append(temp[:])
		

	for i in range(len(nums)):
		if visited[i]:
			continue
		if i !=  0 and visited[i-1] and nums[i-1] == nums[i]:
			continue
		visited[i] = True
		temp.append(nums[i])
		dfs2(nums,temp,results,visited)
		visited[i] = False
		temp.pop()


def main():
    array = [1,2]
    test = [1,1,2,1]
    # result = permute(array)
    result = permute2(test)
    print(result)


if __name__ == "__main__":
    main()