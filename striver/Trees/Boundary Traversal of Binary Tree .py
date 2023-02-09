
# Recursion Based Approach

# The boundary traversal of a binary tree can be broken down into 4 parts. 
# These parts are given in the same order as they are present in the traversal-

# The root node - The root node will always be our first node in the whole boundary traversal.
    
# The left boundary - The left most nodes of the left subtree are also included in the boundary traversal,
#  so we will process them next except for the leaf node as it will be processed in our next part.
#  We can use recursion for this and traverse for only left child until a leaf node is encountered. 
#  If the left child is not present we recurse for the right child.
    
# The leaf Nodes - The leaf nodes of the binary tree will be processed next.
#  We can use a simple inorder traversal for that. Inorder traversal will make sure 
#  that we process leaf nodes from left to right.
    
# The right boundary - The right most nodes of the right subtree will be processed 
# at last in reverse order except for the leaf node as it is already processed in the 
# previous part. For this, we can use recursion in a postorder manner and traverse for 
# the right child only until we encounter a leaf node. If the right child is not present 
# we will recurse for the left child. The postorder recursion will make sure that we traverse
#  the right boundary in reverse order.

# Time Complexity

# O(N), where ‘N’ is the total number of nodes in the binary tree.

 

# Since we are traversing for left and right boundaries in a binary tree, 
# and this will take at the most linear time. Also, traversing for leaf nodes can also be performed 
# in linear time. Hence, the overall time complexity is O(N).

# Space Complexity

# O(N), where ‘N’ is the total number of nodes in the binary tree.

# The recursion stack can grow at maximum the height of the binary tree. 
# In the worst-case scenario, the height of a binary tree can be up to N (Skewed Trees).
#  Hence the overall space complexity will be O(N).


'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the number of nodes in the Binary Tree.
'''

from queue import Queue

# Binary tree node class for reference.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def leftBoundary(root, ans):
    if(root == None or (root.left == None and root.right == None)):
        return

    ans.append(root.data)

    if(root.left != None):
        leftBoundary(root.left, ans)
    else:
        leftBoundary(root.right, ans)


def rightBoundary(root, ans):
    if(root == None or (root.left == None and root.right == None)):
        return

    if(root.right != None):
        rightBoundary(root.right, ans)
    else:
        rightBoundary(root.left, ans)

    ans.append(root.data)


def leafNodes(root, ans):
    if(root == None):
        return

    if(root.left == None and root.right == None):
        ans.append(root.data)
        return

    leafNodes(root.left, ans)
    leafNodes(root.right, ans)

# Functions to traverse on each part.
def traverseBoundary(root):
    ans = []

    if(root == None):
        return ans

    ans.append(root.data)

    # Traverse left boundary.
    leftBoundary(root.left, ans)

    # Traverse for leaf nodes.
    leafNodes(root.left, ans)
    leafNodes(root.right, ans)

    # Traverse right boundary.
    rightBoundary(root.right, ans)

    return ans