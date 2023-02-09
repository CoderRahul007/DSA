class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:            
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            val = carry % 10           
            n.next = ListNode(val)
            n = n.next
            carry //= 10
        return root.next