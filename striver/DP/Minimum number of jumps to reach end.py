# Given an array of integers where each element represents the max number of steps that can be made forward from that element. Write a function to return the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then we cannot move through that element. If we can’t reach the end, return -1.

# Examples:

# Input:  arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
# Output: 3 (1-> 3 -> 8 -> 9)

# Explanation: Jump from 1st element to
# 2nd element as there is only 1 step,
# now there are three options 5, 8 or 9.
# If 8 or 9 is chosen then the end node 9
# can be reached. So 3 jumps are made.
# Input  :  arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
# Output : 10

# Explanation: In every step a jump is
# needed so the count of jumps is 10.
# In this post, its O(n) solution will be discussed.

# python program to count Minimum number
# of jumps to reach end

# Returns minimum number of jumps to reach arr[n-1] from arr[0]

# https://www.geeksforgeeks.org/minimum-number-jumps-reach-endset-2on-solution/

# https://www.youtube.com/watch?v=CqgK_qi4SKQ&t=453s
def minJumps(arr, n):

    # The number of jumps needed to reach the starting index is 0
    if (n <= 1):
        return 0

    # Return -1 if not possible to jump
    if (arr[0] == 0):
        return -1

    # initialization
    # stores all time the maximal reachable index in the array
    maxReach = arr[0]
    # stores the amount of steps we can still take
    step = arr[0]
    # stores the amount of jumps necessary to reach that maximal reachable position
    jump = 1

    # Start traversing array

    for i in range(1, n):
        # Check if we have reached the end of the array
        if (i == n-1):
            return jump

        # updating maxReach
        maxReach = max(maxReach, i + arr[i])

        # we use a step to get to the current index
        step -= 1

        # If no further steps left
        if (step == 0):
            # we must have used a jump
            jump += 1

        # Check if the current index / position or lesser index
        # is the maximum reach point from the previous indexes
        if(i >= maxReach):
            return -1

        # re-initialize the steps to the amount
        # of steps to reach maxReach from position i.
        step = maxReach - i
    return -1


# Driver program to test above function
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
size = len(arr)

# Calling the minJumps function
print("Minimum number of jumps to reach end is % d " % minJumps(arr, size))

# This code is contributed by Aditi Sharma
