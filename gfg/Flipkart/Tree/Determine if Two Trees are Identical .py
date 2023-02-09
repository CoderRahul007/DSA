def check(r1 , r2):
    if not r1 and not r2:
        return True
    if r1 and not r2:
        return False
    if r2 and not r1:
        return False
    if r1.data != r2.data:
        return False
    l = check(r1.left , r2.left)
    r =  check(r1.right , r2.right)
    return l and r
        
    
class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,root1, root2):
        # Code here
        return check(root1 , root2)