# Given an array of non-negative integers of size N. Find the maximum possible
#  XOR between two numbers present in the array.

# Example 1:

# Input:
# Arr = {25, 10, 2, 8, 5, 3}
# Output: 28
# Explanation:
# The maximum result is 5 ^ 25 = 28.

# Example 2:

# Input :
# Arr = {1, 2, 3, 4, 5, 6, 7}
# Output : 7
# Explanation :
# The maximum result is 1 ^ 6 = 7.

# As a next step, the interviewer will ask you to optimize the above solution in terms of time
#  and space complexity or may directly ask you to solve it using Tries. In fact, the majority 
# of the interviewers ask this question to check the candidate's thinking ability and to test 
# the knowledge of Tries(See Using Trie in Data Structure). The intuition for this approach is
#  the same as the above one, i.e., we can maximize the 'XOR' value of any two integers by taking 
# their bits at the ith position as 1 and 0 or as 0 and 1,


# The idea is to insert the binary representation of the numbers in the array arr[] into a Trie.
#  Iterate through the binary representation of all the numbers in the trie and if the current 
# bit is 0, then find the path with value 1 and vice-versa. Keep updating the maximum value for each number in the process.
# Algorithm

# Initialize the maximumXOR as 0.
    
# Create a trie data structure to store the binary representation of 32-bit integers of the array.
#  While insertion, if the current bit is 0, then create a node in the left. Else create a node in
#  the right of the current head node.
    
# Linearly traverse the given array, and for each element of the array.Initialize currentXOR as 0.
# Traverse the binary representation of the element stored in trie.

# If the ith bit is 1 and node->left exists then update the value of currentXOR as currentXOR + pow(2, i)
#  and update the node as node->left.
    
# Otherwise, update node = node -> right.If the ith bit is 0 and node->right exists then update the
#  value of currentXOR as currentXOR + pow(2, i) and update the node as node->right. Otherwise, 
# update the node and node->left.
    
# For each array element, update the maximumXOR if the maximumXOR is greater than the currentXOR.
    
# Print the value of the maximumXOR.

# https://takeuforward.org/data-structure/maximum-xor-of-two-numbers-in-an-array/
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.val = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, binary):
        cur = self.root
        for char in binary:
            cur = cur.children[int(char)]

    def search(self, binary) -> int:
        result = 0
        cur = self.root
        for char in binary:
            opposite = 1 - int(char)
            if opposite in cur.children:
                result = (result << 1) | 1
                cur = cur.children[opposite]
            else:
                result = (result << 1)
                cur = cur.children[int(char)]
        return result


def findMaximumXOR( nums):
    trie = Trie()
    result = float('-inf')
    # format binary string in length of  max num
# The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.

# If the value of the len parameter is less than the length of the string, no filling is done.    
    maxLen = len(bin(max(nums))[2:])
    for num in nums:
        key = bin(num)[2:].zfill(maxLen)
        trie.insert(key)
        result = max(result, trie.search(key))
    return result


arr = [14, 70, 53, 33, 49, 91, 36, 80, 92, 51, 66, 70]
print(findMaximumXOR( arr))