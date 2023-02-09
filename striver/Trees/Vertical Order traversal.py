'''
    Time Complexity: O(N log N)
    Space Complexity: O(N)

    Where 'N' is the number of nodes in a binary tree.
'''

from collections import deque


def verticalOrderTraversal(root):

    # To store the final result
    result = []

    # Base Case
    if root == None:
        return result

    # Create a dictionary and store vertical order in map.
    store = {}
    # Initial horizontal distance.
    hd = 0
    # Every pair of deque contains node and horizontal distance with respect to the root node.
    level = deque()
    level.append((root, hd))

    while len(level):
        # Pop element from the queue.
        temp = level[0]
        level.popleft()

        hd = temp[1]
        node = temp[0]

        # Insert the value of current node in the vector of map.
        if hd not in store:
            store[hd] = []
        store[hd].append(node.data)

        # For the left subtree, we pass the HD as the Horizontal distance of root minus 1.
        if node.left != None:
            level.append((node.left, hd - 1))
        # For the right subtree, we pass the HD as Horizontal Distance of root plus 1.
        if node.right != None:
            level.append((node.right, hd + 1))

    # Traverse the map and store node values at every horizontal distance (hd).
    for it in sorted(store.keys()):
        for i in store[it]:
            result.append(i)

    # Return the vertical order traversal of the given binary tree.
    return result
