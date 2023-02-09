#  Bit-Masking

# Instead of finding two elements having maximum xor, we will focus on finding the
#  two numbers in an array, such that xor of which equals a number ‘P’. In this case, 
# ‘P’ will be the maximum number we want to achieve till i-th bit.


 

# For ‘P’ to be maximum, we need to try to get as many bits as possible to be 
# 1 from left to right, left-most being the biggest bit. Note that the value of left 
# bits is greater than the sum of all the right bits, so we will try to make bits towards
#  the left to be 1 first, then move towards the right.


 

# We will iterate from left to right bits and consider only the bits from left
#  to current bit to find the optimal answer achievable for those bits. We can 
# store only the prefix of that number till that bit by using a bitmask which will 
# store all the bits from left to current bit for that element.

# To find this, we will do bitwise AND of all elements with another number where
#  only those bits are 1, which we need for the prefix and rest to be 0.


 

# We will store all the prefix masks in a set and evaluate if we can make the current bit 1 in the answer.

# We know if,

# a xor b  = c

# Then

# a = c xor b

# So we will set the current bit 1 in a temporary answer, iterate through the set,
#  and check if xor of this and the current element is present in the set. If it is 
# present, we can update the answer to the temporary answer. 

# Algorithm: 

#     Initialise ‘ans’ to 0.
#     Initialise ‘mask’ to 0.
#     Run a loop ‘i’ from 30 to 0
#         Create a set ‘s’ of integers.
#         Make the ith bit 1 in the ‘mask’.
#         Run a loop ‘j’ from ‘0’ to ‘N’ - 1
#             Insert the bitwise and of ‘A[j]’ and ‘mask’ into the set.
#         Initialise ‘tempAns’ to ‘ans’
#         Make the ith bit 1 in the ‘tempAns’.
#         Iterate through the set
#             If xor of ‘tempAns’ and current element is present in the array, update ‘ans’ to ‘tempAns’ and break.

#     Return ‘ans’

# Time Complexity

# O(N * log (M)), where ‘N’ is the size of the array and ‘M’ is the maximum number present in the array.

# Since for each bit, we are iterating through the whole array, the time complexity becomes O(N * log (M)).

# Space Complexity

# O(N), where ‘N’ is the size of the array


'''
    Time Complexity: O(N * log (M))
    Space Complexity: O(N)

    Where ‘N’ is the length of the given array and 'M' the maximum value in the array.
'''

def maximumXor(A):
    
    ans = 0
    n = len(A)
    s = set()
    mask = 0
    
    for i in range (30, -1, -1):
        
        # Setting the ith bit 1 in mask.
        mask = mask | (1 << i)
        
        for j in range (n):
            # Inserting prefix bitmask into the set.
            s.add(A[j] & mask)
            
        tempAns = ans
        
        # Setting the ith bit 1.
        tempAns = tempAns | (1 << i)
        
        for it in s:
            # Checking if 'it' xor 'tempAns' is present in set. 
            if it ^ tempAns in s:
                ans = tempAns
                break
            
        s = set()
        
    return ans

######################################################################################
# Trie

class TrieNode:
    def __init__(self):
        self.children = dict()                        # children nodes
        self.val = 0                                  # end value 

class Trie:
    def __init__(self, n):
        self.root = TrieNode()                        # root node
        self.n = n                                    # max length of all numbers
        
    def add_num(self, num):
        node = self.root 
        for shift in range(self.n, -1, -1):           # only shift self.n bits 
            val = 1 if num & (1 << shift) else 0      # verify bit from left to right 
            if val not in node.children:
                node.children[val] = TrieNode()
            node = node.children[val]
        node.val = num
        
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_len = len(bin(max(nums))) - 2             # get max length of all numbers' binary
        trie = Trie(max_len)
        for num in nums:
            trie.add_num(num)            # build trie
            
        ans = 0
        for num in nums:                              # for each num, find the number which can create max value with num using XOR
            node = trie.root 
            for shift in range(max_len, -1, -1):
                val = 1 if num & (1 << shift) else 0  # verify bit from left to right
                node = node.children[1-val] if 1-val in node.children else node.children[val] # try opposite bit first, otherwise use same bit
            ans = max(ans, num ^ node.val)            # maintain maximum
        return ans

# https://takeuforward.org/data-structure/maximum-xor-of-two-numbers-in-an-array/

# Time Complexity: O(N*32) + O(M*32)

# Reason: For inserting all the elements of arr1 into the trie take O(N*32) [32 Bit] and O(M*32) for finding the maxXOR for every element of arr2.

# Space Complexity: O(N*32)

