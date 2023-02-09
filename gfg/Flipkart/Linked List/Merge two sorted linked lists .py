# not working dont know
def sortedMerge(head1, head2):
    # code here
    h1 = Node(0)
    h2 = h1
    while head1 and head2:
        if head1.data < head2.data:
            h1.next = head1
            h1 = h1.next
            head1 = head1.next
        elif head1.data > head2.data:
            h1.next = head2
            h1 = h1.next
            head2 = head2.next
        else:
            h1.next = head1
            h1.next.next = head2
            h1 = h1.next.next
            head2 = head2.next
            head1 = head1.next
    while head1 :
        h1.next = head1
        h1 = h1.next
        head1 = head1.next
    while head2:
        h1.next = head2
        h1 = h1.next
        head2 = head2.next
    return h2.next


# working
def sortedMerge(head1, head2):
    # code here
    h1 = Node(0)
    h2 = h1
    while head1 and head2:
        if head2.data > head1.data:
            h1.next = head1
            head1 = head1.next
        else:
            h1.next = head2
            head2 = head2.next
            
        h1 = h1.next
    h1.next = head1 or head2
    return h2.next

# recursive
def merge(h1,h2):
    if h1==None:
        return h2
    if h2==None:
        return h1
    
    if h1.val<=h2.val:
        h1.next=merge(h1.next,h2)
        return h1
    else:
        h2.next=merge(h2.next,h1)
        return h2

    return merge(list1,list2)