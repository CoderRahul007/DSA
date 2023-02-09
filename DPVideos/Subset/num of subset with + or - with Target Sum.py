# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-'
#  before each integer in nums and then concatenate all the integers.

#     For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and
# concatenate them to build the expression "+2-1".

# Return the number of different expressions that you can build, which evaluates to target.


# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3


# Assume all -ve values in one subset and other +ve in other subset
# S2 - S1 = target sum
# s2- s1 = diff
# Sum - s1 - s1 = diff
# sum - 2* s1 = diff
# (sum - diff)/ 2 = s1


def TargetSum(arr , n , sum) :
    dp = [[-1 for i in range(sum+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1, sum+1):
        dp[0][i] = 0
    for i in range(1, n+1):
        for j in range(1 , sum+1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else :
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
    return dp[n][sum]


arr = [1,1,1,1,1]
target = 3
sum = (sum(arr) - target) //2
n = len(arr)
print(TargetSum(arr , n , sum))

