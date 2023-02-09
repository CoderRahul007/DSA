# Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island.
#  For example, the below matrix contains 5 islands

# Example: 

# Input : mat[][] = {{1, 1, 0, 0, 0},
#                    {0, 1, 0, 0, 1},
#                    {1, 0, 0, 1, 1},
#                    {0, 0, 0, 0, 0},
#                    {1, 0, 1, 0, 1}}
# Output : 5

# This is a variation of the standard problem: “Counting the number of connected components
#  in an undirected graph”. 

# Before we go to the problem, let us understand what is a connected component.
#  A connected component of an undirected graph is a subgraph in which every two 
# vertices are connected to each other by a path(s), and which is connected to no 
# other vertices outside the subgraph. 
# For example, the graph shown below has three connected components. 
 

# Find the number of islands
 
# Recommended PracticeFind the number of islandsTry It!

# A graph where all vertices are connected with each other has exactly one connected component,
#  consisting of the whole graph. Such a graph with only one connected component is called a Strongly Connected Graph.
# The problem can be easily solved by applying DFS() on each component. In each DFS() call,
#  a component or a sub-graph is visited. We will call DFS on the next un-visited component.
#  The number of calls to DFS() gives the number of connected components. BFS can also be used.

# What is an island? 

# A group of connected 1s forms an island. For example, the below matrix contains 4 islands
 

# island
# Recommended PracticeFind the number of islandsTry It!

# A cell in 2D matrix can be connected to 8 neighbours. So, unlike standard DFS(),
#  where we recursively call for all adjacent vertices, here we can recursively call 
# for 8 neighbours only. We keep track of the visited 1s so that they are not visited again. 

### DFS 

# Program to count islands in boolean 2D matrix
class Graph:

	def __init__(self, row, col, g):
		self.ROW = row
		self.COL = col
		self.graph = g

	# A function to check if a given cell
	# (row, col) can be included in DFS
	def isSafe(self, i, j, visited):
		# row number is in range, column number
		# is in range and value is 1
		# and not yet visited
		return (i >= 0 and i < self.ROW and
				j >= 0 and j < self.COL and
				not visited[i][j] and self.graph[i][j])
			

	# A utility function to do DFS for a 2D
	# boolean matrix. It only considers
	# the 8 neighbours as adjacent vertices
	def DFS(self, i, j, visited):

		# These arrays are used to get row and
		# column numbers of 8 neighbours
		# of a given cell
		rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1];
		colNbr = [-1, 0, 1, -1, 1, -1, 0, 1];
		
		# Mark this cell as visited
		visited[i][j] = True

		# Recur for all connected neighbours
		for k in range(8):
			if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
				self.DFS(i + rowNbr[k], j + colNbr[k], visited)


	# The main function that returns
	# count of islands in a given boolean
	# 2D matrix
	def countIslands(self):
		# Make a bool array to mark visited cells.
		# Initially all cells are unvisited
		visited = [[False for j in range(self.COL)]for i in range(self.ROW)]

		# Initialize count as 0 and traverse
		# through the all cells of
		# given matrix
		count = 0
		for i in range(self.ROW):
			for j in range(self.COL):
				# If a cell with value 1 is not visited yet,
				# then new island found
				if visited[i][j] == False and self.graph[i][j] == 1:
					# Visit all cells in this island
					# and increment island count
					self.DFS(i, j, visited)
					count += 1

		return count


graph = [[1, 1, 0, 0, 0],
		[0, 1, 0, 0, 1],
		[1, 0, 0, 1, 1],
		[0, 0, 0, 0, 0],
		[1, 0, 1, 0, 1]]


row = len(graph)
col = len(graph[0])

g = Graph(row, col, graph)

print ("Number of islands is:")
print (g.countIslands())

# Time complexity: O(ROW x COL)
# Auxiliary Space: O(ROW x COL), due to visited matrix

