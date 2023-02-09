# This is an easy to understand basic DFS approach.
# at any node the recurions basically tries to find out the min depth 
# (either from left path or from right path) and add 1 for current node and then return back 
# to previous function call as the overall minimum depth for that particular node.
# If only one child exists then only that path is considered

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0  # return 0 as depth if empty tree
        elif not root.left and not root.right:
            return 1 # base case handling
        elif not root.left:
            return self.minDepth(root.right)+1 # if no left child then only path is right, so consider right depth
        elif not root.right:
            return self.minDepth(root.left)+1  # if no right child then only path is left, so consider left depth
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
            # if both child exist then pick the minimum one, add one for current node and return min depth

####################################################################################################################

from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        visit_queue = deque([(root, 1)])

        while len(visit_queue) != 0:
            # BFS Traversal

            next_visit, cur_depth = visit_queue.popleft()

            if next_visit is None:
                # empty node or empty tree
                continue
            
            if next_visit.left is None and next_visit.right is None:
                # reach a leaf node
                # get the minimal depth of binary tree, early return
                return cur_depth

            #append left and right child into visit_queue, increase current depth by 1
            visit_queue.append( (next_visit.left, cur_depth + 1) )
            visit_queue.append( (next_visit.right, cur_depth + 1) )

        # depth 0 for empty-tree
        return 0
