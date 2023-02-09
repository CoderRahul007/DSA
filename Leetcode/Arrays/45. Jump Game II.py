# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i.
#  In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated 
# such that you can reach nums[n - 1].

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step 
# from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2


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

# https://leetcode.com/problems/jump-game-ii/solutions/1192401/easy-solutions-w-explanation-optimizations-from-brute-force-to-dp-to-greedy-bfs/

# https://www.youtube.com/watch?v=CqgK_qi4SKQ&t=453s

##################################################################################################################

# Minimum number of jumps to reach the end using Recursion: 

#     Start from the first element and recursively call for all the elements reachable from the first element.
#      The minimum number of jumps to reach end from first can be calculated using the minimum value from 
#      the recursive calls. 

#     minJumps(start, end) = Min ( minJumps(k, end) ) for all k reachable from start.

# Follow the steps mentioned below to implement the idea:

#     Create a recursive function.
#     In each recursive call get all the reachable nodes from that index.
#         For each of the index call the recursive function.
#         Find the minimum number of jumps to reach the end from current index.
#     Return the minimum number of jumps from the recursive call.

# Below is the Implementation of the above approach:

# Python3 program to find Minimum
# number of jumps to reach end
 
# Returns minimum number of jumps
# to reach arr[h] from arr[l]
 
 
def minJumps(arr, l, h):
 
    # Base case: when source and
    # destination are same
    if (h == l):
        return 0
 
    # when nothing is reachable
    # from the given source
    if (arr[l] == 0):
        return float('inf')
 
    # Traverse through all the points
    # reachable from arr[l]. Recursively
    # get the minimum number of jumps
    # needed to reach arr[h] from
    # these reachable points.
    min = float('inf')
    for i in range(l + 1, h + 1):
        if (i < l + arr[l] + 1):
            jumps = minJumps(arr, i, h)
            if (jumps != float('inf') and
                    jumps + 1 < min):
                min = jumps + 1
 
    return min
 
 
# Driver program to test above function
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)
print('Minimum number of jumps to reach',
      'end is', minJumps(arr, 0, n-1))
 

# Output

# Minimum number of jumps to reach the end is 3

# Time complexity: O(nN^n). 

#     There are maximum n possible ways to move from an element. 
#     So the maximum number of steps can be nn, Thus O(nn)

# Auxiliary Space: O(n). For recursion call stack. 

#####################################################################################################
# Minimum number of jumps to reach end using Dynamic Programming from left to right:

#     It can be observed that there will be overlapping subproblems. 

#     For example in array, arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9} minJumps(3, 9) will be called 
# two times as arr[3] is reachable from arr[1] and arr[2]. So this problem has both properties
#  (optimal substructure and overlapping subproblems) of Dynamic Programming

# Follow the below steps to implement the idea:

#     Create jumps[] array from left to right such that jumps[i] indicate the minimum number of
#      jumps needed to reach arr[i] from arr[0].
#     To fill the jumps array run a nested loop inner loop counter is j and the outer loop count is i.
#         Outer loop from 1 to n-1 and inner loop from 0 to i.
#         If i is less than j + arr[j] then set jumps[i] to minimum of jumps[i] and jumps[j] + 1.
#          initially set jump[i] to INT MAX
#     Return jumps[n-1].

# Below is the implementation of the above approach:

# Python3 program to find Minimum
# number of jumps to reach end
 
# Returns minimum number of jumps
# to reach arr[n-1] from arr[0]
 
 
def minJumps(arr, n):
    jumps = [0 for i in range(n)]
 
    if (n == 0) or (arr[0] == 0):
        return float('inf')
 
    jumps[0] = 0
 
    # Find the minimum number of
    # jumps to reach arr[i] from
    # arr[0] and assign this
    # value to jumps[i]
    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            if (i <= j + arr[j]) and (jumps[j] != float('inf')):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n-1]
 
 
# Driver Program to test above function
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
size = len(arr)
print('Minimum number of jumps to reach',
      'end is', minJumps(arr, size))
 
# Output

# Minimum number of jumps to reach end is 3

# Thanks to paras for suggesting this method. 

# Time Complexity: O(n2) 
# Auxiliary Space: O(n), since n extra space has been taken.



###########################################################################################################
def jump (nums):
    n = len(nums)
    i = 0
    maxReachable = 0
    lastJumpedPos = 0
    jumps = 0
    while lastJumpedPos < n-1 : # loop till last jump hasn't taken us till the end
        maxReachable = max(maxReachable, i + nums[i]) # furthest index reachable on the next level from current level
        if i == lastJumpedPos: # current level has been iterated & maxReachable position on next level has been finalised
            lastJumpedPos = maxReachable # so just move to that maxReachable position
            jumps += 1 #and increment the level
            # jumps only gets updated after we iterate all possible jumps from previous level
            # This ensures jumps will only store minimum jump required to reach lastJumpedPos
        i += 1
    return jumps

####################################################################################################################
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
            step = maxReach - i
        # Check if the current index / position or lesser index
        # is the maximum reach point from the previous indexes
        if(i >= maxReach):
            return -1

        # re-initialize the steps to the amount
        # of steps to reach maxReach from position i.
        
    return -1