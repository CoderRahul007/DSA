# Example 1:

# Input:
# LinkedList1: 9->6->4->2->3->8
# LinkedList2: 1->2->8->6
# Output: 6 2 8

# Your Task:
# You task is to complete the function findIntersection() which takes the heads
#  of the 2 input linked lists as parameter and returns the head of intersection list.
#  Returned list will be automatically printed by driver code.
# Note: The order of nodes in this list should be same as the order in which
#  those particular nodes appear in input list 1.

# Constraints:
# 1 <= n,m <= 104

# Expected time complexity: O(m+n)
# Expected auxiliary space: O(m+n)
class Solution:
    def findIntersection(self, head1, head2):
        # code here
        # return head of intersection list
        mp = {}
        h1 = Node(0)
        h2 = h1
        l = []
        while head2:
            if not head2.data in mp:
                mp[head2.data] = 1
            else:
                mp[head2.data] += 1
            head2 = head2.next
        while head1:
            if head1.data in mp:
                h1.next = Node(head1.data)
                h1 = h1.next
                mp[head1.data] -=1
                
                if mp[head1.data] == 0:
                     del mp[head1.data]
            head1 = head1.next    

        return h2.next