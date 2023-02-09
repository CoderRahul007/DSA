# #Idea
# The basic idea is to make the given linked list cyclic, then move the head pointer to its new position,
#  finally make it linear.

# #Details

# We want to use k %= length to speed up, because if there are only 3 items, rotating 31 times
#  is the same as rotating 1 time.
# To make the linked list cyclic, we need to get the tail. In addition, we can get length 
# in the same process.
# From observation, we want to move the head pointer length - k units.
# To make the linked list linear again, we want the tail (one before our header), and set it next to None
# Return the head which points to the new head node!
#Code

# https://leetcode.com/problems/rotate-list/solutions/1838907/python-visual-easy-to-understand-o-n-time-o-1-space/?languageTags=python

def rotateRight(self, head, k):

    if not head:
        return []
    
    length, curr = 1, head

    # Get the `tail` and `length`
    while curr.next:
        length += 1
        curr = curr.next
        
    k %= length
    
    # Make it cyclic
    curr.next = head
    
    # Move the head pointer, below is one element before the correct head
    for i in range(length - k - 1):
        head = head.next
    
    # Make it linear, and return the correc head
    last = head
    head = head.next
    last.next = None
    
    return head