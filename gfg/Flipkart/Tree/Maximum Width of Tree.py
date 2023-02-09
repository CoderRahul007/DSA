# Given a Binary Tree, find the maximum width of it. 
# Maximum width is defined as the maximum number of nodes in any level.
# For example, maximum width of following tree is 4 as there are 4 nodes at 3rd level.

#           1
#        /     \
#      2        3
#    /    \    /    \
#   4    5   6    7
#     \
#       8

# Example 1:

# Input:
#        1
#      /    \
#     2      3
# Output: 2

# Example 2:

# Input:
#         10
#       /     \
#     20      30
#    /    \
#   40    60
# Output: 2
class Solution:
    #Function to get the maximum width of a binary tree.
    def getMaxWidth(self,root):
        q = [root]
        m = 0
        while len(q) > 0:
            M = len(q)
            m = max(M , m)
            for i in range(M):
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return m
# Complexity Analysis:
#  Time Complexity: O(N) where N is the total number of nodes in the tree. In level order traversal, every node of the tree is processed once and hence the complexity due to the level order traversal is O(N) if there are total N nodes in the tree. Therefore, the time complexity is O(N).

# Auxiliary Space: O(w) where w is the maximum width of the tree.
# In level order traversal, a queue is maintained whose maximum size at any moment can go upto the maximum width of the binary tree.         