'''
    Time complexity: O(N)
	Space complexity: O(N)

	Where 'N' denotes the number of nodes in the Binary tree.
'''

class   TreeNode :
    def __init__(self, val) :
        self.data = val
        self.left = None
        self.right = None
        
def buildUtil(inorder, post, inStrt, inEnd, pIndex):
     
    # Base case
    if (inStrt > inEnd):
        return None
 
    # Pick current node from Postorder traversal using postIndex and decrement postIndex.
    node = TreeNode(post[pIndex[0]])
    pIndex[0] -= 1
 
    if (inStrt == inEnd):
        return node
 
    iIndex = search(inorder, inStrt, inEnd, node.data)
    
    # Create recursive call for left and right subtree
    node.right = buildUtil(inorder, post, iIndex + 1, inEnd, pIndex)
    node.left = buildUtil(inorder, post, inStrt, iIndex - 1, pIndex)
 
    return node
 

def buildTree(inorder, post, n):
    pIndex = [n - 1]
    return buildUtil(inorder, post, 0, n - 1, pIndex)


def search(arr, strt, end, value):
    
    i = 0

    # Iterate i from strt to end
    for i in range(strt, end + 1):
        
        if (arr[i] == value):
            break
    
    return i


def getTreeFromPostorderAndInorder(postOrder, inOrder):

    # Call buildTreeHelper function 
    root = buildTree(inOrder, postOrder, len(inOrder))
    
    return root