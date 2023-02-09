# https://www.codingninjas.com/codestudio/problems/diameter-of-the-binary-tree_920552?topList=striver-sde-sheet-problems&leftPanelTab=0

# Optimized Approach

# The basic idea of this approach is to calculate the height of the subtree in the same 
# recursion instead of calling getHeight() for it.

# Let us define a recursive function getDiamter(TreeNode<int> *root, int& height) which returns 
# the diameter of the given subtree rooted at the “root” node. And, a variable “height” is passed by 
# reference, which denotes the height of that subtree. 

# Algorithm

#     If the root node is NULL, assign “height” = 0 and return 0 because the height and diameter
#      of an empty tree will be 0.
#     Initialize two variables, “leftHeight” and “rightHeight” to 0, which denotes the height 
#     of the left subtree and right subtree, respectively.
#     Recur for the left subtree and store the diameter of the left subtree in a variable i.e. 
#     leftDiameter = getDiameter(root->left, leftHeight)
#     Similarly, recur for the right subtree and store the diameter of the right subtree in a
#      variable i.e. rightDiamater = getDiamter(root->right, rightHeight)
#     Update the height of the tree i.e. height = max(leftHeight, rightHeight) + 1
#     The diameter of the given tree will be the maximum of the following terms:
#         “leftDiameter”
#         “rightDiameter”
#         “leftHeight” + “rightHeight”
#     Return the maximum of above terms i.e. max(leftDiameter, rightDiameter, leftHeight + rightHeight).

# Time Complexity

# O(N), Where ‘N’ is the number of nodes in the given binary tree.


# Since we are traversing all the tree nodes, which takes O(N) time, the overall time complexity will be O(N).
# Space Complexity

# O(N), Where ‘N’ is the number of nodes in the given binary tree.

 

# Since we are doing a recursive tree traversal and in the worst case (Skewed Trees), 
# all nodes of the given tree can be stored in the call stack. So the overall space complexity will be O(N).


"""
    Time Complexity : O(N)
    Space Complexity : O(N)
	
    Where 'N' is the number of nodes in the given binary tree.
"""

def getDiameter(root, height):

    if (root == None):
    
        # Height and diameter of an empty tree will be 0.
        height[0] = 0
        return 0
    

    # To store the height of left and right subtrees.
    leftHeight = [0]
    rightHeight = [0]

    # Recur for left subtree and get the height as well as diameter.
    leftDiameter = getDiameter(root.left, leftHeight)

    # Recur for right subtree and get the height as well as diameter.
    rightDiameter = getDiameter(root.right, rightHeight)

    # Update the height of the given binary tree.
    height[0] = max(leftHeight[0], rightHeight[0]) + 1

    # Diameter of given binary tree.
    diameter = max(leftDiameter, rightDiameter, leftHeight[0] + rightHeight[0])

    return diameter


def diameterOfBinaryTree(root):

    # Initialize a variable to store the height of the of binary tree.
    height = [0]

    # Recursive function to find diameter.
    return getDiameter(root, height)

