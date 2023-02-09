
# Min And Max Heap Approach

# The idea is to maintain two equal halves of the current stream: the higher half 
# containing greater valued elements, and the lower half containing lower valued element.
#  For each new addition, the transition between elements in the two halves goes this way:

#     If the new element is less than the maximum element of the lower half, then this element
#  gets added to the lower half.

# After the addition, if the difference between the sizes of the two halves becomes greater than 1, 
# then to maintain the balance, the maximum element is removed from the lower half and added to the higher half. 

#     2. If the new element is greater than the maximum element of the lower half, then this element
#  gets added to the higher half. 

# Now, if the difference between the sizes of the two halves becomes greater than 1, to maintain balance, 
# the minimum element of the higher half is removed and added to the lower half.

# By maintaining the halves in this way, we assure that the elements of the stream are equally distributed 
# between the two halves.

# Hence, after each addition the maximum element of the lower half and the minimum element of the higher 
# half become the middle-most elements, which we can use to compute the median. 
# Considering the odd elements case, whichever half has more elements, the maximum of lower half or minimum 
# of higher half will be the median. 
# Considering the even elements case, average of maximum of lower half and minimum of higher half will be the 
# median.
# How can we store these elements in a way that supports this functionality? We can create a max heap for the 
# lower half, and a min heap for the upper half.
# Time Complexity

# O(N * log(N)), where N is the number of elements in the array.

 

# There are N additions, and each new addition takes O(log(N)) time for transition (insertion/deletion) 
# of elements between the two heaps. Hence, the overall Time Complexity is O(N * log(N)). 
# Space Complexity

# O(N), where N is the number of elements in the array.

 

# Maintaining the two heaps will require O(N) memory. Hence, the overall Space Complexity is O(N).


"""
    Time Complexity: O(N * log(N) )
    Space Complexity: O(N)
    
    where N is the number of elements in the array.
"""

from queue import PriorityQueue
INT_MAX = 10000000000

def findMedian(arr, n):

    # We want lowerHalf to be a max heap, we will be inserting negative values
    lowerHalf = PriorityQueue()
    higherHalf = PriorityQueue()

    # The variable size is the size of the current stream
    for size in range(1, n + 1):

        x = INT_MAX

        """
            The get() function is used to get the top element
            The put() function is used to insert the element
        """
        if (lowerHalf.qsize() > 0):

            x = abs(lowerHalf.get())
            lowerHalf.put(-x)

        if (lowerHalf.qsize() > 0 and x > arr[size - 1]):

            # Insert ARR[size-1] in lowerHalf
            lowerHalf.put(-(arr[size - 1]))

            if (lowerHalf.qsize() > higherHalf.qsize() + 1):

                # Insert the top element of lowerHalf into higherHalf
                higherHalf.put(abs(lowerHalf.get()))

        else:

            higherHalf.put(arr[size - 1])

            if (higherHalf.qsize() > lowerHalf.qsize() + 1):

                # Insert the top element of higherHalf into lowerHalf
                lowerHalf.put(-(higherHalf.get()))

        # Check if size is odd
        if (size % 2 == 1):

            if (higherHalf.qsize() > lowerHalf.qsize()):

                median = higherHalf.get()
                higherHalf.put(median)

            else:

                median = abs(lowerHalf.get())
                lowerHalf.put(-median)

        else:
            
            a = lowerHalf.get()
            lowerHalf.put(a)
            b = higherHalf.get()
            higherHalf.put(b)

            median = (abs(a) + b) // 2

        # Print the variable median
        print(median, end=" ")
