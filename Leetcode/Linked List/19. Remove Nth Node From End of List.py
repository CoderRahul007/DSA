
# n ahead - AC in 48 ms

# The standard solution, but without a dummy extra node.
#  Instead, I simply handle the special case of removing the head right after the fast cursor got its head start.

class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast: # if we are deleting head node meand n is equal to length of linked list
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

# 1-> 2 -> 3 -> 4 -> 5 , n = 2 , node = 4 to be deleted
# 1 -> 2 -> 3 , fast at node 3
# 
# after while loop slow at 3 and fast at 5         
