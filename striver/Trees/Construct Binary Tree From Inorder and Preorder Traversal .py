
# Using HashMap

# The basic idea of this approach is to use HashMap to store a key, value pair of <nodeValue, index> 
# of the inorder sequence. Since we are searching the index of the root node in the inorder sequence
#  in each recursive call, we can optimize it from O(N) to O(1) using HashMap.

 

# Consider a recursive function “constructTree” which takes five arguments: “inStart”, “inEnd”, “pIndex”, 
# “inorderIndex”, “preorder”. Here “inorderIndex” denotes HashMap to store a key, value pair of <nodeValue, index> ,
#  “preorder” denotes the preorder sequence of the binary tree respectively. And, “inStart” and “inEnd” represent 
# the starting and ending index of the inorder sequence of the given subtree and “pIndex” denotes the index of the
#  first element of the preorder sequence of the given subtree.

 

# The node at index “pIndex” in the preorder traversal will be the root node of the binary tree.
#  The idea here is to find the index of the root node in the inorder traversal because that index 
# will divide the inorder traversal into two parts. The index of the root node can be found from “inorderIndex”
#  and store in the variable “inIndex”. Now, the node from index “inStart” to “inIndex” - 1 are the inorder
#  sequence of the left subtree of the root node and the node from index “inIndex” + 1 to “inEnd” are the inorder
#  sequence of the right subtree.

 

# Now, the problem is reduced to constructing the left and right subtree and then linking it to the root node.
#  We can follow the same procedure and build the left and right subtree recursively.

 

# Algorithm:

 

# Consider a HashMap “inorderIndex” to store a key, value pair of <nodeValue, index> of the inorder sequence. Iterate over the inorder sequence and store the value of the inorder item as a key and index of that item as a value in the HashMap.
# Consider a recursive function “constructTree” which takes five arguments: “inStart”, “inEnd”, “pIndex”, “inorderIndex”, “preorder”. Here “inorderIndex” denotes HashMap to store a key, value pair of <nodeValue, index> , “preorder” denotes the preorder sequence of the binary tree respectively. And, “inStart” and “inEnd” represent the starting and ending index of the inorder sequence of the given subtree and “pIndex” denotes the index of the first element of the preorder sequence of the given subtree.
# Initially, set the value of “inStart” equal 0, “inEnd” equal to the size of the “inorder” sequence, and “pIndex” equal to 0.
# If “inStart” is greater than “inEnd” then return a “NULL” node because the subtree is empty.
# Assign the first element of the preorder sequence, denoted by “pIndex” in a variable, say “rootNode”. Make a new tree node with the “rootNode” value. And increment the “pIndex” by 1.
# If “inStart” and “inEnd” are equal, i.e., there is a single node in the given subtree. Return the root.
# Otherwise, find the index of “rootNode” in the inorder sequence using “mp” and store it in a variable, i.e., “inIndex” = inorderIndex[rootNode]
# Now, we can divide the inorder sequence of given subtrees into two parts i.e. [“inStart”, “inIndex” - 1] and [“inIndex” + 1, “inEnd”].
# Recur for the left subtree by calling “constructTree” with arguments “inStart”, “inIndex” - 1, “pIndex”, “inorderIndex”, “preorder” and link the left child of the “rootNode” with the tree returned by the “constructTree”.
# Similarly, recur for the right subtree by calling “constructTree” with arguments “inIndex” + 1, “inEnd”, “pIndex”, “inorderIndex”, “preorder” and link the right child of the “rootNode” with the tree returned by the “constructTree”.
# Return the root node.

# Time Complexity

# O(N), Where ‘N’ is the number of nodes in the given binary tree.

 

# Since we are constructing the tree recursively, there will be  ‘N’ recursive calls,
#  one for each node, and then a search is performed using HashMap, which takes O(1) on average.
#  So, the overall time complexity will be O(N).
# Space Complexity

# O(N), Where ‘N’ is the number of nodes in the given binary tree.

 

# Since we are using the HashMap to store the index of the inorder sequence, which takes O(N)
#  space for ‘N’ elements, also, we are doing a recursive tree traversal, and in the worst case
#  (Skewed Trees), all nodes of the given tree can be stored in the call stack. So the overall 
# space complexity will be O(N).


'''
    Time Complexity : O(N)
    Space Complexity : O(N)

    Where 'N' is the number of nodes in the given binary tree.
'''

# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Constructs the subtree and returns the root node.
def constructTree(inStart, inEnd, inorder, preorder):

    if (inStart > inEnd):

        # Subtree is empty.
        return None

    # Get root node value from preorder sequence.
    rootNode = preorder[constructTree.pIndex]

    # Increment the index denoting the first element of preorder traversal.
    constructTree.pIndex += 1

    # Create the root node with "rootNode" value.
    root = BinaryTreeNode(rootNode)
   
    if (inStart == inEnd ):
        # There is a single node in the given subtree.
        return root
 
    # Else Get the index of root node from the inorder sequence.
    inIndex = buildBinaryTree.inorderIndex[rootNode]
    
    # Recur for the left subtree and right subtree.
    root.left = constructTree(inStart, inIndex - 1, inorder, preorder)
    root.right = constructTree(inIndex + 1, inEnd, inorder, preorder)
 
    return root

def buildBinaryTree(preorder:list, inorder:list):
	
    # Index of the first element of the preorder sequence
    constructTree.pIndex = 0

    # A HashMap to store the <nodeValue, index> pair of inorder sequence.
    buildBinaryTree.inorderIndex = dict()

    for i in range(0, len(inorder)):

        # Storing key, value pair
        buildBinaryTree.inorderIndex[inorder[i]] = i

    root = constructTree(0, len(inorder) - 1, inorder, preorder)
	
    return root