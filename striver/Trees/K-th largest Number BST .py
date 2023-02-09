############################################################################
class Solution:
    def KthLargestNumber(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        ans = float('inf')
        def inorderTraversal(node):
            nonlocal count, ans
            if node:
                inorderTraversal(node.right)                
                count -= 1
                if count == 0:
                    ans = node.val
                
                inorderTraversal(node.left)
                
        inorderTraversal(root)
        return ans
################################################################################
'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    where N is the total number of nodes of the BST.
'''

def inorder(root, inTraversal):
    if root == None:
        return

    # Recurse over left subtree.
    inorder(root.left, inTraversal)

    inTraversal.append(root.data)

    # Recurse over right subtree.
    inorder(root.right, inTraversal)


def KthLargestNumber(root, k):
    inTraversal = []

    inorder(root, inTraversal)

    n = len(inTraversal)

    if k > n:
        return -1
    
    return inTraversal[n - k]

##################################################################################

# Reverse Inorder Traversal

'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    where N is the total number of nodes of the BST.
'''

def revInorder(root, visCount, k):
    if root == None:
        return -1
    
    # Recurse over right subtree.
    right = revInorder(root.right, visCount, k)

    if right != -1:
        return right
    
    visCount[0] += 1

    if visCount[0] == k:
        return root.data

    # Recurse over left subtree.
    left = revInorder(root.left, visCount, k)

    return left


def KthLargestNumber(root, k):

    # Passing by reference.
    visCount = [0]

    return revInorder(root, visCount, k)  