class Graph:
	def __init__(self,row,col,g):
		self.ROW = row
		self.COL = col
		self.graph = g

	# A function to check if a given cell
	# ( row, col) can be included in DFS
	def isSafe(self,i,j,visited):
		return (i >= 0 and i < self.ROW and 
				j >= 0 and j < self.COL and 
				not visited[i][j] and self.graph[i][j])


	def DFS(self,i,j,visited):
		rowNbr = [ -1,	-1,	-1,	 0,	0,	1,	1,	1	];
		colNbr = [ -1,	 0,	 1,	-1,	1, -1,	0,	1	];

		visited[i][j] = True
		print({"i": i},{"J": j})
	# 	for k in range(8):
		for k in range(8):
			print({"k": k},{"rowNbr": rowNbr[k]},{"colNbr": colNbr[k]})
			print(self.isSafe(i + rowNbr[k], j + colNbr[k], visited))
			if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
				self.DFS(i+rowNbr[k] , j + colNbr[k],visited)


	def countIsLands(self):
		# Make a bool array to mark visited cells 
		# Initially all cells are visited
		visited = [[False for j in range(self.COL)] for i in range(self.ROW)]
		print(visited)

		# Initialize count as 0 and traverse
		# through the all cells of
		# given matrix
		count = 0
		for i in range(self.ROW):
			for j in range(self.COL):
				if visited[i][j] == False and self.graph[i][j] == 1:
					#visit all cells in this island
					print({"i": i},{"j": j},{"SELF.GRAPH": self.graph[i][j]})
					self.DFS(i,j,visited)
					count += 1
					print("*********************************************")

		return count



graph = [[1,	1,	0,	0,	0],
		 [0,	1,	0,	0,	1],
		 [1,	0,	0,	1,	1],
		 [0,	0,	0,	0,	0],
		 [1,	0,	1,	0,	1]]

row = len(graph)
col = len(graph[0])
g = Graph(row, col, graph)
print("Number of island is: ")
g.countIsLands()
# print g.countIsLands()


