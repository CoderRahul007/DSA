# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
#  in the sequence has an edge connecting them. A node can only appear in the sequence 
#  at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Example 1:


# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# Example 2:


# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.


# There could be four possibilities.

# 1. The path starts at the root and goes down through the root's left child.
#  We don't know how long the path is, but it could extend to the bottom of the left subtree.

# 2. The path starts at the root and goes down through the root's right child. 
#  Very similar to the previous case, but the direction is toward the right.

# 3. The path involves both the left and the right child.

# 4. The path doesn't involve any child. The root itself is the only element of the path with maximum sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        max_path = -float('inf')

        # post order traversal of subtree rooted at `node`
        def gain_from_subtree(node) -> int:
            nonlocal max_path

            if not node:
                return 0

            # add the gain from the left subtree. Note that if the
            # gain is negative, we can ignore it, or count it as 0.
            # This is the reason we use `max` here.
            gain_from_left = max(gain_from_subtree(node.left), 0)

            # add the gain / path sum from right subtree. 0 if negative
            gain_from_right = max(gain_from_subtree(node.right), 0)

            # if left or right gain are negative, they are counted
            # as 0, so this statement takes care of all four scenarios
            left_right_node = gain_from_left + gain_from_right + node.val

            max_path = max(max_path, left_right_node )

            # return the max sum for a path starting at the root of subtree
            return node.val + max( gain_from_left , gain_from_right)
              

        gain_from_subtree(root)

        return max_path

# Let n be the number of nodes in the tree.

# Time complexity: O(n)

# Each node in the tree is visited only once. During a visit,
#  we perform constant time operations, including two recursive calls
#   and calculating the max path sum for the current node. So the time complexity is O(n).

# Space complexity: O(n)

# We don't use any auxiliary data structure, but the recursive call stack can
#  go as deep as the tree's height. In the worst case, the tree is a linked list,
#   so the height is n. Therefore, the space complexity is O(n).