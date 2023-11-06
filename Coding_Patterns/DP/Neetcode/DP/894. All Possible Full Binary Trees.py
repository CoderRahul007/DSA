# # Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

# # Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

# # A full binary tree is a binary tree where each node has exactly 0 or 2 children.

# Input: n = 7
# Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# Example 2:

# Input: n = 3
# Output: [[0,0,0]]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = { 0 : [] , 1 : [TreeNode()]}
        
        def backtrack(n):
            if n in dp:
                return dp[n]
            
            res  = []
            for left in range(n):
                right = n - left - 1
                leftSubTree , rightSubTree = backtrack(left) , backtrack(right)
            
                for t1 in leftSubTree:
                    for t2 in rightSubTree:
                        res.append(TreeNode(0 , t1 ,t2))
                        
            dp[n] = res
            return dp[n]
        
        return backtrack(n)


# O( 2** n)        