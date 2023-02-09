'''
    Time complexity: O(N^2)
    Space complexity: O(N)
    
    O(N^2), Where ‘N’ is the number of nodes in a binary tree.

 

It is possible that this approach can achieve the worst time complexity in the case of a skew tree.

Suppose we have a ‘right’ skew tree with ‘n’ numbers of nodes then we call height method for root node ‘n’ times, for first ‘right’ child (root->right) ‘n-1’ time and second ‘right’ child (root->right->right) ‘n-2’.

So we call height method ‘  n + n-1 + n-2 + …………+ 1 = n*(n+1)/2’ times. so overall time complexity is o(n^2).  
Space Complexity

O(N), Where ‘N’ is the number of nodes in a binary tree.

 

In the case of the skew tree, we will be using a linear space call stack.


    Where 'N' is number of nodes in binary tree.
'''

def height(root):

    # Base condition.
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def isBalancedBT(root):

    # Base condition.
    if root is None:
        return True

    # Height of left and right child subtree.
    heightLeft = height(root.left)
    heightRight = height(root.right)

    # Allowed only height difference '0, 1, -1' and both subtrees balanced.
    if (isBalancedBT(
            root.left) is True and isBalancedBT(root.right) is True and abs(heightLeft - heightRight) <= 1):
        return True

    # If current subtree is not balanced.
    return False


###############################################################################################
# Optimal Approach

'''
    Time complexity: O(N)
    Space complexity: O(N)
    
    Where 'N' is number of nodes in binary tree.
'''

def helperMethod(root):

    # Base case.
    if(root is None):
        return 0

    leftValue = helperMethod(root.left)
    rightValue = helperMethod(root.right)

    # If one of them is '-1' then child subtree are not balanced.
    if(leftValue == -1 or rightValue == -1):
        return -1

    # Allow only '0, -1, 1' height differencein 'left' child subtree height and 'right' subtree height.
    if(abs(leftValue-rightValue) <= 1):
        return max(leftValue, rightValue)+1

    # If left and right child subtree height more than '2'.
    return -1


def isBalancedBT(root):

    # Base condition.
    if(root is None):
        return True

    # If root tree is balanced.
    if (helperMethod(root) != -1):
        return True
    else:
        return False
