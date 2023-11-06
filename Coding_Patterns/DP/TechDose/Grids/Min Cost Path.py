# Given a cost matrix cost[][] and a position (m, n) in cost[][], 
# write a function that returns cost of minimum cost path to reach (m, n) from (0, 0).
#  Each cell of the matrix represents a cost to traverse through that cell. 
#  The total cost of a path to reach (m, n) is the sum of all the costs on that path 
#  (including both source and destination). You can only traverse down, right and diagonally 
#  lower cells from a given cell, i.e., from a given cell (i, j), cells (i+1, j), (i, j+1), 
#  and (i+1, j+1) can be traversed. 
# You may assume that all costs are positive integers.

# 1) Optimal Substructure 
# The path to reach (m, n) must be through one of the 3 cells: (m-1, n-1) or (m-1, n) or (m, n-1). 
# So minimum cost to reach (m, n) can be written as “minimum of the 3 cells plus cost[m][n]”.
# minCost(m, n) = min (minCost(m-1, n-1), minCost(m-1, n), minCost(m, n-1)) + cost[m][n]

# 2) Overlapping Subproblems 
# Following is a simple recursive implementation of the MCP (Minimum Cost Path) problem. 
# The implementation simply follows the recursive structure mentioned above.  


# Dynamic Programming Python implementation of Min Cost Path
# problem
# A Naive recursive implementation of MCP(Minimum Cost Path) problem
import sys
R = 3
C = 3

# Returns cost of minimum cost path from (0,0) to (m, n) in mat[R][C]


def minCost(cost, m, n):
	if (n < 0 or m < 0):
		return sys.maxsize
	elif (m == 0 and n == 0):
		return cost[m][n]
	else:
		return cost[m][n] + min(minCost(cost, m-1, n-1),
								minCost(cost, m-1, n),
								minCost(cost, m, n-1))

# A utility function that returns minimum of 3 integers */


def min(x, y, z):
	if (x < y):
		return x if (x < z) else z
	else:
		return y if (y < z) else z


# Driver code
cost = [[1, 2, 3],
		[4, 8, 2],
		[1, 5, 3]]
print(minCost(cost, 2, 2))

# This code is contributed by
# Smitha Dinesh Semwal



def minCost(cost, m, n):

	# Instead of following line, we can use int tc[m+1][n+1] or
	# dynamically allocate memoery to save space. The following
	# line is used to keep te program simple and make it working
	# on all compilers.
	tc = [[0 for x in range(len(cost))] for x in range(len(cost[0]))]

	tc[0][0] = cost[0][0]

	# Initialize first column of total cost(tc) array
	for i in range(1, m+1):
		tc[i][0] = tc[i-1][0] + cost[i][0]

	# Initialize first row of tc array
	for j in range(1, n+1):
		tc[0][j] = tc[0][j-1] + cost[0][j]

	# Construct rest of the tc array
	for i in range(1, m+1):
		for j in range(1, n+1):
			tc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j]

	return tc[m][n]


# Driver code
cost = [[1, 2, 3],
		[4, 8, 2],
		[1, 5, 3]]
print(minCost(cost, 2, 2))

# This code is contributed by Bhavya Jain



cost = [ [ 1, 2, 3 ],
             [ 4, 8, 2 ],
             [ 1, 5, 3 ] ]

minCost(cost)


####

 # https://www.geeksforgeeks.org/min-cost-path-dp-6/

# Djikstra 
# Minimum Cost Path using Dijkstra’s shortest path
# algorithm with Min Heap by dinglizeng
# Python3

# Define the number of rows and the number of columns
R = 4
C = 5

# 8 possible moves
dx = [ 1, -1, 0, 0, 1, 1, -1, -1 ]
dy = [ 0, 0, 1, -1, 1, -1, 1, -1 ]

# The data structure to store the coordinates of
# the unit square and the cost of path from the top
# left.
class Cell():
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.cost = z

# To verify whether a move is within the boundary.
def isSafe(x, y):
	return (x >= 0 and x < R and
			y >= 0 and y < C)

# This solution is based on Dijkstra’s shortest
# path algorithm
# For each unit square being visited, we examine all
# possible next moves in 8 directions,
# calculate the accumulated cost of path for each
# next move, adjust the cost of path of the adjacent
# units to the minimum as needed.
# then add the valid next moves into a Min Heap.
# The Min Heap pops out the next move with the minimum
# accumulated cost of path.
# Once the iteration reaches the last unit at the lower
# right corner, the minimum cost path will be returned.
def minCost(cost, m, n):

	# the array to store the accumulated cost
	# of path from top left corner
	dp = [[0 for x in range(C)] for x in range(R)]

	# the array to record whether a unit
	# square has been visited
	visited = [[False for x in range(C)]
				for x in range(R)]

	# Initialize these two arrays, set path cost
	# to maximum integer value, each unit as
	# not visited
	for i in range(R):
		for j in range(C):
			dp[i][j] = float("Inf")
			visited[i][j] = False

	# Define a reverse priority queue.
	# Priority queue is a heap based implementation.
	# The default behavior of a priority queue is
	# to have the maximum element at the top.
	# The compare class is used in the definition of
	# the Min Heap.
	pq = []

	# initialize the starting top left unit with the
	# cost and add it to the queue as the first move.
	dp[0][0] = cost[0][0]
	pq.append(Cell(0, 0, cost[0][0]))

	while(len(pq)):
	
		# pop a move from the queue, ignore the units
		# already visited
		cell = pq[0]
		pq.pop(0)
		x = cell.x
		y = cell.y
		if(visited[x][y]):
			continue

		# mark the current unit as visited
		visited[x][y] = True

		# examine all non-visited adjacent units in 8
		# directions
		# calculate the accumulated cost of path for
		# each next move from this unit,
		# adjust the cost of path for each next
		# adjacent units to the minimum if possible.
		for i in range(8):
			next_x = x + dx[i]
			next_y = y + dy[i]
			if(isSafe(next_x, next_y) and
				not visited[next_x][next_y]):
				dp[next_x][next_y] = min(dp[next_x][next_y],
										dp[x][y] + cost[next_x][next_y])
				pq.append(Cell(next_x, next_y,
								dp[next_x][next_y]))

	# return the minimum cost path at the lower
	# right corner
	return dp[m][n]

# Driver code
cost = [[1, 8, 8, 1, 5],
		[4, 1, 1, 8, 1],
		[4, 2, 8, 8, 1],
		[1, 5, 8, 8, 1]]
print(minCost(cost, 3, 4))
