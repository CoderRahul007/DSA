# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), 
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:

# Input: n = 2
# Output: false

# https://leetcode.com/problems/happy-number/solution/

# Based on our exploration so far, we'd expect continually following links to end in one of three ways.

# It eventually gets to 11.
# It eventually gets stuck in a cycle.
# It keeps going higher and higher, up towards infinity.
# That 3rd option sounds really annoying to detect and handle.
#  How would we even know that it is going to continue going up,
#  rather than eventually going back down, possibly to 1?
#  Luckily, it turns out we don't need to worry about it.
#   Think carefully about what the largest next number we could get for each number of digits is.

##########################################################################################################
# Using hash Set

def isHappy(self, n: int) -> bool:

    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10) # d => n%10 , n = n//10
            total_sum += digit ** 2
        return total_sum

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1

# TC -> log n
# SC -> Log n
########################################################################################################
# Floyd Warshall

# Approach 2: Floyd's Cycle-Finding Algorithm
# Intuition

# The chain we get by repeatedly calling getNext(n) is an implicit LinkedList. 
# Implicit means we don't have actual LinkedNode's and pointers, but the data does 
# still form a LinkedList structure. The starting number is the head "node" of the list,
#  and all the other numbers in the chain are nodes. The next pointer is obtained with our getNext(n) function above.

def isHappy(self, n: int) -> bool:  
    def get_next(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    slow_runner = n
    fast_runner = get_next(n)
    
    while fast_runner != 1 and slow_runner != fast_runner:
        slow_runner = get_next(slow_runner)
        fast_runner = get_next(get_next(fast_runner))
    return fast_runner == 1

# TC -> log n
# SC -> 1    