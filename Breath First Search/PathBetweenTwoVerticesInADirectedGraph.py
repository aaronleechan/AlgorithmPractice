from collections import defaultdict

class Graph:
	print("come in ? ")

	def __init__(self,vertices):
		self.V = vertices
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

	#Use BFS to check path between s and d
	def isReachable(self,s,d):
		#Mark all the vertices as not visited
		visited = [False]*(len(self.graph))
		print({"visited": visited})

		#Create a queue for BFS
		queue = []

		#Mark the source node as visited and enqueu it
		queue.append(s)
		visited[s] = True

		while queue:
			
			#Deque a vertex from queue
			n = queue.pop(0)
			print({"n": n})

			#if this adjacent node is the destination node,
			if n == d:
				return True

			#Else, continue to do BFS
			for i in self.graph[n]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True





g = Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,0)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

u = 1; v = 3

if g.isReachable(u,v):
	print('There is a path from %d to %d' % (u,v))
else:
	print('There is no a path from %d to %d' % (u,v))

u = 3; v = 1

if g.isReachable(u,v):
	print("There is a path from %d to %d" % (u,v))
else:
	print("There is no path from %d to %d" % (u,v))

