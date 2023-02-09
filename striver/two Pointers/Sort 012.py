

########################################################################################
# one pass approach
# We’ll use a three-pointer approach to solve this problem

# The three-pointers will be: current, zeroPos and twoPos.:
#     current - This will hold the position of the current element that we’re on during the iteration of the array. This will be initialised to 0.
#     zeroPos - This will hold the index where we will push any 0s that we may encounter. This will be initialised to 0.
#     twoPos - This will hold the index where we will push any 2s that we may encounter. This will be initialised to n - 1, where n is the size of the array.
# We’ll iterate through the array using the current pointer. Every element is either 0, 1 or 2 so let’s see what we’ll be doing in each of these cases:
#     If arr[current] = 0 - In this case, we need to push the element towards the front of the array. To do that we can swap arr[current] 
# and arr[zeroPos], then we will increase both current and zeroPos by 1.
#     If arr[current] = 1 - In this case, we will just increase the current by 1, since we are only concerned with push 0s to the front
#  and 2s to the end of the array.
#     If arr[current] = 2 - In this case, we need to push the element towards the end of the array. Again, to do this, we’ll just swap 
# arr[current] and arr[twoPos]. We will decrease twoPos by 1. However, in this case, we will not increase the current by 1.
# What will be the condition that must be satisfied so that our loop can end? You might think that it’s when current reaches the end of
#  the array but that’s not the case here. Let’s see why. Can you see what exactly the two pointers, zeroPos and twoPos are doing? As 
# we go through the array, every element before zeroPos is a 0 and every element after twoPos is a 2. Also, every element after zeroPos
#  but before the current is a 1. Therefore, all these elements are ‘sorted’. The element that remains to be sorted is the ones that lie
#  between the indices current and twoPos. Therefore our loop will terminate when the current reaches the value of twoPos.
# Now, let’s understand why we can’t increase the value of current when arr[current] = 2. When we swap arr[current] with arr[twoPos],
#  we don’t know what value was initially at index twoPos (before the swap happened), it could be any of the values 0, 1, or 2. So, we 
# can’t increase the value of current without checking what value was swapped with twoPos. We didn’t have to worry about this in the case 
# where we were swapping arr[current] with arr[zeroPos] because then we would always be swapping 0 and 1.

# Time Complexity

# O(N), where ‘N’ is the size of the array.

# We are only doing a Single Pass of the array.  So Overall Time Complexity is O(N).
def sort012(arr , n):
    zero = 0 
    i = 0
    twos = n-1

    while i <= twos:
        if arr[i] == 0:
            arr[zero] , arr[i] = arr[i] , arr[zero]
            zero += 1
            i +=1
        elif arr[i] == 2:
            arr[twos] , arr[i] = arr[i] , arr[twos]
            twos -=1
        else:
            i+=1

############################################################################################
# two pass approach

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :

	# write your code here
    # don't return anything 
        z = arr.count(0)
        o = arr.count(1)
        t = arr.count(2)
        i = 0
        while z > 0:
            arr[i] = 0
            i+=1
            z-=1
        i = i+z
        while o > 0:
            arr[i] = 1
            i+=1
            o-=1
        i = i+o
        while t > 0:
            arr[i] =2
            t-=1
            i+=1
        
            


#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
