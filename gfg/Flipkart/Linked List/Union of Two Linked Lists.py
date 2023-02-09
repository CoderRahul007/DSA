def union(head1,head2):
    # code here
    # return head of resultant linkedlist
    s = set()
    while head1 :
        s.add(head1.data)
        head1 = head1.next
    while head2:
        s.add(head2.data)
        head2 = head2.next
    
    ans = Node(0)
    tail = ans
    for i in sorted(s):
        tail.next = Node(i)
        tail = tail.next
    ans = ans.next
    return ans
    

# Given two linked lists, your task is to complete the function makeUnion(), 
# that returns the union of two linked lists. This union should include all the distinct elements only.

# Example 1:

# Input:
# L1 = 9->6->4->2->3->8
# L2 = 1->2->8->6->2
# Output: 1 2 3 4 6 8 9

# Your Task:
# The task is to complete the function makeUnion() which makes the union of 
# the given two lists and returns the head of the new list.

# Note: The new list formed should be in non-decreasing order.

# Expected Time Complexity: O(N * Log(N))
# Expected Auxiliary Space: O(N)