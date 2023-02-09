##################################################################################

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def recurse(l, r):
            # base case, l must always be <= r
            # l == r is the case of a leaf node.
            if l > r: return None
            mid = (l+r)//2
            node = TreeNode(nums[mid])
            node.left = recurse(l, mid-1)
            node.right = recurse(mid+1, r)
            return node
        # both the indices are inclusive,
        # mathematically given by: [0, len(nums)-1]
        return recurse(0, len(nums)-1)

# In this case the time complexity is the same, O(N), but the space complexity is now O(log(N)).
# We just need to consider the maximum height of the stack while recursion. 
# This is log(N) becasue we are dealing with height-balanced BST!



#####################################################################################
def recursive(self, nums):
    def rec(nums, start, end):
        if start <= end:
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = rec(nums, start, mid - 1)
            node.right = rec(nums, mid + 1, end)
            return node
    return rec(nums, 0, len(nums) - 1)

# Time Complexity: O(n log n)
# Space Complexity: O(n)

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/2406277/Python-oror-Easily-Understood-oror-Faster-than-86-oror-Less-than-83-oror-Recursion    