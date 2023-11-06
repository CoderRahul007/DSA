# You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

# Return true if you can make this square and false otherwise.

 

# Example 1:


# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
# Example 2:

# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the matchsticks.

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        k = 4
        if sum(matchsticks) % k :
            return False
        matchsticks.sort(reverse = True)
        used = [False for i in range(len(matchsticks))]

        target = sum(matchsticks) // k

        def backtrack(i , k , subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0 , k - 1 , 0)
            
            for j in range(i , len(matchsticks)):
                
                if j > 0 and not used[j - 1] and matchsticks[j] == matchsticks[j - 1]:
                    continue
                if used[j] or subsetSum + matchsticks[j] > target:
                    continue
                used[j] = True
                if backtrack(j + 1 , k, subsetSum + matchsticks[j]):
                    return True
                used[j] = False
            return False
        return backtrack(0 , k , 0)