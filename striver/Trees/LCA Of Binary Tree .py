'''
    Time Complexity : O(N)
    Space Complexity : O(N)

    Where 'N' is the number of nodes in the given binary tree.\
'''


def getPath(root, path, x):
    # Base Case
    if root == None:
        return False
    path.append(root.data)

    # Check if we reached to the destination node i.e. 'X'
    if (root.data == x):
        return True

    # Recur to find 'X' in the left and the right subtree.
    if getPath(root.left, path, x) or getPath(root.right, path, x):
        return True

    # Remove the root node because 'X' doesn't exists in the subtree rooted at "root".
    path.pop()

    return False


def lowestCommonAncestor(root, x, y):
    # To store the path from the root node to 'X' and 'Y'
    pathToX, pathToY = [], []
    # Get the path from the root node to node 'X'
    getPath(root, pathToX, x)
    # Get the path from the root node to node 'Y'
    getPath(root, pathToY, y)

    # Iterate while elements in the lists are equal.
    for index in range(min(len(pathToX), len(pathToY))):
        if pathToX[index] != pathToY[index]:
            # If elements are not same, return the LCA
            return pathToX[index - 1]

    # Return the LCA.
    return pathToX[min(len(pathToX), len(pathToY)) - 1]
#######################################################################################################################

# Space Optimised Approach

# The basic idea of this approach is to find the LCA in a single traversal without using any extra space.

 

# Let us start moving from the root node. Now consider the following situations:

#     If either X or Y is the root node, then the LCA of X and Y will be the root node itself 
#       because the root node is the topmost node in the binary tree.
#     If X and Y exist in the left subtree, then the LCA will be necessarily present in the 
#       left subtree because the farthest common ancestor from the root node will be present in the left subtree.
#     Similarly, if X and Y exist in the right subtree, then the LCA will be necessarily present 
#       in the right subtree.
#     If both X and Y are present in the different subtrees, then the LCA will be the root node.

# We can easily generalize the points mentioned above for any node. Let 

# findLCA(TreeNode* root, int X, int Y) 

#   be a function that returns the LCA of X and Y in the given tree or return -1 if it does not exist.
#   Now consider the steps as follows:

 

# If the root is NULL, then return -1 because LCA will not exist in an empty tree.
# If either the root is equal to X or Y return root. In this case, the root node itself
#  will be LCA because the root is the topmost node in the binary tree.
# Let us find the LCA in the left subtree and store it in a variable leftLCA, i.e.
# leftLCA = findLCA(left-child of the root, X, Y)
# Similarly, find the LCA in the right subtree and store it in a variable rightLCA i.e.
#  rightLCA = findLCA(right-child of the root, X, Y)
# If leftLCA and rightLCA both are not equal to -1, then the root must be the LCA. 
# Because both ‘X’ and ‘Y’ are present in two different subtrees.
# Otherwise,  the LCA must be present in either of the two subtrees.
#     If leftLCA is not equal to -1, return leftLCA.
#     Otherwise, return rightLCA.

# Time Complexity

# O(N), Where N is the number of nodes in the given binary tree.

 

# Since we are doing a pre-order traversal which takes O(N) time. So the overall time complexity will be O(N).
# Space Complexity

# O(N), Where N is the number of nodes in the given binary tree.

 

# Since we are doing a recursive tree traversal and in the worst case (Skewed Trees), 
# all nodes of the given tree can be stored in the call stack. So the overall space complexity will be O(N).

'''
    Time Complexity : O(N)
    Space Complexity : O(N)

    Where 'N' is the number of nodes in the given binary tree.
'''


# Returns the LCA of X and Y or return -1 if it does not exist.
def findLCA(root, x, y):

    # Base Case
    if root == None:
        return -1
    # The root node itself is a LCA
    elif root.data == x or root.data == y:
        return root.data
    else:
        # Recur to find the LCA in the left subtree
        leftLCA = findLCA(root.left, x, y)
        # Recur to find the LCA in the right subtree
        rightLCA = findLCA(root.right, x, y)
        if leftLCA != -1 and rightLCA != -1:
            # The root must be the LCA since both X and Y are present in two different subtrees.
            return root.data
        elif leftLCA != -1:
            # LCA exists in the left subtree.
            return leftLCA
        else:
            # LCA exists in the right subtree.
            return rightLCA


def lowestCommonAncestor(root, x, y):
    return findLCA(root, x, y)