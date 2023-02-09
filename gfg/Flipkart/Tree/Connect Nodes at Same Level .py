class Solution:
    #Function to connect nodes at same level.
    def connect(self, root):
        if not root:
            return root
        queue = [root]
       
        while queue:
            size = len(queue)
         
            # for keeping track of previous node
            prev = Node(None)
            for i in range(size):
                temp = queue.pop(0)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                if prev != None:
                    prev.nextRight = temp
                    prev = temp
            prev.nextRight = None