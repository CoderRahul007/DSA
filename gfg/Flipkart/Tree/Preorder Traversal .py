def preorder(root):
    
   list1 = []
   if not root:
       return []
   list1.append((root.data))
   list1 += preorder(root.left)
   list1 += preorder(root.right)
   return list1