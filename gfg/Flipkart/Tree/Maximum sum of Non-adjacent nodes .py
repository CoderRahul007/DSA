# Given a binary tree with a value associated with each node, 
# we need to choose a subset of these nodes such that sum of 
# chosen nodes is maximum under a constraint that no two chosen
#  node in subset should be directly connected that is, if we have
#  taken a node in our sum then we can’t take its any children or 
# parents in consideration and vice versa.

                                               

# Example 1:

# Input:
#      11
#     /  \
#    1    2
# Output: 11
# Explanation: The maximum sum is sum of
# node 11.

# Example 2:

# Input:
#         1
#       /   \
#      2     3
#     /     /  \
#    4     5    6
# Output: 16
# Explanation: The maximum sum is sum of
# nodes 1 4 5 6 , i.e 16. These nodes are
# non adjacent.

class Solution:
    #Function to return the maximum sum of non-adjacent nodes.
    def getMaxSum(self,root):
        #code here
        def helper(root):
            if not root:
                return [0,0]
            left = helper(root.left)
            right = helper(root.right)
            
            pick = root.data + left[1] + right[1]
            notPick = max(left[0] , left[1]) + max(right[0] , right[1])
            
            return [pick , notPick]
        ans = helper(root)
        return max(ans)
####################################################################################################################
def solve(root, dp):
   if not root:
       return 0
   
   if root in dp:
       return dp[root]
   
   incl = root.data
   if root.left:
       incl +=solve(root.left.left, dp)
       incl +=solve(root.left.right, dp)
   if root.right:
       incl +=solve(root.right.left, dp)
       incl +=solve(root.right.right, dp)
   
   
   excl = solve(root.left, dp) + solve(root.right, dp)
   dp[root] = max(incl, excl)
   return dp[root]
   
class Solution:
   #Function to return the maximum sum of non-adjacent nodes.
   def getMaxSum(self,root):
       ans = solve(root, dict())
       return ans