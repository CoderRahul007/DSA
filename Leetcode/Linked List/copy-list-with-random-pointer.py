##################################################################################

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # recurisve method
        if head == None:
            return None
        if head in self.visited:
            return self.visited[head]
        node = Node(head.val, None, None)
        self.visited[head] = node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node
        # time and space o(n)



############################################################################################3

# easiest
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmap = {None:None}
        curr = head
        while curr:
            hmap[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy = hmap[curr]
            copy.next = hmap[curr.next]
            copy.random = hmap[curr.random]
            curr = curr.next
        return hmap[head]
        
#########################################################################################


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # normal part: constructing the list by going through next elements
        # random part: when we create next elements, some of them might already be created (as we need to hook them to copy)

        if head == None:
            return None
        # create a hashtable to track the created nodes (mapping of node to copy)
        node_copy_map = {}
        cur = head
        prev_copy = None

        # loop through the linked list
        # make a copy of value, if it is not existing in map
        # same for random
        while cur != None:
            if cur not in node_copy_map:
                node_copy_map[cur] = Node(cur.val)  # initialize copy

            cur_copy = node_copy_map[cur]

            if prev_copy is not None:                   # hook copy with previous element
                prev_copy.next = cur_copy

            # Assign random for the copy, create one if it hasn't
            cur_random = cur.random
            if cur_random != None and cur_random not in node_copy_map:
                node_copy_map[cur_random] = Node(cur_random.val)
            if cur_random != None:
                cur_copy.random = node_copy_map[cur_random]

            # shift pointers to next
            prev_copy = node_copy_map[cur]
            cur = cur.next
        return node_copy_map[head]

###########################################################################################

