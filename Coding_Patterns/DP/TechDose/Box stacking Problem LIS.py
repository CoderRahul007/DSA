# You are given a set of n types of rectangular 3-D boxes, where the i^th box has height 
# h(i), width w(i) and depth d(i) (all real numbers). You want to create a stack of boxes
#  which is as tall as possible, but you can only stack a box on top of another box if the
#   dimensions of the 2-D base of the lower box are each strictly larger than those of the
#    2-D base of the higher box. Of course, you can rotate a box so
#  that any side functions as its base. It is also allowable to use multiple instances of 
#  the same type of box. 

# We need to build a maximum height stack. 
# Following are the key points to note in the problem statement: 
# 1) A box can be placed on top of another box only if both width and 
# depth of the upper placed box are smaller than width and depth of the lower box respectively. 
# 2) We can rotate boxes such that width is smaller than depth. For example, 
# if there is a box with dimensions {1x2x3} where 1 is height, 2×3 is base, 
# then there can be three possibilities, {1x2x3}, {2x1x3} and {3x1x2} 
# 3) We can use multiple instances of boxes. What it means is, we can have two 
# different rotations of a box as part of our maximum height stack.

# Method 1 : dynamic programming using tabulation

# 1) Generate all 3 rotations of all boxes. The size of rotation array
#  becomes 3 times the size of the original array. 
# For simplicity, we consider width as always smaller than or equal to depth. 
# 2) Sort the above generated 3n boxes in decreasing order of base area.
# 3) After sorting the boxes, the problem is same as LIS with following optimal substructure property. 
# MSH(i) = Maximum possible Stack Height with box i at top of stack 
# MSH(i) = { Max ( MSH(j) ) + height(i) } where j < i and width(j) > width(i) and depth(j) > depth(i). 
# If there is no such j then MSH(i) = height(i)
# 4) To get overall maximum height, we return max(MSH(i)) where 0 < i < n
# Following is the implementation of the above solution. 
 
# Dynamic Programming implementation
# of Box Stacking problem
from sqlite3 import Time


class Box:
	
	# Representation of a box
	def __init__(self, h, w, d):
		self.h = h
		self.w = w
		self.d = d

	def __lt__(self, other):
		return self.d * self.w < other.d * other.w

def maxStackHeight(arr, n):

	# Create an array of all rotations of
	# given boxes. For example, for a box {1, 2, 3},
	# we consider three instances{{1, 2, 3},
	# {2, 1, 3}, {3, 1, 2}}
	rot = [Box(0, 0, 0) for _ in range(3 * n)]
	index = 0

	for i in range(n):

		# for each rotation side will be diff
		# Copy the original box
		rot[index].h = arr[i].h
		rot[index].d = max(arr[i].d, arr[i].w) # max of d and w
		rot[index].w = min(arr[i].d, arr[i].w) # min of d and w
		index += 1

		# every time the side will be different
		# First rotation of the box
		rot[index].h = arr[i].w
		rot[index].d = max(arr[i].h, arr[i].d)
		rot[index].w = min(arr[i].h, arr[i].d)
		index += 1

		# Second rotation of the box
		rot[index].h = arr[i].d
		rot[index].d = max(arr[i].h, arr[i].w)
		rot[index].w = min(arr[i].h, arr[i].w)
		index += 1

	# Now the number of boxes is 3n
	n *= 3

	# Sort the array 'rot[]' in non-increasing
	# order of base area decreasing order
	rot.sort(reverse = True)

	# Uncomment following two lines to print
	# all rotations
	for i in range(n):
		print(rot[i].h, 'x', rot[i].w, 'x', rot[i].d)

	# Initialize msh values for all indexes
	# msh[i] --> Maximum possible Stack Height
	# with box i on top
	msh = [0] * n

	for i in range(n):
		msh[i] = rot[i].h

	# Compute optimized msh values
	# in bottom up manner
	for i in range(1, n):
		for j in range(0, i):
			if (rot[i].w < rot[j].w and rot[i].d < rot[j].d): # previos value is greater than next
				# A box can be placed on top of another box only if both width and 
				# depth of the upper placed box are smaller than width and depth of the lower box respectively. 
				msh[i] = max(msh[i] , msh[j] + rot[i].h )	
				# add the height				

	return max(msh[i])


if __name__ == "__main__":
	arr = [Box(4, 6, 7), Box(1, 2, 3),
		Box(4, 5, 6), Box(10, 12, 32)]
	n = len(arr)
	print("The maximum possible height of stack is",
		maxStackHeight(arr, n))

#Time - O(n^2)