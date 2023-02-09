#############################################
# Recursion
'''
    Time Complexity:  O(2^N )
    Space Complexity:O(N)

    Where 'N' is the size of the array.
'''
# Sum of all subsets in increasing order
from typing import List

def subset(i: int, sum: int, num: List[int], ans: List[int]) -> None:

    # Completely traverse the whole array, insert the "sum" in the "ans" vector.
    if i == len(num):
        ans.append(sum)
        return

    # Insert the element in the sum.
    subset(i + 1, sum + num[i], num, ans)

    # Don't take the element in the sum.
    subset(i + 1, sum, num, ans)


def subsetSum(num: List[int]) -> List[int]:

    # Ans vector contains all the subset sums.
    ans = []

    subset(0, 0, num, ans)
    
    # Sort the vector and finally return it.
    ans.sort()
    return ans
########################################################################################
# Iterative + Bitmasking

# The idea is to denote every subset as a binary representation of a positive integer. 
# For example, let the size of a given array is 3 and an integer 5, which has a binary 
# representation “101”, here “101” means we take a subset which has elements 1st and 
# 3rd(1 means include the element and 0 means not include the element). LSB of  “101” represents 
# the first element of the array and MSB represents the last element of the array.

# Similarly, “111” means we have taken all the 3 elements in our subset.
 
# So, if we have ‘n’ elements we need to have an integer that has its binary representation ‘n’ bits long,
#  which is (2^n)-1. So, every integer from 0 to (2^n)-1 represents a different subset. 
 
# For checking, if an ith element is present in a subset or not we can say that if the ith bit from LSB 
# is set then the ith element is present in a subset otherwise not.

# Here is the algorithm :

#     Declare an integer ‘n’ and initialize it with the size of the given array.
#     Declare an vector “ans” which stores all possible subset sums.
#     Run a loop from 0 to (2^n)-1 (say iterator ‘i’)
#         Initialize a variable “sum”=0, which stores the sum of a particular subset.
#             Iterate over the elements of the given array (say iterator ‘j’)  and check to see whether 
#             an element is present in the current subset or not. If it is present then update sum as sum+= num[j]
#         Insert “sum” in “ans” vector.
#     Sort the “ans” vector.
#     Return “ans”.

# Time Complexity

# O( (2^N)* N ), where ‘N’ is the size of the array.

 

# Each element of the array has 2 choices whether to include in a subset or not. So there is a 
# 2^N number of subsets. And for calculating the sum of a particular subset is O(N).

# Hence, the overall time complexity will be O( (2^N)* N ).
# Space Complexity

# O( 1 )

 

# No extra space is used.

'''
    Time Complexity:  O((2^N) * N)
    Space Complexity:O(1)

    Where 'N' is the size of the array.
'''

from typing import List

def subsetSum(num: List[int]) -> List[int]:

    n = len(num)
    
    # Ans vector contains all the subset sums.
    ans = []

    for i in range(2 ** n):
    
        sum = 0
        for j in range(n):
        
            # Checking wheather the element is present the subset or not.
            if (2 **  j) & i:
                sum += num[j]
    
        ans.append(sum)
    
    # Sort the vector and finally return it.
    ans.sort()
    return ans

