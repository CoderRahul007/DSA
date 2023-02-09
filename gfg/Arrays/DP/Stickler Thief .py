# Stickler the thief wants to loot money from a society having n houses in a single line.
#  He is a weird person and follows a certain rule when looting the houses.
#  According to the rule, he will never loot two consecutive houses.
#  At the same time, he wants to maximize the amount he loots. The thief knows which
#  house has what amount of money but is unable to come up with an optimal looting strategy.
#  He asks for your help to find the maximum money he can get if he strictly follows the rule. 
# Each house has a[i]amount of money present in it.

# Example 1:

# Input:
# n = 6
# a[] = {5,5,10,100,10,5}
# Output: 110
# Explanation: 5+100+5=110

# Example 2:

# Input:
# n = 3
# a[] = {1,2,3}
# Output: 4
# Explanation: 1+3=4


class Solution:  
    def FindMaxSum(self,a, n):
        dp = [-1 for _ in range(n+1)]
    
        def solve(arr, n):
            if n < 0:
                return 0
            if dp[n] != -1:
                return dp[n]
            
            # if current element is pick then previous cannot be picked                            
            pick  = arr[n] + solve(arr, n-2)

            # if current element is not picked then previous element is picked
            notPick  = solve(arr, n-1)

            dp[n] = max(pick , notPick )
            
            return dp[n]

        return solve(a, n-1)

    def anotherOne(self , a, n):
        if n == 0:
            return 0
 
        value1 = a[0]
        if n == 1:
            return a[0]

        value2 = max(a[0], a[1])
        if n == 2:
            return max(a[0], a[1])
    
        # contains maximum stolen value at the end
        max_val = None
    
        # Fill remaining positions
        for i in range(2, n):
            max_val = max(a[i] + value1 , value2)
            value1 = value2
            value2 = max_val
    
        return max_val

# Algorithm: 
 

# Create an extra space dp, DP array to store the sub-problems.
# Tackle some basic cases, if the length of the array is 0, print 0, if the length of the array is 1, 
# print the first element, if the length of the array is 2, print maximum of two elements.
# Update dp[0] as array[0] and dp[1] as maximum of array[0] and array[1]
# Traverse the array from the second element (2nd index) to the end of array.
# For every index, update dp[i] as maximum of dp[i-2] + array[i] and dp[i-1], 
# this step defines the two cases, if an element is selected then the previous element cannot be selected 
# and if an element is not selected then the previous element can be selected.
# Print the value dp[n-1]        
      