# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined 
# between two nodes p and q as the lowest node in T that has both p and q as descendants 
# (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself 
# according to the LCA definition.
# Example 3:

# Input: root = [1,2], p = 1, q = 2
# Output: 1

#########################################################################3
 
 
# https://www.youtube.com/watch?time_continue=592&v=13m9ZCB8gjw&feature=emb_title

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', n1: 'TreeNode', n2: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root == n1 or root == n2:
            return root
        left = self.lowestCommonAncestor(root.left , n1 , n2)
        right = self.lowestCommonAncestor(root.right , n1 , n2)

        if left and right: # if none of left and right are None then i am getting the n1 and n2 in my left and right so the anser is root
            return root
        if not left and not right:
            return None
        return left if left else right

##############################################
# Iterative

class Solution:

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q


# Complexity Analysis

# Time Complexity : O(N), where NNN is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree.

# Space Complexity : O(N). In the worst case space utilized by the stack, the parent pointer dictionary and the ancestor set, would be O(N) each, since the height of a skewed binary tree could be NNN.