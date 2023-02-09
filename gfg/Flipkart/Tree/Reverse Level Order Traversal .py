def reverseLevelOrder(root):
    # code here
       level=[]
       q=[]
       q.append(root)
       while (q):
           node=q.pop(0)
           level.append(node.data)
           if node.right:
               q.append(node.right)
           if node.left:
               q.append(node.left)
       return level[::-1]

# Given a binary tree of size N, find its reverse level order traversal. ie- the traversal must begin from the last level.

# Example 1:

# Input :
#         1
#       /   \
#      3     2

# Output: 3 2 1
# Explanation:
# Traversing level 1 : 3 2
# Traversing level 0 : 1

# Example 2:

# Input :
#        10
#       /  \
#      20   30
#     / \ 
#    40  60

# Output: 40 60 20 30 10
# Explanation:
# Traversing level 2 : 40 60
# Traversing level 1 : 20 30
# Traversing level 0 : 10


