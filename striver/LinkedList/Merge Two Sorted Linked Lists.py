class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
      
def sortTwoLists(first, second):
    # Write your code here.
    head = Node(-1)
    newhead = head
    
    while first and second :
        if first.data <= second.data :
            head.next = first
            first = first.next            
        else:
            head.next = second
            second = second.next
        head = head.next

    while first:
        head.next = first
        head = head.next
        first = first.next
    while second:
        head.next = second
        head = head.next
        second = second.next     
    return newhead.next