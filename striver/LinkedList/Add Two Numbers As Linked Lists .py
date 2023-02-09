def addTwoNumbers(head1, head2):
    # Write your code here.
    head = curr = Node(-1)
    c = 0
    while head1 or head2 or c:
        if head1:
            c += head1.data
            head1 = head1.next
        if head2:
            c += head2.data
            head2 = head2.next
        curr.next = Node(c % 10)
        c = c // 10
        curr = curr.next
    return head.next