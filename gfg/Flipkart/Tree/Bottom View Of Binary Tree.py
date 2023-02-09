class Solution:
    def bottomView(self, root):
        freq=dict()
        q=deque()
        q.append([root,0])
        while q:
            x=q.popleft()
            freq[x[1]]=x[0].data
            if x[0].left!=None:
                q.append([x[0].left,x[1]-1])
            if x[0].right!=None:
                q.append([x[0].right,x[1]+1])
        print(freq)
        temp=[]
        for i in sorted (freq): # sorted keys
            temp.append(freq[i])
        return temp


# Given a binary tree, print the bottom view from left to right.
# A node is included in bottom view if it can be seen when we look at the tree from bottom.

#                       20
#                     /    \
#                   8       22
#                 /   \        \
#               5      3       25
#                     /   \      
#                   10    14

# For the above tree, the bottom view is 5 10 3 14 25.
# If there are multiple bottom-most nodes for a horizontal distance from root,
#  then print the later one in level traversal. For example, in the below diagram, 
# 3 and 4 are both the bottommost nodes at horizontal distance 0, we need to print 4.

#                       20
#                     /    \
#                   8       22
#                 /   \     /   \
#               5      3 4     25
#                      /    \      
#                  10       14

# For the above tree the output should be 5 10 4 14 25.
 