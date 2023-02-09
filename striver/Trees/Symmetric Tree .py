'''
    Time complexity: O(N)
    Space complexity: O(H)

    where N is the number of nodes present in the tree.
    H is the height of the tree.
'''

def checkSymmetricity(firstRoot, secondRoot) :

    # Check if both nodes are NULL
    if(firstRoot == None and secondRoot == None) : 
        return True
    

    # Check if one node is NULL, while the other is non-NULL
    if( (firstRoot == None and secondRoot != None) or (firstRoot != None and secondRoot == None) ) :
        return False

    # Check if the number present in the nodes are unequal
    if(firstRoot.data != secondRoot.data) :
        return False  
    

    #     Finally, do the same for left node of firstRoot and right node of secondRoot, 
    #     and right of firstRoot and left of secondRoot.
    return ( checkSymmetricity(firstRoot.right, secondRoot.left) and checkSymmetricity(firstRoot.left, secondRoot.right) )


def isSymmetric(root) :
    return checkSymmetricity(root, root)  