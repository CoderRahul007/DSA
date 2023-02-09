# https://leetcode.com/problems/validate-binary-search-tree/solutions/32112/learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-java-solution/

# https://leetcode.com/problems/validate-binary-search-tree/solutions/786520/general-tree-traversal-problems-interview-prep/?orderBy=most_votes&languageTags=python
#################################################
# Recursive
def isValidBST(self, root):
    low = float("-inf")
    high = float("inf")
    return self.helper(root, low, high )
    
def helper(self, root, low, high):
    if not root:
        return True
    if not root.left and not root.right:
        return low < root.val < high
    return low < root.val < high and self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high)

##################################################
# Inorder Traversal

def InorderTraversal(self, root):
        pre, stack = None, []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return True
            node = stack.pop()
            if pre and pre.val >= node.val:
                return False
            pre = node
            root = node.right    