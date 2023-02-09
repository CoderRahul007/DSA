class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        res=[]
        i=0
        queue=[root]
        level=[]
        while queue and root is not None:
            l=[]
            for node in queue:
                l.append(node.data)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if i>1 and i%2==0:
                res+=l
            else:
                l=l[::-1]
                res+=l
            queue=level
            level=[]
            i+=1
        return res

# Given a Binary Tree. Find the Zig-Zag Level Order Traversal of the Binary Tree.

 

# Example 1:

# Input:
#         3
#       /   \
#      2     1
# Output:
# 3 1 2

# Example 2:

# Input:
#            7
#         /     \
#        9       7
#      /  \     /   
#     8    8   6     
#    /  \
#   10   9 
# Output:
# 7 7 9 8 8 6 9 10 

 