class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root ):
        # Code here
        if not root:
            return []
        q = [root]
        res = []
        while len(q) > 0:
            node = q.pop(0)
            res.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res