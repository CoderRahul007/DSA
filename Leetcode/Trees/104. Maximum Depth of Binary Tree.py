class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
#################################################################################
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif root.left is None:
            return 1 + self.maxDepth(root.right)
        elif root.right is None:
            return 1 + self.maxDepth(root.left)
        else:
            return 1 + max(self.maxDepth(root.left)  , self.maxDepth(root.right))
############################################################################################                
    # level by level 
    def maxDepth1(self, root):
        deque, depth = collections.deque(), 0
        if root:
            deque.append(root)
        while deque:
            size = len(deque)
            for _ in range(size):
                node = deque.popleft()
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            depth += 1
        return depth

    ####  stack
    def iterative(self, root):
        if not root:
            return 0
        stack = [[root, 1]]
        h = 0
        m = 0
        while len(stack):

            top, h = stack.pop()

            if top.left: 
                stack.append([top.left, h + 1])
            if top.right: 
                stack.append([top.right, h + 1])
            m = max(h, m)

        return m


    # BFS + deque   
    def maxDepth2(self, root):
        if not root:
            return 0
        from collections import deque
        queue = deque([(root, 1)])
        while queue:
            curr, val = queue.popleft()
            if not curr.left and not curr.right and not queue:
                return val
            if curr.left:
                queue.append((curr.left, val+1))
            if curr.right:
                queue.append((curr.right, val+1))