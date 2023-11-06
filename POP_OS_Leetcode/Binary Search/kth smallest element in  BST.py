# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        s=[]
        res=[]
        while s or root and k>=0:
            if root:
                s.append(root)
                root=root.left
            else:
                root=s.pop()
                res.append(root.val)
                k-=1
                root=root.right
            if k==0:
                break
        return res[-1]

# Follow up

#     What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

# Insert and delete in a BST were discussed last week, the time complexity of these operations is O(H)\mathcal{O}(H)O(H), where HHH is a height of binary tree, and H=log⁡NH = \log NH=logN for the balanced tree.

# Hence without any optimisation insert/delete + search of kth element has O(2H+k)\mathcal{O}(2H + k)O(2H+k) complexity. How to optimise that?

# That's a design question, basically we're asked to implement a structure which contains a BST inside and optimises the following operations :

#     Insert

#     Delete

#     Find kth smallest

# Seems like a database description, isn't it? Let's use here the same logic as for LRU cache design, and combine an indexing structure (we could keep BST here) with a double linked list.

# Such a structure would provide:

#     O(H)\mathcal{O}(H)O(H) time for the insert and delete.

#     O(k)\mathcal{O}(k)O(k) for the search of kth smallest.

# bla

# The overall time complexity for insert/delete + search of kth smallest is O(H+k)\mathcal{O}(H + k)O(H+k) instead of O(2H+k)\mathcal{O}(2H + k)O(2H+k).

# Complexity Analysis

#     Time complexity for insert/delete + search of kth smallest: O(H+k)\mathcal{O}(H + k)O(H+k), where HHH is a tree height. O(log⁡N+k)\mathcal{O}(\log N + k)O(logN+k) in the average case, O(N+k)\mathcal{O}(N + k)O(N+k) in the worst case.

#     Space complexity : O(N)\mathcal{O}(N)O(N) to keep the linked list.
