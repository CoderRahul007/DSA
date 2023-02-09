# Given a Binary Tree having positive and negative nodes. Find the maximum sum of a level in the given Binary Tree.

# Example 1:

# Input :               
#              4
#           /    \
#          2     -5
#         / \    / \
#       -1   3  -2  6

# Output: 6

# Explanation :
# Sum of all nodes of 0'th level is 4
# Sum of all nodes of 1'th level is -3
# Sum of all nodes of 2'th level is 6
# Hence maximum sum is 6

import sys
class Solution:
    def maxLevelSum(self, root):
        # Code here
        q = [root]
        m = -sys.maxsize
        while q :
            t = len(q)
            
            s = 0
            while t>0:
                
                temp = q.pop(0)
                s+= temp.data
                
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                t-=1
            m = max(m , s)
        return m

def maxLevelSum(self, root):
        # Code here
        ans=-1000000
        queue=[root]
        level=[]
        while queue!=[] and root is not None:
            l=[]
            for node in queue:
                l.append(node.data)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            s1=sum(l)
            ans=max(ans,s1)
            queue=level
            level=[]
        return ans        