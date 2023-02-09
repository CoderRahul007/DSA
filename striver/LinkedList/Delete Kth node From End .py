def removeKthNode(head, k):
    # Write your function here.
    if not head:
        return None
    if k == 0:
        return head
    slow = fast = head
    while k > 0: # go till K 
        fast = fast.next
        k-=1
    # fast is at Kth node
    if not fast:
        return head.next
    while fast.next: # now start from head and go till fast is not None
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head
  
##############################################################################

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, head, n):
        if not head:
            return head
        slow, fast = head, head
        for _ in range(n): # till 4 , 13 node
            if fast.next:
                fast = fast.next
            else:
                return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
            # slow will go till 9 node
        slow.next = slow.next.next
        return head

# [7,6,9,4,13,2,8], n = 4
# 

###################################################################################



# class Solution {
#     public ListNode removeNthFromEnd(ListNode head, int n) {
#         ListNode start = new ListNode();
#         start.next = head;
#         ListNode fast = start;
#         ListNode slow = start;     

#         for(int i = 1; i <= n; ++i)
#             fast = fast.next;
    
#         while(fast.next != null)
#         {
#             fast = fast.next;
#             slow = slow.next;
#         }
        
#         slow.next = slow.next.next;
        
#         return start.next;
#     }
# }

