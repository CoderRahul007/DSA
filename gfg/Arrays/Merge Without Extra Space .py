# https://takeuforward.org/data-structure/merge-two-sorted-arrays-without-extra-space/
# https://www.geeksforgeeks.org/merge-two-sorted-arrays-o1-extra-space/


# Method-5 [Insertion Sort with Simultaneous Merge]

# Approach:

# 1. sort list 1 by always comparing with head/first of list 2 and swapping if required
# 2. after each head/first swap, perform insertion of the swapped element into correct position in list 2 
# which will eventually sort list 2 at the end. 

# For every swapped item from list 1, perform insertion sort in list 2 to 
# find its correct position so that when list 1 is sorted, list 2 is also sorted.



# "Insertion sort of list 2 with swaps from list 1"
#
# swap elements to get list 1 correctly, meanwhile
# place the swapped item in correct position of list 2
# eventually list 2 is also sorted
# Time = O(m*n) or O(n*m)
# AUX = O(1)
def merge(arr1, arr2):
	x = arr1; y = arr2
	end = len(arr1)
	i = 0
	while(i < end):				 # O(m) or O(n)
		if(x[i] > y[0]):
			swap(x,y,i,0)
			insert(y,0)			 # O(n) or O(m) number of shifts
		i+=1

# O(n):
def insert(y, i):
	orig = y[i]
	i+=1
	while (i<len(y) and y[i]<orig):
		y[i-1] = y[i]
		i+=1
	y[i-1] = orig

def swap(x,y,i,j):
	temp = x[i]
	x[i] = y[j]
	y[j] = temp

def test():
	c1 = [2, 3, 8, 13]
	c2 = [1, 5, 9, 10, 15, 20 ]
	for _ in range(2):
		merge(c1,c2)
		print(c1,c2)
		c1, c2 = c2, c1

test()
