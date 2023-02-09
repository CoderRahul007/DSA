# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree
# rooted with that node. If such a node does not exist, return null.

# Example 1:

# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# Example 2:


# Input: root = [4,2,7,1,3], val = 5
# Output: []

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val == val:
            return root
        else:
            return  self.searchBST(root.left , val) if root.val > val else self.searchBST(root.right , val)

###########################################################################################################

# iteration:

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None and root.val != val:
            root = root.left if root.val > val else root.right
        return root