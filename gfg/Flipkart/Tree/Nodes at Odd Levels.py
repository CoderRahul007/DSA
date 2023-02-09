# Given a binary tree of size N, find all the nodes at odd levels.Root is considered at level 1.

# Example 1:

# Input: 
#           1
#        /     \
#       2       3
#     /   \       \
#    4     5       6
#         /  \     /
#        7    8   9

# Output  1 4 5 6
class Solution:
    def nodesAtOddLevels(self,root):
        #code here

        q = [root]
        i = 0
        ans =[]
        flag = True
        
        while q :
            n = len(q)
            while n:
                temp = q.pop(0)
                if flag:
                    ans.append(temp.data)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                n-=1
            flag = not flag
            
        return ans


################################################################################################
        
class Solution:
    def nodesAtOddLevels(self,root):
        #code here

        q = [root]
        i = 0
        ans =[]
        lvl = []
        
        while q and root is not None:
            l = []
            for node in q:
                l.append(node.data)
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
            if i % 2 == 0:
                ans += l
            q = lvl
            lvl = []
            i+=1
        return ans