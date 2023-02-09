#  Stack

#     Instead of storing all the elements in the list. We can prepare a stack in which we store the next smallest element on its top. We update the stack on demand to maintain the next smallest element on its top.
#     We know that for the given root of the binary search tree its smallest element will be the leftmost node’s value in its subtree. So first of all we insert all nodes in the stack till we reach the leftmost node in the tree, which means that our stack now will store the smallest element on its top.
#     When we call the next() function for the first time we need to return the smallest element which is already present at our stack’s top. We will pop the value from the stack and return it. But before returning the value we need to ensure that our stack will contain the next smaller element on its top for further calls of the next() function. So there are two cases we need to check to maintain our stack :
#         First, check if the node we are popping currently is a leaf node or not. If it is a leaf node then in that case we simply pop it because the next top contains the next smaller element already.
#         If the node we are popping is not a leaf then we need to check if it has the right child or not. We don’t need to check the left child because the way we are maintaining the stack, the left child of the node was already processed. So for the right child, we again add all leftmost nodes present in the subtree of the right child including itself in the stack.
#     If you observe we are traversing the binary search tree according to the inorder traversal and maintaining the stack to store the nodes.
#     For the call of hasNext() function we just need to check if the stack is empty or not. If it is empty that means we processed all the nodes so we return false else we will return true.
#     The following image summarizes the above approach:

# Time Complexity

# O(N), where ‘N’ is the number of nodes in the binary search tree.
 


# We are traversing each node one time while performing inorder traversal that will take O(N) time complexity.

# All the calls of the next() function will overall have O(N) complexity.

# Each call of the hasNext() function will work in O(1) complexity.

# Thus, the final time complexity is O(N).
# Space Complexity

# O(N), where ‘N’ is the number of nodes in the binary search tree.



'''
    Time Complexity: O(N)
    Space complexity: O(N)

    Where 'N' is the number of nodes.

'''

class BSTiterator:
    
    # Create a stack which will store smallest element at the top
    st = []

    def __init__(self, root):
        
        # Fill the stack with leftmost nodes present in the subtree of root
        self.leftMostInorder(root)
    

    def next(self):

        # Pop the minimum
        top = self.st[-1]
        self.st.pop()
        
        # Check if it has right child
        if (top.right != None):
        
            # Push leftmost nodes present in the subtree of right child
            self.leftMostInorder(top.right)
        
        return top.data
    
    def hasNext(self):
    
        # If size of stack is greater than zero that means there are still some nodes left for processing
        if (len(self.st) > 0):
            return True
        else:
            return False

    # This function will used to push leftmost nodes in the stack present in the subtree of root
    def leftMostInorder(self, root):
        while (root != None):
            self.st.append(root)
            root = root.left;

####################################################################
'''
    Time Complexity: O(N)
    Space complexity: O(N)

    Where 'N' is the number of nodes.

'''

class BSTiterator:
    
    def __init__(self, root):
        
        # Create a list to store node's value in sorted order
        self.nodeValues = []
        
        # This will be used to iterate over the list
        self.index = 0;
        self.inorder(root)

    def next(self):
        nextSmallest = self.nodeValues[self.index]
        
        # Increment the index for next smallest element
        self.index += 1
        return nextSmallest

    def hasNext(self):
        
        # If index is less than size of the list that means there are still some nodes left for processing
        if (self.index < len(self.nodeValues)):
            return True
        else:
            return False

    # This function will used to perform inorder traversal on the BST
    def inorder(self, root):
        if (root == None):
            return
            
        # Traverse on the left child
        self.inorder(root.left)
        
        # Store the data
        self.nodeValues.append(root.data)
        
        # Traverse on the right child
        self.inorder(root.right)