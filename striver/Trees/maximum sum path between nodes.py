def maxPathSum(root):
    maxi = -float('inf')
    maxPathDown(root , maxi)
    return maxi

def maxPathDown(node , maxi):
    if not node:
        return 0
    left = max(0 , maxPathDown(node.left, maxi))
    right = max(0 , maxPathDown(node.right, maxi)) # 0 for handling negative

    maxi = max(maxi , left + right + node.val) # maximum for a subtree
    return max(left , right) + node.val # to select the maximum  of sum for left and right

#O(n)    