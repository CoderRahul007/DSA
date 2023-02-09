######################################################################3
# Recursive 
class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            INDEX = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[INDEX])
            root.left = self.buildTree(preorder, inorder[:INDEX])
            root.right = self.buildTree(preorder, inorder[INDEX + 1:])

            return root

# O(N**2)


#########################################################
# With Memo

def buildTree(self, preorder, inorder):
    def helper(Lin, Rin):
        if Lin < Rin:
            root = TreeNode(preorder.pop(0))
            rootind = inddict[root.val]
            root.left  = helper(Lin, rootind)
            root.right = helper(rootind+1, Rin)
            return root
    inddict = {val:i for i, val in enumerate(inorder)}
    return helper(0, len(inorder))

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/2279180/python-explained/

############################################ 
# iterative

def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
	d = dict()
	n = len(preorder)
	for i in range(n):
		d[inorder[i]] = i
	def solve(left, right, limit):
		i = limit
		while not(left <= d[preorder[i]] <= right):
			i += 1
		temp = TreeNode(preorder[i])
		mid = d[preorder[i]]
		if(mid != left):
			temp.left = solve(left, mid-1, limit+1) 
		if(mid != right):
			temp.right = solve(mid+1, right, limit+1)   
		return temp
	return solve(0, n-1, 0)
