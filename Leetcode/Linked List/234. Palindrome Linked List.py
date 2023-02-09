class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def reverse(head):
            prev = None
            while head:
                nextEl = head.next
                head.next = prev
                prev= head
                head = nextEl
            return prev
        
        # Find Mid
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse from mid to end
        rev = reverse(slow)
        
        # compare
        while rev:
            if head.val != rev.val:
                return False
            head= head.next
            rev = rev.next
        return True

################################################################################################
def isPalindrome(self, head):
    fast = slow = head
    # find the mid node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # reverse the second half
    node = None
    while slow:
        nxt = slow.next
        slow.next = node
        node = slow
        slow = nxt

    # compare the first and second half nodes
    while node: # while node and head:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True