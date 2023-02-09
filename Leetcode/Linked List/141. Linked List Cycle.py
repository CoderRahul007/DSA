# Set Method
def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeSet = set()
        while head:
            if head in nodeSet:
                return True
            nodeSet.add(head)
            head = head.next
        return False

# Two pointers

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True