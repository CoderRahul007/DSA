

#######################################################################

import heapq


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:  # edge case check
            return head
        heap = []  # instantiate an empty list for heapq
        while head:  # add all the elements in the linked-list to heapq
            heapq.heappush(heap, head.val)
            head = head.next

        newHead = dummy = ListNode(-1)
        while heap:  # pop the elements in the heapq and add those to the linkedlist
            dummy.next = ListNode(heapq.heappop(heap))
            dummy = dummy.next

        return newHead.next


#########################################################################################
# Top Down Merge sort


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Split the list into two halfs
        left = head
        leftEnd = self.getMid(head)
        right = leftEnd.next
        leftEnd.next = None       

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    def getMid(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Merge the list
    def merge(self, list1, list2):
        newHead = tail = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return newHead.next

############################################################################
# Bottom Up Approach Merge Sort


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        def getSize(head):
            # Simply count the length of linked list
            counter = 0
            while head:
                counter += 1
                head = head.next
            return counter

        def split(head, size):
            # given the head & size, return the the start node of next chunk
            for i in range(size-1):
                if not head:
                    break
                head = head.next

            if not head:
                return None
            next_start, head.next = head.next, None  # disconnect

            return next_start

        def merge(l1, l2, dummy_start):
            # Given dummy_start, merge two lists, and return the tail of merged list
            curr = dummy_start
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next, l1 = l1, l1.next
                else:
                    curr.next, l2 = l2, l2.next
                curr = curr.next

            curr.next = l1 if l1 else l2
            while curr.next:
                curr = curr.next  # Find tail
            # the returned tail should be the "dummy_start" node of next chunk
            return curr

        total_length = getSize(head)
        dummy = ListNode(0)
        dummy.next = head
        start, dummy_start, size = None, None, 1

        while size < total_length:
            dummy_start = dummy
            start = dummy.next
            while start:
                left = start
                # start from left, cut with size=size
                right = split(left, size)
                # start from right, cut with size=size
                start = split(right, size)
                # returned tail = next dummy_start
                dummy_start = merge(left, right, dummy_start)
            size *= 2
        return dummy.next
