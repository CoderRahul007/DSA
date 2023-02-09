def LCA(root, n1, n2):
    #code here.
    if not root:
        return root
    if root.data == n1 or root.data == n2:
            return root
    l = LCA(root.left , n1 , n2)
    r = LCA(root.right , n1 , n2)
    
    if l and r:
        return root
    elif l:
        return l
    else:
        return r


#############################################Also
def LCA(root, n1, n2):
    #code here.
    if not root:
        return root
    if root.data < n1 and root.data < n2:
        return LCA(root.right , n1 , n2)
    elif root.data > n1 and root.data > n2:
        return LCA(root.left , n1 , n2)
    return root