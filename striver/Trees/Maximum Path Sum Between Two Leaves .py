''' 
    Time Complexity : O(N)
    Space Complexity : O(N)
    
    where 'N' is the number of nodes in the Binary Tree.
'''
def maxPathSumUtil(root, res):
 
    # Base Case
    if root is None:
        return 0
 
    # if root is leaf node we can return root.data
    if not root.left and not root.right:
        return root.data
 
    # Find maximumsum in left and right subtree. Also
    # find maximum root to leaf sums in left and right
    # subtrees ans store them in ls and rs
    ls = maxPathSumUtil(root.left, res)
    rs = maxPathSumUtil(root.right, res)
 
    # If both left and right children exist
    if root.left is not None and root.right is not None:
 
        # update result if needed
        res[0] = max(res[0], ls + rs + root.data)
 
        # Return maximum possible value for root being
        # on one side
        return max(ls, rs) + root.data
 
    # If any of the two children is empty, return
    # root sum for root being on one side
    if root.left is None:
        return rs + root.data
    else:
        return ls + root.data
 
# The main function which returns sum of the maximum
# sum path betwee ntwo leaves. THis function mainly
# uses maxPathSumUtil()
 
 
def maxPathSum(root):
    res = [INT_MIN]
    res1 = maxPathSumUtil(root, res)
    # we have to check if root.left is None or root.right is None
    # for ex:-   10
    #            /  \
    #         None  -5
    # this will return INT_MIN but answer is 5 which is res1
    if root.left and root.right:
        return res[0]
    return max(res[0], res1)
 
 
# Driver program to test above function
root = Node(-15)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(-8)
root.left.right = Node(1)
root.left.left.left = Node(2)
root.left.left.right = Node(6)
root.right.left = Node(3)
root.right.right = Node(9)
root.right.right.right = Node(0)
root.right.right.right.left = Node(4)
root.right.right.right.right = Node(-1)
root.right.right.right.right.left = Node(10)
 
print("Max pathSum of the given binary tree is", maxPathSum(root))
 

# Output
# Max pathSum of the given binary tree is 27
# Time complexity: O(n) where n is the number of nodes
# Auxiliary Space: O(n)



