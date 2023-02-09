def sortedListToBST(self, head: ListNode) -> TreeNode:
    if head is None:
        return None
    
    if head.next is None:
        return TreeNode(head.val)
    
    slow = head
    fast = head.next
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    if prev:
        prev.next = None
    else:
        head = None # means slow is still at my head
    
    node = TreeNode(slow.val)
    node.left = self.sortedListToBST(head)
    node.right = self.sortedListToBST(slow.next)
    
    return node
