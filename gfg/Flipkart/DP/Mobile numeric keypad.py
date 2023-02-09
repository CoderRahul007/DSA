# Given the mobile numeric keypad. You can only press buttons that are up, 
# left, right, or down to the current button. You are not allowed to press 
# bottom row corner buttons (i.e. * and # ). Given a number N, the task is
#  to find out the number of possible numbers of the given length.

# Example 1:

# Input: 1
# Output: 10
# Explanation: Number of possible numbers 
# would be 10 (0, 1, 2, 3, …., 9)  

# Example 2:

# Input: N = 2
# Output: 36
# Explanation: Possible numbers: 00, 08, 11,
# 12, 14, 22, 21, 23, 25 and so on.
# If we start with 0, valid numbers 
# will be 00, 08 (count: 2)
# If we start with 1, valid numbers 
# will be 11, 12, 14 (count: 3)
# If we start with 2, valid numbers 
# will be 22, 21, 23,25 (count: 4)
# If we start with 3, valid numbers 
# will be 33, 32, 36 (count: 3)
# If we start with 4, valid numbers 
# will be 44,41,45,47 (count: 4)
# If we start with 5, valid numbers 
# will be 55,54,52,56,58 (count: 5) 
# and so on..


# Your Task:  
# You don't need to read input or print anything. Complete the function getCount() which takes N as input parameter and returns the integer value

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N)

# https://www.youtube.com/watch?v=IN3uTs8afz4

class Solution:
	def getCount(self, n):
		# code here
            dic = {1:(1,2,4),
            2:(1,3,2,5),
            3:(3,6,2),
            4:(1,5,4,7),
            5:(5,4,2,8,6),
            6:(6,5,3,9),
            7:(7,4,8),
            8:(5,7,9,0,8),
            9:(6,8,9),
            0:(8,0)}
            
            dp = [[0 for i in range(10)] for j in range(n+1)]   # row is how many times key is pressed
            for i in range(10):
                dp[1][i] = 1
    
            for i in range(2,n+1):
                for j in range(10):
                    for ele in dic[j]:
                        dp[i][j] += dp[i-1][ele]            
            s = sum(dp[n])
            return s