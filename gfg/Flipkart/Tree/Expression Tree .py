class Solution:
    # function should return an integer denoting the required answer
    def evalTree(self, root):
        # Code here
        if root.left is None and root.right is None:
            return int(root.data)
        l = self.evalTree(root.left)
        r = self.evalTree(root.right)
        if root.data == '+':
            return l+r
        elif root.data == '-':
            return l - r
        elif root.data == "*":
            return l*r
        elif root.data == '/':
            return int(l/r)
        return 0