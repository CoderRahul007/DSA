def nodeToRoot(root , data , res):
    if not root:
        return False
    if root.data == data:
        return True
    if nodeToRoot(root.left , data):
        res.append(root.data)
        return True
    if nodeToRoot(root.right , data):
        res.append(root.data)
        return True
    return False

# https://www.youtube.com/watch?v=1Kyc-zQS7eQ