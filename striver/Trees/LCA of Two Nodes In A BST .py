# For Binary search tree, while traversing the tree from top to bottom the first node which
#  lies in between the two numbers n1 and n2 is the LCA of the nodes, i.e. the first node n 
#  with the lowest depth which lies in between n1 and n2 (n1<=n<=n2) n1 < n2. 

# So just recursively traverse the BST , if node’s value is greater than both n1 and n2 then 
# our LCA lies in the left side of the node, if it is smaller than both n1 and n2, then LCA 
# lies on the right side. Otherwise, the root is LCA (assuming that both n1 and n2 are present in BST)

# Follow the given steps to solve the problem:

# Create a recursive function that takes a node and the two values n1 and n2.
# If the value of the current node is less than both n1 and n2, then LCA lies in the right subtree. 
# Call the recursive function for the right subtree.
# If the value of the current node is greater than both n1 and n2, then LCA lies in the left subtree.
#  Call the recursive function for the left subtree.
# If both the above cases are false then return the current node as LCA.

#####################################################################################################

# Reursion
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Function to find LCA of n1 and n2. The function assumes
# that both n1 and n2 are present in BST
 
 
def lca(root, n1, n2):
 
    # Base Case
    if root is None:
        return None
 
    # If both n1 and n2 are smaller than root, then LCA
    # lies in left
    if(root.data > n1 and root.data > n2):
        return lca(root.left, n1, n2)
 
    # If both n1 and n2 are greater than root, then LCA
    # lies in right
    if(root.data < n1 and root.data < n2):
        return lca(root.right, n1, n2)
 
    return root


####################################################################################################3

'''
    Time Complexity: O(N)
    Space Complexity: O(1)

    where N is the total number of nodes of the BST.
'''


def LCAinaBST(root, P, Q):

    while root != None:

        if root.data < P.data and root.data < Q.data:
            root = root.right

        elif root.data > P.data and root.data > Q.data:
            root = root.left

        else:
            return root