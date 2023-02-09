def findSpiral(root):
    # Code here
    queue=[root]
    level=[]
    result=[]
    i=0
    while queue!=[] and root is not None:
        l=[]
        for node in queue:
            l.append(node.data)
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        if i>1 and i%2==0:
            result+=l[::-1]
        else:
            result+=l
        queue=level
        level=[]
        i+=1
    return result