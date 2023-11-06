'''
 Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3

return [2, -3, 4], since all the values happen only once, return all of them in any order.

Examples 2
Input:

  5
 /  \
2   -5

return [2], since 2 happens twice, however -5 only occur once.

Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer. 
'''
# class Solution:
#     def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
#         def foo(root: TreeNode) -> int:
#             sum = root.val
#             sum += foo(root.left) if root.left else 0
#             sum += foo(root.right) if root.right else 0

#             freq[sum] = freq[sum] + 1 if sum in freq else 0

#             return sum

#         if not root:
#             return []

#         freq = {}
#         foo(root)
#         max_freq = max(freq.values())

#         return [k for k, v in freq.items() if v == max_freq]
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findFrequentTreeSum(self, root):
        def recur(root,d):
            if root is None:             
                return 0
            elif root.right is None and root.left is None:
                if root.val in d:
                    d[root.val]+=1
                    print(root.val,'if')
                else:
                    print(root.val,'else')
                    d[root.val]=1        
                return root.val
            else:            
                l=recur(root.left,d) 
                r=recur(root.right,d) 
                left=l if l else 0
                right=r if r else 0
                s=root.val+left+right
                print(s,root.val,'Root')
                if s in d:
                    d[s]+=1
                else:
                    d[s]=1
                return s

        if not root:
            return []
        d={}
        recur(root,d)
        val=list(d.values())
        m=max(val)
        print(m)
        res=[]
        for i in d.keys():
            if d[i]== m:
                res.append(i)
        return res
ll=TreeNode(3)
rl=TreeNode(5)
l=TreeNode(2,ll,rl)
r=TreeNode(-5)
root=TreeNode(5,l,r)
        
s=Solution()
print(s.findFrequentTreeSum(root))
        
        
        
        