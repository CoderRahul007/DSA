# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths
# where the sum of the node values in the path equals targetSum. Each path should be returned
#  as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node.
#  A leaf is a node with no children.

# Example 1:

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
# Example 2:


# Input: root = [1,2,3], targetSum = 5
# Output: []
# Example 3:

# Input: root = [1,2], targetSum = 0
# Output: []


######################################################
# O(n) DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # the idea is to use dfs to traverse the tree from all root to leaf paths
    # `path` is used to store the current route
    # `remainingSum` is used to store thre remaining sum that we need with the initial value `targetSum`.
    #  we substract it from the node value when we traverse down the tree
    # if we arrive the leaf and the the remaining sum is eqaul to leaf node value
    # then we can add `path` to ans
    # e.g. path = [5,4,11,2] and remainingSum = targetSum = 22
    # traverse node 5, remainingSum = 22 - 5 = 17
    # traverse node 4, remainingSum = 17 - 4 = 13
    # traverse node 11, remainingSum = 13 - 11 = 2
    # traverse node 2, remainingSum = 2 - 2 = 0
    # remainingSum is 0 which means the sum of current path is eqaul to targetSum
    # so how to find another path?
    # we can backtrack here
    # we can pop back a node and try another
    # e.g. path = [5, 4, 11, 7]
    # pop 7 out = [5, 4, 11]
    # push 2 = [5, 4, 11, 2]
    # ... etc
    def dfs(self, root, path, ans, remainingSum):
        # if it is None, then return
        if not root:
            return
        # add the current node val to path
        path.append(root.val)
        # !node.left && !node.right : check if it is a leaf node
        # remainingSum == node.val: check if the remaining sum - node.val == 0
        # if both condition is true, then we find one of the paths
        if not root.left and not root.right and remainingSum == root.val:
            ans.append(list(path))
        # traverse left sub tree with updated remaining sum
        # we don't need to check if left sub tree is nullptr or not
        # as we handle it in the first line of this function
        self.dfs(root.left, path, ans, remainingSum - root.val)
        # traverse right sub tree with updated remaining sum
        # we don't need to check if right sub tree is nullptr or not
        # as we handle it in the first line of this function
        self.dfs(root.right, path, ans, remainingSum - root.val)
        # backtrack
        path.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        self.dfs(root, [], ans, targetSum)
        return ans

###############################################################################################

# The idea is that you follow standard DFS by adding the children of the current node to the stack.
# While you are pushing the children nodes to the stack, also push a running sum and
# the values of the current path to your stack in a tuple.
# So, the tuple will have a shape like (child_node, running_sum, [path_values]).
# Then, if it's a leaf node, check whether the running_sum equals sum. If so,
# add the path_values to your result.


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result, stack = [], []

        if root:
            # (root, running_sum, path_values)
            stack.append((root, root.val, [root.val]))

        while stack:
            node, running_sum, vals = stack.pop()

            # if it's a leaf node and the running_sum equals sum, append path to results
            if not node.left and not node.right and running_sum == sum:
                result.append(vals)

                # if there's a right node and/or a left node, add their info to the stack
            if node.right:
                stack.append((node.right, running_sum +
                             node.right.val, vals + [node.right.val]))
            if node.left:
                stack.append(
                    (node.left, running_sum+node.left.val, vals + [node.left.val]))

        return result

#################################################################################################

# BFS + queue


def pathSum3(self, root, sum):
    if not root:
        return []
    res = []
    queue = [(root, root.val, [root.val])]
    while queue:
        curr, val, ls = queue.pop(0)
        if not curr.left and not curr.right and val == sum:
            res.append(ls)
        if curr.left:
            queue.append((curr.left, val+curr.left.val, ls+[curr.left.val]))
        if curr.right:
            queue.append((curr.right, val+curr.right.val, ls+[curr.right.val]))
    return res

# DFS + stack I


def pathSum4(self, root, sum):
    if not root:
        return []
    res = []
    stack = [(root, sum-root.val, [root.val])]
    while stack:
        curr, val, ls = stack.pop()
        if not curr.left and not curr.right and val == 0:
            res.append(ls)
        if curr.right:
            stack.append((curr.right, val-curr.right.val, ls+[curr.right.val]))
        if curr.left:
            stack.append((curr.left, val-curr.left.val, ls+[curr.left.val]))
    return res

# DFS + stack II


def pathSum5(self, root, s):
    if not root:
        return []
    res = []
    stack = [(root, [root.val])]
    while stack:
        curr, ls = stack.pop()
        if not curr.left and not curr.right and sum(ls) == s:
            res.append(ls)
        if curr.right:
            stack.append((curr.right, ls+[curr.right.val]))
        if curr.left:
            stack.append((curr.left, ls+[curr.left.val]))
    return res
