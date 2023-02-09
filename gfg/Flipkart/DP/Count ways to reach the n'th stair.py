# There are n stairs, a person standing at the bottom wants to reach the top. 
# The person can climb either 1 stair or 2 stairs at a time.
#  Count the number of ways, the person can reach the top (order does matter).

# Example 1:

# Input:
# n = 4
# Output: 5
# Explanation:
# You can reach 4th stair in 5 ways. 
# Way 1: Climb 2 stairs at a time. 
# Way 2: Climb 1 stair at a time.
# Way 3: Climb 2 stairs, then 1 stair
# and then 1 stair.
# Way 4: Climb 1 stair, then 2 stairs
# then 1 stair.
# Way 5: Climb 1 stair, then 1 stair and
# then 2 stairs.

# Example 2:

# Input:
# n = 10
# Output: 89 
# Explanation: 
# There are 89 ways to reach the 10th stair.

# Method 1: The first method uses the technique of recursion to solve this problem.
# Approach: We can easily find the recursive nature in the above problem. 
# The person can reach nth stair from either (n-1)th stair or from (n-2)th stair. 
# Hence, for each stair n, we try to find out the number of ways
#  to reach n-1th stair and n-2th stair and add them to give the answer 
# for the nth stair. Therefore the expression for such an approach comes out to be : 

# ways(n) = ways(n-1) + ways(n-2)

# The above expression is actually the expression for Fibonacci numbers, 
# but there is one thing to notice, the value of ways(n) is equal to fibonacci(n+1). 

# ways(1) = fib(2) = 1
# ways(2) = fib(3) = 2
# ways(3) = fib(4) = 3

def fib(n):
	if n <= 1:
		return n
	return fib(n-1) + fib(n-2)

# Returns no. of ways to
# reach sth stair
def countWays(s):
	return fib(s+1)
############################################################################
# Memoization
class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        def fib(n)->int:
            if n <=2:
                return n
            if n not in mem:
                mem[n] = fib(n-1)+fib(n-2)
            return mem[n]
        return fib(n)    

##############################################################
# Iterative
    def countWays(self , n):       
        if n <= 3:
            return n
        a = 1
        b = 2 
        s = 0
        for i in range(3 , n + 1):
            s = (a+b)  % 1000000007
            a = b % 1000000007
            b = s
        return s