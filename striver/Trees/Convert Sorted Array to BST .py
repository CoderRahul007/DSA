#####################################################################
# Python code to convert a sorted array
# to a balanced Binary Search Tree

# binary tree node
class Node:
	def __init__(self, d):
		self.data = d
		self.left = None
		self.right = None

# function to convert sorted array to a
# balanced BST
# input : sorted array of integers
# output: root node of balanced BST
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        total_nums = len(nums)
        if not total_nums:
            return None

        mid_node = total_nums // 2
        return TreeNode(
            nums[mid_node], 
            self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node + 1 :])
        )
# Time Complexity: O(n log n)
# Space Complexity: O(n)


########################################################################
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None
            mid = (left + right)//2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        l = 0
        r = len(nums)-1
        return helper(l, r)


#########################################################################
'''
    Time Complexity  : O(N)
    Space Complexity : O(log(N))

    Where N is the total number of elements in the given array.
'''

class TreeNode :
    def __init__(self, val) :
        self.val = val
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right


# 'nodeData' struct to store root node of subtree and their respective range in given array.
class nodeData:

    def __init__(self, node, low, high):
        self.node = node
        self.low = low
        self.high = high


def sortedArrToBST (arr,n):

    '''
        Initialise a root node with 'val' = -1 and range [ 0:n-1 ] and append it into a stack data structure.
        Later on we will update its 'val' to arr['mid'], where 'mid' is middle index of   [0:n-1].
    '''

    root = TreeNode(-1)
    st = []

    node = nodeData(root, 0, n - 1)
    st.append(node)

    while len(st) >0 :
        curNode = st.pop()

        # Find 'mid' for the currNode and update node with arr[mid].
        mid = curNode.low + (curNode.high - curNode.low) // 2
        curNode.node.val = arr[mid]

        # Push the left part of array, that makes left subtree of current node.
        if (curNode.low < mid):
            curNode.node.left = TreeNode(-1)
            node = nodeData(curNode.node.left, curNode.low, mid - 1)
            st.append(node)

        # Push the right part of array, that makes right subtree of current node
        if (curNode.high > mid):
            curNode.node.right = TreeNode(-1)
            node = nodeData(curNode.node.right, mid + 1, curNode.high)
            st.append(node)
     
    # Return root of tree.
    return root