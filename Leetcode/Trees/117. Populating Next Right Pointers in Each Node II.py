# Given a binary tree

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node.
#  If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Not Complete binary Tree

# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A),
#  your function should populate each next pointer to point to
#  its next right node, just like in Figure B.
#   The serialized output is in level order as connected by the next pointers,
#    with '#' signifying the end of each level.
# Example 2:

# Input: root = []
# Output: []


def connect(self, node):
    head = tail = TreeLinkNode(0)
    while node:
        for c in (node.left, node.right):
            tail.next = c
            if c:
                tail = tail.next
        if node.next:
            node = node.next
        else:
            node, tail = head.next, head


##################################################################

class Solution:
    def connect(self, root):
        if not root:
            return
        if not root.right and not root.left:
            root.next = None
            return
        queue = collections.deque([(root, 1)])
        dic = collections.defaultdict(list)
        while queue:
            node, level = queue.popleft()
            if not node:
                continue
            dic[level].append(node)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        for key, nodes in dic.items():
            i = 0
            while i < len(nodes)-1:
                nodes[i].next = nodes[i+1]
                i += 1
            nodes[i].next = None
# TC -> O(n)
# SC -> O(n)