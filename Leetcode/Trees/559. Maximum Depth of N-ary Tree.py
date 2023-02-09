class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        nodes = deque()
        nodes.append((root, 1))
        maxx = 0
        while nodes:
            cur, val = nodes.popleft()
            maxx = val
            if cur.children:
                for child in cur.children:
                    nodes.append((child, val+1))
        return maxx
####################################################################################

class Solution(object):
    def maxDepth(self, root):
        if not root: 
            return 0
        return 1 + max(map(self.maxDepth, root.children or [None]))
######################################################################################

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if root.children:
            return max(self.maxDepth(childNode) + 1 for childNode in root.children)
        return 1        