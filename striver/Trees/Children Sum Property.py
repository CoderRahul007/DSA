# https://www.youtube.com/watch?v=fnmisPM6cVo

def changeTree( root ):
    if not root:
        return
    child = 0
    if root.left:
        child += root.left.data
    if root.right:
        child += root.right.data
    
    # child contains summation of left and right node of a node

    if child >= root.data:
        root.data = child
        # if summation is greater than root then assign root to be summation
    else:
        if root.left : # else assign root data to left and right
            root.left.data = root.data
        elif root.right:
            root.right.data = root.data

    # then recur for left and right subtree 
    changeTree(root.left)
    changeTree(root.right)


    tot = 0
    if root.left:
        tot += root.left.data
    if root.right:
        tot += root.right.data
    if root.left or root.right :
        root.data = tot
    #after that assign left and right data to root
    
    