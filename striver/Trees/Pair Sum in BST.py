''' 
    Time Complexity: O(N)
    Space Complexity: O(N)
    
    Where N is the number of nodes in the given BST.
'''

# Function to store inorder traversal of BST in 'nums'.
def inorder(root, nums):
    if root == None:
        return

    inorder(root.left, nums)

    nums.append(root.data)

    inorder(root.right, nums)


def pairSumBST(root, k):
    
    # To store the inorder traversal
    nums = []

    inorder(root, nums)

    # Iterating over the nums list using 2-pointer
    i, j = 0, len(nums) - 1
    
    while i < j:
  
        if nums[i] + nums[j] == k:
            return True

        # If the sum of elements at index 'i' and 'j' is less than target 'k'.
        if nums[i] + nums[j] < k:
            # Increment the left pointer 'i'.
            i += 1

        # If the sum of elements at index 'i' and 'j' is greater than target 'k'. 
        else:
            # Decrement the right pointer 'j'.
            j -= 1

    return False

#################################################################################################################
''' 
    Time Complexity: O(N)
    Space Complexity: O(N)
    
    Where N is the number of nodes in the given BST.
'''


def pairSumBSTHelper(root, k, hashSet):
    if root == None:
        return False

    # Pair found.
    if k - root.data in hashSet:
        return True

    # If the pair is not found then simply insert the root's data into the 'hashSet'.
    hashSet.add(root.data)

    # Recursively call on both left and right subtrees.
    return pairSumBSTHelper(root.left, k, hashSet) or pairSumBSTHelper(root.right, k, hashSet)


def pairSumBST(root, k):

    # Set to store the nodes.
    hashSet = set()

    return pairSumBSTHelper(root, k, hashSet)



##################################################################################################################
''' 
    Time Complexity: O(N)
    Space Complexity: O(N)
    
    Where N is the number of nodes in the given BST.
'''

from collections import deque

def pairSumBST(root, k):
    
    # Deque used as stack.
    '''
        Stack 'start' and 'end' to store the smaller and larger 
        values of BST respectively.
    '''
    start = deque()
    end = deque()

    currNode = root
    
    # Storing left values of BST in 'start'.
    while currNode != None:
        start.append(currNode)
        currNode = currNode.left

    # Setting currNode again pointing to root.
    currNode = root
    
    # Storing right values of BST in 'end'.
    while currNode != None:
        end.append(currNode)
        currNode = currNode.right

    
    while start[-1] != end[-1]:
        # Storing top node's value of 'start' stack in 'val1'.
        val1 = start[-1].data
        # Storing top node's value of 'end' stack in 'val2'.
        val2 = end[-1].data

        # If sum of 'val1' and 'val2' is equal to 'k' then return "true".
        if val1 + val2 == k:
            return True

        # Move to the next greatest closer value.
        if val1 + val2 < k:
            currNode = start[-1].right
            start.pop()
            
            while currNode != None:
                start.append(currNode)
                currNode = currNode.left

        # Move to the next smallest closer value.
        else:
            currNode = end[-1].left
            end.pop()

            while currNode != None:
                end.append(currNode)
                currNode = currNode.right

    # If no two nodes are found, return false.
    return False    