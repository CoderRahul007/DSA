def reverseLinkedList(head):
    # Write your code here.
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev