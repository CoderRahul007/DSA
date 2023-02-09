# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = [(l.val, idx) for idx, l in enumerate(lists) if l]  # k elements
        # 1st element of each lists
        heapq.heapify(h)

        head = cur = ListNode(None)
        while h:
            val, idx = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            node = lists[idx] = lists[idx].next
            if node:
                heapq.heappush(h, (node.val, idx))
        return head.next


def mergeKLists_heapq(self, lists):
    h = []
    head = tail = ListNode(0)
    for i in range(len(lists)):
        heapq.heappush(h, (lists[i].val, i, lists[i]))

    while h:
        node = heapq.heappop(h)
        node = node[2]
        tail.next = node
        tail = tail.next
        if node.next:
            i += 1
            heapq.heappush(h, (node.next.val, i, node.next))

    return head.next

# By the way, the runtime of this will be O(nklog(k)) for those who are wondering.
# The while loop will run for as many nodes as there are in lists which is order k * n,
#  where n is the length of the list. Each time during the while loop, heappop and heap replace takes O(log(k))
# time since we'll have at most k elements in our heap. So the runtime of the while loop is O(nklog(k)).
