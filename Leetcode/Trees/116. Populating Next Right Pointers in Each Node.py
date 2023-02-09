# You are given a perfect binary tree where all leaves are on the same level,
#  and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next
#  right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function should populate
# each next pointer to point to its next right node, just like in Figure B.
# The serialized output is in level order as connected by the next pointers,
#  with '#' signifying the end of each level.
# Example 2:

# Input: root = []
# Output: []


# Constraints:

# The number of nodes in the tree is in the range [0, 212 - 1].
# -1000 <= Node.val <= 1000

# 3

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                ## if i is not last element
                if i < size - 1:
                    node.next = queue[0] # queue[0] is next element
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

####################################################################################################
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/solutions/1654181/c-python-java-simple-solution-w-images-explanation-bfs-dfs-o-1-optimized-bfs/
# iterative

# Now, we need to populate next pointers of each node with nodes that occur
# to its immediate right on the same level. This can easily be done with BFS.
#  Since for each node, we require the right node on the same level, we will
#  perform a right-to-left BFS instead of the standard left-to-right BFS.

# Before starting the traversal of each level, we would initialize a rightNode
#  variable set to NULL. Then, since we are performing right-to-left BFS,
#   we would be starting at rightmost node of each level. We set the next node
#   of cur as rightNode and update rightNode = cur. This would ensure that each
#   node would be assigned its rightNode properly while traversing from right to left.
# Also, if cur has a child, we would first push its right child and only then its
# left child (since we are doing right-to-left BFS). Once BFS is completed (after queue becomes empty),
#  all next node would be populated and we can finally return root.


class Solution:
    def connect(self, root):
        if not root:
            return None
        q = deque([root])
        while q:
            rightNode = None
            n = len(q)

            for _ in range(n):

                cur = q.popleft()
                cur.next = rightNode
                rightNode = cur  # step back

                if cur.right:
                    q.extend([cur.right, cur.left])
        return root


# Time Complexity : O(N), where N is the number of nodes in the given tree.
#  We only traverse the tree once using BFS which requires O(N).
# Space Complexity : O(W) = O(N), where W is the width of given tree.
#  This is required to store the nodes in queue. Since the given tree is a perfect binary tree,
#   its width is given as W = (N+1)/2 ≈ O(N)

#############################################################################################
# Recursive

# We can also populate the next pointers recursively using DFS.
# This is slightly different logic than above but relies on the fact that the given tree is a perfect binary tree.

# In the above solution, we had access to right nodes since we traversed in level-order.
# But in DFS, once we go to the next level, we cant get access to right node.
#  So, we must update next pointers of the child of each node from the its parent's level itself.
#  Thus at each recursive call -

# If child node exists:

# assign next of left child node as right child node: root -> left -> next = root -> right.
#  Note that, if once child exists, the other exists as well.
# assign next of right child node as left child of root's next (if root's next exists):
# root -> right -> next = root -> next -> left.
# How? We need right immediate node of right child. This wont exist if current root's next node doesnt exists.
#  If next node of current root is present (the next pointer of root would already be populated in above level) ,
#  the right immediate node of root's right child must be root's next's left child because if child of root exists,
#  then the child of root's next must also exist.
# If child node doesn't exist, we have reached the last level, we can directly return since there's no child nodes to populate their next pointers

# The process is very similar to the one illustrated in the image below with just the difference that we are traversing with DFS instead of BFS shown below.

class Solution:
    def connect(self, root):
        if not root:
            return None
        L, R, N = root.left, root.right, root.next
        if L:
            L.next = R
            if N:
                R.next = N.left
            self.connect(L)
            self.connect(R)
        return root

# Time Complexity : O(N), each node is only traversed once
# Space Complexity : O(logN), required for recursive stack.
# The maximum depth of recursion is equal to the height of tree which in this case of perfect binary tree is equal to O(logN)

########################################################
# Space optimized


class Solution:
    def connect(self, root):
        head = root
        while root:
            cur = root
            root = root.left
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                    if cur.next:
                        cur.right.next = cur.next.left
                else:
                    break
                cur = cur.next

        return head

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        levelhead = Node(0)

        while node:

                # needle is sewing next fields in current level
                # first time in a level, it is same as leavelHead (with null next)
                # but as soon as we get a non null child from node
                # needle threads that child into its next, 
                # thus making that child as next levelHead
            needle = levelhead

            # this loop moves node in current level
            while node:
                if node.left:

                    needle.next = node.left
                    needle = needle.next

                if node.right:
                    needle.next = node.right
                    needle = needle.next
                node = node.next # move node to next in same level, end up null at rightmost   
            
            # current level ended in node being null
            # take node fom sentinel's next, which is next levels start
            node = levelhead.next
                
            # levelhead.next grabbed into node above, it has been used
            # so make it null so next time we dont grab again, 
            # if all next lvl is null, it remains null prompting end of run
            levelhead.next = None
        return root

# Time Complexity : O(N), we only traverse each node once, basically doing a standard BFS.
# Space Complexity : O(1), only constant extra space is being used
