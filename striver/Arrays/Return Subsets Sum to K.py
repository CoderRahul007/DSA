# recursive

def findSubsetsThatSumToK(arr, n, k) :
    # Write your code here.
    def helper(i  , k , arr , subs):
        if i == len(arr):
            if k == 0 and len(subs) != 0:
                ans.append(subs[:])
            return 
        subs.append(arr[i])
        helper(i+1 , k - arr[i] , arr , subs)
        subs.pop()
        helper(i+1 , k , arr , subs)
    ans = []            
    helper(0 , k , arr , [])
    return ans
# 2^n *n
# return all the subsets which sums to K            


######################################################################################
#  Iterative + Bitmasking

# The idea is to denote every subset as a binary representation of a positive integer. For example, let the size of a given array is 3 and an integer 5, which has a binary representation ‘101’, here ‘101’ means we take a subset which has elements 1st and 3rd(1 means include the element and 0 means not include the element). LSB of  '101' represents the first element of the array and MSB represents the last element of the array.

# Similarly, '111' means we have taken all the 3 elements in our subset.

 

# So, if we have ‘n’ elements we need to have an integer that has its binary representation ‘n’ bits long, which is (2 ^ n) - 1. So, every integer from 0 to (2 ^ n) - 1 represents a different subset. 

# For checking, if an ith element is present in a subset or not we can say that if the ith bit from LSB is set then the ith element is present in a subset otherwise not.

 

# Here is the algorithm :

#     Declare a 2-d vector 'ans' which stores all possible subsets which sum up to ‘K’.
#     Run a loop from 0 to (2 ^ n) - 1 (say iterator ‘i’)
#         Initialize a variable 'sum'=0, which stores the sum of a particular subset and a vector ‘temp’ to store the subset.
#             Iterate over the elements of the given array (say iterator ‘j’)  and check to see whether an element is present in the current subset or not. If it is present then update sum as sum += num[j], add element in ‘temp’.
#         If ‘sum’ is ‘K’
#             Insert 'temp' in 'ans' vector.
#     Return 'ans'.

# Time Complexity

# O((2^N)* N), where ‘N’ is the size of the array. 
# Each element of the array has 2 choices whether to include in a subset or not. So there is a 2 ^ N number of subsets. And for calculating the sum in a particular subset is O(N).

# Hence, the overall time complexity will be O((2^N) * N).
# Space Complexity

# O( 1 )
'''
    Time Complexity: O((2^N) * N).
    Space Complexity: O( 1 ).

    Where 'N' is the size of the array.
'''

def findSubsetsThatSumToK(arr, n, k):
    # Ans vector contains all the subset which sum upto 'K'.
    ans = [[]]
    
    for i in range(0, 1 << n):
        sum = 0
        vec = []
        for j in range(n):
            # Checking wheather the element is present the subset or not.
            if ((1 << j) & i):
                sum += arr[j]
                vec.append(arr[j])

        # If sum is 'K'.
        if (sum == k):
            ans.append(vec)

    # Return ans.
    return ans