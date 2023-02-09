####################################################################################################

#  Modifying Array IN-PLACE

# For this approach we use the array indices to store the visited state of each number. 
# We know that only the duplicate element would be visited more than once. For each number
#  we go to its index position and multiply it with ’-1’, thus making it negative. 
# In case of duplicate, it will visit twice and hence will become positive, which will be returned.

# Example:     Input: 2 4 1 5 3 6 8 7 4

# Explanation: 

# Traverse from start and multiply each element with ‘-1’ and checking if after multiplication 
# it becomes positive then return it.

# 2 4 1 5 3 6 8 7 4

# -2 -4 -1 -5 -3 -6 -8 -7 4

# 4 is positive hence return 4

# Output: 

# 4
# Time Complexity

# O(N), where N is the length of the array.

 

# We need to traverse the array only once hence, in the worst case the complexity will be O(N).
# Space Complexity

# O(1), Constant space is required.

def findDuplicate(arr, n):
    
    # For each value of array perform.
    for i in range(n):
        
        # Use array indices to store visited state of each element.
        index = abs(arr[i]) - 1
        
        # Mark as visited by multiplying with '-1'.
        arr[index] *= -1
        
        # In case of duplicate, this will become +ve.
        if arr[index] > 0:
            
            # Return duplicate element.
            return abs(arr[i])
            
            
    return -1
            
######################################################################################################
# For this approach, we divide the whole process into two phases and use two pointers named tortoise and hare.. 

# Phase 1(Find the intersection point): The hare would be twice as fast as the tortoise.
#  Hence, HARE = ARR[ARR[HARE]] and TORTOISE = ARR[TORTOISE]. Since the tortoise is slow,
#   the hare would catch it at some point, this point will be our intersection point.
#    Note that the intersection point may not be equal to the starting point of the loop. 

# Example: ARR = 2 4 1 5 3 6 8 7 4


# Hare: 2 1 3 8 4 5 6 7

# Tortoise: 2 4 1 5 3 6 8 7

# In the above array, we can see that the intersection point of hare and tortoise
#  will be 7 but the starting point of the loop is 4.

# After finding the intersection point, we start with the second phase:

# Phase 2: 

# Now, we reduce the speed of the hare and make it equal to the speed of the tortoise,
#  meaning now HARE = ARR[HARE] and TORTOISE = ARR[TORTOISE]. The tortoise starts from 
#  the start of the array, while the hare starts from the intersection point found in 
#  the first phase. Now, the point where the hare and the tortoise intersect will be the
#   starting point of the loop which is the repeated element and hence returned.
# Time Complexity

# O(N), where N is the length of the array.

 

# The time complexity of this algorithm is linear, hence O(N).
# Space Complexity

# O(1), Constant space is required.

# https://www.youtube.com/watch?v=PvrxZaH_eZ4

def findDuplicate(arr, n):
    
    # Initialise tortoise and hare pointers.
    tortoise = arr[0]
    hare = arr[0]
    
    tortoise = arr[tortoise]
    hare = arr[arr[hare]]
    
    # Find the intersection point of the two runners.
    while tortoise != hare:
        # Hare pointer moves twice as fast as tortoise.
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]
    
    # To find the entrance to the cycle tortoise begins from start of array while hare begins from intersection point.
    tortoise = arr[0]
    while tortoise != hare:
        # This time both runners move with same speed.
        tortoise = arr[tortoise]
        hare = arr[hare]
        
    # Return the entrance to the cycle, which will be the repeated element.
    return hare