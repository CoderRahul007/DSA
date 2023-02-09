# Given the heads of two singly linked-lists headA and headB,
# return the node at which the two lists intersect. If the two linked
# lists have no intersection at all, return null.

# For example, the following two linked lists begin to intersect at node c1:

# The test cases are generated such that there are no cycles anywhere in the entire linked structure.

# Note that the linked lists must retain their original structure after the function returns.

# Custom Judge:

# The inputs to the judge are given as follows (your program is not given these inputs):

# intersectVal - The value of the node where the intersection occurs.
# This is 0 if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
# The judge will then create the linked structure based on these inputs
#  and pass the two heads, headA and headB to your program.
#  If you correctly return the intersected node, then your solution will be accepted.
####################################################################################################

#Faster
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        return self.withConstantSpaceAndLinearTime(headA, headB)
      
    def getLength(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length
    
    # Faster than 96.35% (Yay!!)
    def withConstantSpaceAndLinearTime(self, headA, headB):
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        if lenB > lenA:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA
        
        
        diff = lenA - lenB
        while diff:
            headA = headA.next
            diff -= 1
        
        # print(headA.val, headB.val)
        
        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
        return headA


#####################################################################################################
# A little hint that may help people understand

# A) 1  - 2 - 3 -
#                      \
#                       -  5 -6
# B)          4 - /
# To walk all A then B: 1,2,3,5,6,4,5,6
# To walk all B then A: 4,5,6,1,2,3,5,6

# Notice how they both end up at number 5 together after 7 steps

def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa = headA  # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa  # only 2 ways to get out of the loop, they meet or the both hit the end=None

# the idea is if you switch head, the possible difference between length would be countered.
# On the second traversal, they either hit or miss.
# if they meet, pa or pb would be the node we are looking for,
# if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None

##############################################################################################################

# Another Way to Solve This
# spent god damn half a hour to solve this “easy” problem
# Concatenate list A and list B, if there's an intersection, there's a loop,
#  so we need to find the start of the loop if there's any:


class Solution(object):
    def getIntersectionNode(self, A, B):
        if not A or not B:
            return None

        # Concatenate A and B
        last = A
        while last.next:
            last = last.next
        last.next = B

        # Find the start of the loop
        fast = slow = A
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                fast = A
                while fast != slow:
                    slow, fast = slow.next, fast.next
                last.next = None
                return slow

        # No loop found
        last.next = None
        return None
#################################################################################################

# Approach 1- O(N+M) Time| O(N) Space


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
            hashmap = {}
            while headA:
                hashmap[headA]=1
                headA=headA.next
            while headB and headB not in hashmap:
                headB=headB.next
            return headB        