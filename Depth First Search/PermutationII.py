class Permutation:

	def permutationTwo(self,value):
		print(value)
		self.results = []
		self.visited = { i: False for i in range(len(value))}
		print(self.visited)
		self.dfs([],sorted(value))
		return self.results

	def dfs(self,path,nums):
		if len(path) == len(nums):
			print(path[:])
			print("-----------------")
			self.results.append(path[:])
			print({"******************************* ": self.results})
			return

		for i in range(len(nums)):
			print({"i": i},{"len(nums)": len(nums)},{"visited": self.visited[i]},{"Nums": nums[i]})
			if self.visited[i]:
				continue

			if i != 0 and nums[i] == nums[i-1] and self.visited[i-1]:
				continue

			self.visited[i] = True
			path.append(nums[i])
			print({"******************************* ": path})
			self.dfs(path,nums)
			print({"****************************]]]]]]* ": i})
			path.pop()
			print({"Outside:": path})
			self.visited[i] = False
			print({"visited change": self.visited})
			print({"Result Path": self.results})



test1 = [1,2]
test2 = [1,1,2]
p = Permutation()
print(p.permutationTwo(test2))