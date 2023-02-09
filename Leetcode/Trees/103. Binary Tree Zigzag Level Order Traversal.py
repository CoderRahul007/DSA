#######################################################################
# Iterative
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = collections.deque()
        q.append(root)
        ans = []
        switch = True
        
        while q:
            N = len(q)
            temp = []
            for i in range(N):
                node = q.popleft()                
                if switch:
                    temp.append(node.val)
                else:
                    temp.insert(0,node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            ans.append(temp.copy())
            switch = not switch
            
        return ans
        

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return[]
        stack, res = [root], []

        while stack:
            curr_num_nodes = len(stack)
            curr_res, curr_lvl = [], len(res)
            next_lvl_nodes = []

            while curr_num_nodes > 0:
                curr_num_nodes -= 1
                node = stack.pop(0)
                curr_res.append(node.val)
                if node.left:
                    next_lvl_nodes.append(node.left)
                if node.right:
                    next_lvl_nodes.append(node.right)

            if curr_lvl % 2 == 0:
                res.append(curr_res)
            else:
                res.append(curr_res[::-1])
            stack = next_lvl_nodes
        return res


def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    queue = collections.deque([root])
    res = []
    even_level = False
    while queue:
        n = len(queue)
        level = [0] * n  # initalize the array since we know the length
        for i in range(n):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if even_level:
                level[n-1-i] = node.val
            else:
                level[i] = node.val
        res.append(level)
        even_level = not even_level

    return res


def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
	if not root: return []
	queue = collections.deque([root])
	res = []
	even_level = False
	while queue:
		n = len(queue)
		level = []
		for i in range(n):
			if even_level:
				# pop from right and append from left.
				node = queue.pop()
				# to maintain the order of nodes in the format of [left, right, left, right] 
				# we push right first since we are appending from left
				if node.right: queue.appendleft(node.right)
				if node.left: queue.appendleft(node.left)
			else:
				# pop from left and append from right
				node = queue.popleft()
				# here the order is maintained in the format [left, right, left, right] 
				if node.left: queue.append(node.left)
				if node.right: queue.append(node.right)
			level.append(node.val)
		res.append(level)
		even_level = not even_level
	return res

########################################################################
# Recursive


class Solution(object):
    def zigzagLevelOrder(self, root):
        def dfs(level, direction, root):
            if root:
                if level >= len(res):
                    res.append([])
                if direction == 0:
                    res[level].append(root.val)
                if direction == 1:
                    res[level].insert(0, root.val)
                if root.left:
                    dfs(level+1, (direction+1) % 2, root.left)
                if root.right:
                    dfs(level+1, (direction+1) % 2, root.right)
        res = []
        dfs(0, 0, root)
        return res
