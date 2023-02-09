class Solution:
    # root : the root Node of the given BST
    # target : the target sum
    def isPairPresent(self,root, target): 
        # code here.
        st = set()
        q = [root]
        while q:
            tmp = q.pop(0)
            if (target - tmp.data) in st:
                return 1
            else:
                st.add(tmp.data)
            if tmp.left:
                q.append(tmp.left)
            if tmp.right:
                q.append(tmp.right)
        return 0