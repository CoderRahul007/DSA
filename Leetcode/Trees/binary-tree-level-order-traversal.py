############################################################
# Recursive

class Solution(object):
    def levelOrder(self, root):

        def dfs(level, root):
            if root:
                if level >= len(res):
                    res.append([])

                res[level].append(root.val)

                if root.left:
                    dfs(level + 1, root.left)
                if root.right:
                    dfs(level + 1, root.right)                    
        res = []
        dfs(0, root)
        return res


################################################################
# Iterative
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        stack = [root]
        res =  []

        while stack:
            cur_num_nodes = len(stack)

            cur_lvl_res = []
            next_lvl_nodes = []

            while cur_num_nodes > 0:

                cur_num_nodes -= 1
                node = stack.pop(0)
                cur_lvl_res.append(node.val)

                if node.left:
                    next_lvl_nodes.append(node.left)
                if node.right:
                    next_lvl_nodes.append(node.right)

            res.append(cur_lvl_res)
            stack = next_lvl_nodes
        return res

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        res = []
        q =deque([(root,0)])
        while q:
            n,l = q.popleft()
            if len(res) < l +1:
                res.append([])
            res[l].append(n.val)
            if n.left:
                q.append((n.left,l+1))
            if n.right:
                q.append((n.right,l+1))
        return res
