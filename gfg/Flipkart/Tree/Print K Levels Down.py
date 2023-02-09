def printKLevelDown(root , k):
    if k < 0 or not root:
        return
    if k == 0:
        print(root.data)
    printKLevelDown(root.left , k-1)
    printKLevelDown(root.right , k-1)