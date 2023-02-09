class Inversion:
    def swap(root):
        if root == None:
            return
            
        # Swapping the children     
        temp = root.left
        root.left = root.right
        root.right = temp
        
    def invert(root:Node):
        if root == None:
            return
        q = Queue()
        q.put(root)
        while(q.empty()!=True):
            current = q.popleft()
            swap(current)
            if current.left:
                q.put(current.left)
            if current.right:
                q.put(current.right)
# O(n)
# O(n)