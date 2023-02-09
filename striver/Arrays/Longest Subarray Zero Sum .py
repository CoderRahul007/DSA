
'''
    Time Complexity: O(N^2)
    Space Complexity: O(1)

    Where 'N' denotes the number of elements of the array
'''


def LongestSubsetWithZeroSum(arr):

    # Initialize result
    maxLen = 0
    n = len(arr)

    # Pick a starting point
    for i in range(n):

        # Initialize currSum for every starting point
        currSum = 0

        # Try all subarrays starting with 'i'
        for j in range(i, n):
            currSum += arr[j]

            # If currSum becomes 0,then update maxLen if required

            if currSum == 0:
                maxLen = max(maxLen, j - i + 1)

    
    return maxLen

##########################################################################################
#  Hash Map

#   We can maintain a prefix sum for each index. We can check if standing at a particular index
#    sum is zero. If it is zero, then we store the index value as the length of the sub-array.
#     Then we hold the sum values in a hash map. If the present sum is previously present in the
#      hash map, then it means starting from the previous index till the current index, we get 
#      another sub-array whose sum is zero. If the length of this sub-array is greater than the
#       previously stored length, then we modify our answer with this value. 


# The steps are as follows:

# We initialize ‘maxLen’  to store the length of the maximum subset whose sum is zero, ‘sum’ to store 
# the present sum, and hashmap ‘presum’ to keep the previous sums.
# We will iterate over all the elements of the array, i.e., i = 0 to i = N - 1:
#     We will store the sum of the elements till index i in ‘sum’.
#     If ‘sum’ is zero, then we will store i + 1 in maxLen.
#     If arr[i] is zero and maxLen is zero, then we will store 1 in maxLen.
#     If ‘sum’ is not present in presum, we will store the maximum of ‘maxLen’ and i - presum[sum] in ‘maxLen’.
#     We will store i in presum[sum].
# We will return ‘maxLen’ as the final answer.

# Time Complexity

# O(N), where N is the number of elements of the array.

 

# As we check for all values from1 to ‘N’, there are at most ‘N’ iterations. Hence, the overall complexity is O(N).
# Space Complexity

# O(N), where N is the number of elements of the array.

 
from collections import OrderedDict

def LongestSubsetWithZeroSum(arr):

    # Map to store the previous sums
    presum = OrderedDict()

    sum = 0  # Initialize the sum of elements
    maxLen = 0  # Initialize result
    n = len(arr)

    # Traverse through the given array
    for i in range(n):
        # Add current element to sum
        sum += arr[i]

        if (arr[i] == 0 and maxLen == 0):
            maxLen = 1
        if sum == 0:
            maxLen = i + 1

        # Look for this sum in Hash table
        if (sum in presum):
            # If this sum is seen before, then update maxLen
            maxLen = max(maxLen, i - presum.get(sum))

        else:
            # Else insert this sum with index in hash table
            presum[sum] = i

    return maxLen


# We are using extra space to store prefix sum and using a hash map. Hence, the overall complexity is O(N).

def LongestSubsetWithZeroSum(arr):


    # Write your Code here.
    # Return an integer denoting the answer.
    n = len(arr)
    d = {}
    s = 0
    Len = 0
    k = 0 # target sum
    
    for i in range(n):
        s += arr[i]
        if s == k:
            Len = i+1 # if k is found at i 0 then Len will be 1
        elif s-k in d: # if its differnce if found in d map then means we can create k by previous value also
            Len = max(Len , i-d[s-k])
        if s not in d:
            d[s] = i
    return Len

#  Hash Map

#   We can maintain a prefix sum for each index. We can check if standing at a particular index sum is zero.
#  If it is zero, then we store the index value as the length of the sub-array. Then we hold the sum values 
# in a hash map. If the present sum is previously present in the hash map, then it means starting from the 
# previous index till the current index, we get another sub-array whose sum is zero. If the length of this 
# sub-array is greater than the previously stored length, then we modify our answer with this value. 


#  The steps are as follows:

#     We initialize ‘maxLen’  to store the length of the maximum subset whose sum is zero, ‘sum’ to store 
#     the present sum, and hashmap ‘presum’ to keep the previous sums.
#     We will iterate over all the elements of the array, i.e., i = 0 to i = N - 1:
#         We will store the sum of the elements till index i in ‘sum’.
#         If ‘sum’ is zero, then we will store i + 1 in maxLen.
#         If arr[i] is zero and maxLen is zero, then we will store 1 in maxLen.
#         If ‘sum’ is not present in presum, we will store the maximum of ‘maxLen’ and i - presum[sum] in ‘maxLen’.
#         We will store i in presum[sum].
#     We will return ‘maxLen’ as the final answer