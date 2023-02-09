class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nextEl = head.next
            head.next = prev
            prev = head
            head = nextEl
        return prev