class Solution:
    
    #Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root): 
        #Your code here
        if not root:
            return []
        
        queue = []
        level_to_nodes_map = {}
        results = []
        queue.append((0, root))
        
        while(len(queue)):
            count = len(queue)
            while(count):
                level = queue[0][0]
                node = queue[0][1]
                queue.pop(0)
                
                if level in level_to_nodes_map:
                    level_to_nodes_map[level].append(node.data)
                else:
                    level_to_nodes_map[level] = [node.data]
                
                if node.left:
                    queue.append((level - 1, node.left))
                
                if node.right:
                    queue.append((level + 1, node.right))
    
                count = count - 1
                

        for k in sorted(level_to_nodes_map.keys()):
            results.extend(level_to_nodes_map[k])
        
        return results