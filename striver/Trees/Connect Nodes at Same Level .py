'''
    Time complexity: O(N)
    Space complexity: O(N)
	
    Where 'N' is the number of nodes in a binary tree.
'''

def connectNodes(root):

    # Create queue and enqueue address of root in it.
    que = []
    que.append(root)

    # Number of nodes in current level.
    nodesCount = 1

    while(len(que) != 0):
        previous = None

        # Traversing over nodes of current level.
        while(nodesCount > 0):
            if previous != None:
                previous.next = que[0]

            previous = que[0]
            # Pushing left and right child of current node in queue. 
            if que[0].left != None:
                que.append(que[0].left)

            if que[0].right != None:
                que.append(que[0].right)

            que.pop(0)

            nodesCount -= 1
        
        # Updating number of nodes in current level. 
        nodesCount = len(que)

#########################################################################################################

# Optimized Level Order Traversal

# Approach: Suppose we have already populated the ‘NEXT’ pointers till level ‘L’.
#  Now we can iterate over level ‘L’ using ‘NEXT’ pointers and populate ‘next’ pointers in level ‘L + 1’.

# It can be implemented as follow:

# Create a pointer ‘STARTNODE’ and initialize it by the address of the given root node. 
# The pointer ‘STARTNODE’ will keep the address of the first node of the current level.
# Run a while loop till ‘STARTNODE’ is not equal to NULL, and in each iteration do following:
#     Create a pointer ‘PTR’ and assign the value of ‘STARTNODE’ to it, we will use this pointer
#      ‘PTR’ to iterate over nodes of the current level.
#     Assign the address of the first node of next level to ‘STARTNODE’, if there is no next level then assign NULL to it.
#     Iterate over the current level using the pointer ‘PTR’, the next level is formed by the left or
#      right child of the nodes of the current level, so while iterating you can keep track of nodes
#       encountered on the next level from left to right and connect them accordingly.
# All the next pointers will be populated after this while loop.

# Time Complexity

# O(N), where ‘N’ is the number of nodes in a binary tree.

# The above algorithm is simply a modification of BFS or level order traversal.
# So time complexity is the same as Level order traversal.
# Space Complexity

# O(1).

# We are not using any extra space here.

'''
    Time complexity: O(N)
    Space complexity: O(1)
    
    Where 'N' is the number of nodes in a binary tree.
'''

def connectNodes(root):

    # Keep the address of the first node of the current level.
    startNode = root

    while startNode != None:
        ptr = startNode
        previous = None
        startNode = None

        # Traversing over nodes of current level and populating 'next' pointer of nodes of next level.
        while ptr != None:

            if ptr.left != None:

                if previous != None:
                    previous.next = ptr.left

                # Update 'startNode' with first node of next level if not already done.
                if startNode == None:
                    startNode = ptr.left

                # Update previous pointer
                previous = ptr.left

            if ptr.right != None:
                if previous != None:
                    previous.next = ptr.right

                # Update 'startNode' with first node of next level if not already done.
                if startNode == None:
                    startNode = ptr.right
                
                # Update previous pointer.
                previous = ptr.right

            ptr = ptr.next                
# https://www.youtube.com/watch?v=U4hFQCa1Cq0            