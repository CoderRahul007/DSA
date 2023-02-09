# https://www.youtube.com/watch?v=97rrJF7qYTo

# Input:
# 5 -> 10 -> 19 -> 28
# |     |     |     | 
# 7     20    22   35
# |           |     | 
# 8          50    40
# |                 | 
# 30               45
# Output:  5-> 7-> 8- > 10 -> 19-> 20->
# 22-> 28-> 30-> 35-> 40-> 45-> 50.
# Explanation:
# The resultant linked lists has every 
# node in a single level.
# (Note: | represents the bottom pointer.)

# O(n*m)
def mergeTwoLists(a,b):
   temp = Node(0)
   res = temp
   
   while( a and b):
       if(a.data < b.data):
           temp.bottom = a
           a = a.bottom
           temp = temp.bottom
       else:
           temp.bottom = b
           temp = temp.bottom
           b = b.bottom

   temp.bottom = a if a else b
   return res.bottom

def flatten(root):
   if(root==None or root.next==None):
       return root
   #recursive call
   root.next = flatten(root.next) 
   #merge
   root = mergeTwoLists(root,root.next) # root will point to 19 and root.next to 28
   return root