# Recursive Solution - 1

# If the left subtree exists, recursively convert the left subtree to Doubly Linked List.
# If the right subtree exists, recursively convert the right subtree to Doubly Linked List.
# When in the left subtree, find the inorder predecessor of the root, make this as the previous of the root and its next as the root.
# Similarly, when in the right subtree, find the inorder successor of the root, make this as the next of the root and its previous as the root.
# Finally, return the leftmost node and return it since this would be the head of the Doubly Linked List.

# O(N^2), where ‘N’ is the number of nodes in the binary tree.

# We are recursively traversing through all the nodes of the tree in
# reverse inorder fashion. After getting the left subtree, we have to traverse 
# it to the end to attach the right subtree
# Space Complexity

# O(N), where ‘N’ is the number of nodes in the binary tree.

'''
    Time Complexity - O(N^2)
    Space Complexity - O(N)

    where 'N' is the number of nodes in the tree.
'''

''' 
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''

def BTtoDLL(root):

    # Base case.
    if(root == None):
        return root

    if(root.left != None):

        left = BTtoDLL(root.left)

        # Inorder predecessor.
        while(left.right != None):
            left = left.right

        left.right = root
        root.left = left

    if(root.right != None):

        right = BTtoDLL(root.right)

        # Inorder successor.
        while(right.left != None):
            right = right.left

        right.left = root
        root.right = right

    while (root.left != None):
        root = root.left

    return root

##########################################################################################

# Recursive Solution - 2

# Start doing inorder traversal from the root.
# While doing the inorder traversal, keep track of the previously visited node; let's call it prev.
# For the current node, make its previous as prev and make the next of prev as the current node.
# This way, we can easily return the head of the doubly linked list.
# While doing all this, keep track of the head of the doubly linked list and finally return it.

# Time Complexity

# O(N), where ‘N’ is the number of nodes in the binary tree.

 

# We are recursively traversing through all the nodes of the tree in reverse inorder fashion.
# Space Complexity

# O(N), where ‘N’ is the number of nodes in the binary tree.

 

# Stack space for recursive calls of N nodes of the binary tree.

'''
    Time Complexity - O(N)
    Space Complexity - O(N)

    where 'N' is the number of nodes in the tree.
'''

''' 
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''

class LinkedList:

    def __init__(self):
        self.head = None
        self.prev = None

    def findHead(self, root):
        
        # Base case.
        if(root == None):
            return

        self.findHead(root.left)

        if(self.prev == None):
            self.head = root

        else:
            root.left = self.prev
            self.prev.right = root

        self.prev = root

        self.findHead(root.right)


def BTtoDLL(root):
    
    ll = LinkedList()
    ll.findHead(root)

    return ll.head
