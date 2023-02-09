def findMiddle(head):
    # Write your code here
    # head denoted head of linked list
    fast = head
    slow = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow
