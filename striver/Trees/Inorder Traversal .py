'''
    Time Complexity  : O(N)
    Space Complexity : O(N)

    Where 'N' is the total number of nodes in the binary tree.
'''


def getInOrderTraversal(root):
    # Use answer to store traversal of nodes.
    answer = []

    # Base case.
    if (root == None):
        return answer

    # Create an array that will work as a empty stack.
    s = []
    # Initialize current node as 'ROOT'.
    current = root

    # Run a loop until 'CURRENT'!= None or stack is not empty.
    while (current != None or len(s) != 0):
        while (current != None):
            # Append current node to stack.
            s.append(current)
            # Move to left subtree of 'CURRENT'.
            current = current.left

        # 'CURRENT' must be None at this point.
        current = s[len(s) - 1]
        # Pop top node from stack.
        s.pop()
        # Add data of popped node to answer.
        answer.append(current.data)
        # Visit right subtree of current node.
        current = current.right

    # Return answer.
    return answer