###################################################################################
# Program to count islands in boolean 2D matrix
# Changing the matrix
class Graph:

	def __init__(self, row, col, graph):
		self.ROW = row
		self.COL = col
		self.graph = graph

	# A utility function to do DFS for a 2D
	# boolean matrix. It only considers
	# the 8 neighbours as adjacent vertices
	def DFS(self, i, j):
		if i < 0 or i >= len(self.graph) or j < 0 or j >= len(self.graph[0]) or self.graph[i][j] != 1:
			return

		# mark it as visited
		self.graph[i][j] = -1

		# Recur for 8 neighbours
		self.DFS(i - 1, j - 1)
		self.DFS(i - 1, j)
		self.DFS(i - 1, j + 1)
		self.DFS(i, j - 1)
		self.DFS(i, j + 1)
		self.DFS(i + 1, j - 1)
		self.DFS(i + 1, j)
		self.DFS(i + 1, j + 1)

	# The main function that returns
	# count of islands in a given boolean
	# 2D matrix
	def countIslands(self):
		# Initialize count as 0 and traverse
		# through the all cells of
		# given matrix
		count = 0
		for i in range(self.ROW):
			for j in range(self.COL):
				# If a cell with value 1 is not visited yet,
				# then new island found
				if self.graph[i][j] == 1:
					# Visit all cells in this island
					# and increment island count
					self.DFS(i, j)
					count += 1

		return count


graph = [
	[1, 1, 0, 0, 0],
	[0, 1, 0, 0, 1],
	[1, 0, 0, 1, 1],
	[0, 0, 0, 0, 0],
	[1, 0, 1, 0, 1]
]


row = len(graph)
col = len(graph[0])

g = Graph(row, col, graph)

print("Number of islands is:", g.countIslands())

#  Time complexity: O(ROW x COL)
# Auxiliary Space: O(1), as we are not using any extra space.


######################################################################################
### BFS

# A BFS based solution to count number of
# islands in a graph.
from collections import deque

# A function to check if a given cell
# (u, v) can be included in DFS
def isSafe(mat, i, j, vis):
	
	return ((i >= 0) and (i < 5) and
			(j >= 0) and (j < 5) and
		(mat[i][j] and (not vis[i][j])))

def BFS(mat, vis, si, sj):
	
	# These arrays are used to get row and
	# column numbers of 8 neighbours of
	# a given cell
	row = [-1, -1, -1, 0, 0, 1, 1, 1]
	col = [-1, 0, 1, -1, 1, -1, 0, 1]

	# Simple BFS first step, we enqueue
	# source and mark it as visited
	q = deque()
	q.append([si, sj])
	vis[si][sj] = True

	# Next step of BFS. We take out
	# items one by one from queue and
	# enqueue their univisited adjacent
	while (len(q) > 0):
		temp = q.popleft()

		i = temp[0]
		j = temp[1]

		# Go through all 8 adjacent
		for k in range(8):
			if (isSafe(mat, i + row[k], j + col[k], vis)):
				vis[i + row[k]][j + col[k]] = True
				q.append([i + row[k], j + col[k]])

# This function returns number islands (connected
# components) in a graph. It simply works as
# BFS for disconnected graph and returns count
# of BFS calls.
def countIslands(mat):
	
	# Mark all cells as not visited
	vis = [[False for i in range(5)]
				for i in range(5)]
	# memset(vis, 0, sizeof(vis));

	# 5all BFS for every unvisited vertex
	# Whenever we see an univisted vertex,
	# we increment res (number of islands)
	# also.
	res = 0

	for i in range(5):
		for j in range(5):
			if (mat[i][j] and not vis[i][j]):
				BFS(mat, vis, i, j)
				res += 1

	return res

# Driver code
if __name__ == '__main__':
	
	mat = [ [ 1, 1, 0, 0, 0 ],
			[ 0, 1, 0, 0, 1 ],
			[ 1, 0, 0, 1, 1 ],
			[ 0, 0, 0, 0, 0 ],
			[ 1, 0, 1, 0, 1 ]]

	print (countIslands(mat))


