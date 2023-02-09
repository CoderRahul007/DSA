# Problem Statement
# You are given a Singly Linked List of integers and an integer array 'B' of size 'N'. 
# Each element in the array 'B' represents a block size. Modify the linked list by reversing 
# the nodes in each block whose sizes are given by the array 'B'.
# Note:

# 1. If you encounter a situation when 'B[i]' is greater than the number of remaining nodes
#  in the list, then simply reverse the remaining nodes as a block and ignore all the block sizes from 'B[i]'. 

# 2. All block sizes are contiguous i.e. suppose that block 'B[i]' ends at a node cur, 
# then the block 'B[i+1]' starts from the node just after the node cur.

# Example

# Linked list: 1->2->3->4->5
# Array B: 3 3 5

# Output: 3->2->1->5->4

# We reverse the first block of size 3 and then move to block 2. Now, since the number
#  of nodes remaining in the list (2) is less than the block size (3), we reverse the 
# remaining nodes (4 and 5) as a block and ignore all the block sizes that follow.

######################## Recursion ###############################
###################################################################

# In this approach, we reverse one block at a time and then update the link of that block with the remaining list. 
# Base case: The list is empty or the entire block array has been considered.
# Recursive Rules: 
#     Recursively reverse the list beginning from k+1 th node (where k is the current block size).
#     Reverse the k nodes starting from current head, and connect the new reversed sub-list to the post result.
# We can make the next recursive call to reverse the subsequent list, and in the current function, 
# we will do the local reversal and then connect the new reversed list to the post result we obtain from the sub-problem.
# Let’s consider the following example :

# Linked list: 2->5->7->8->4

# Array B: 2 3 4

# Initially, we have block size k = 2 and the pointer head points to the node with the value 2.
#  We reverse the first block where k = 2 (2->5 changes to 5->2). After this operation, the head 
# pointer points to the tail of this sublist (sublist becomes 5->2 and head points to node with value 2). 

# Now, the node next to the tail of this sublist should be the head of the following block after it has 
# been reversed. The next block is 7->8->4, which after reversal becomes 4->8->7. So, the node next to the
#  tail of the sublist 5->2 should be 4, and after updating this link, the list becomes 5->2->4->8->7.

# This link is updated using recursion. We just update the value of head->next by calling the same function
#  recursively on the node from which the next block starts. Thus, after reversing first block, we update the link as follows:
# head->next = reverse(Node 3 with value 7, block size 3)
# This reverses the second block (7->8->4) and updates the link 2->4. Next, we hit the base case as we reach
#  the end of the linked list.
# Time Complexity
# O(L), where ‘L’ is the number of nodes in the linked list.
# Since we are traversing the entire linked list once, thus the time complexity will be O(L).
# Space Complexity

# O(L / K), where ‘L' is the number of nodes in the linked list and K is the minimum block size from the array ‘B’.

 

# On average, there are L / K recursive calls. Thus, the recursive stack takes O(L / K) space. In the worst
#  case for K = 1, the time complexity will be O(L).
''' 

    Time Complexity : O(L)
    Space Complexity : O(L / K)
    
    Where L is the number of nodes in the Linked-List.
    Where K is the minimum block size from the array B.

'''

# List Node Class.
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None


def reverseKElements(head, n, b, idx):

    # Base case: List is empty or entire block array have been considered.
    if (head == None or idx >= n):
        return head

    # K is the size of the current block.
    K = b[idx]

    # Just move to the next block if size of the current block is zero.
    if (K == 0):
        return reverseKElements(head, n, b, idx + 1)

    cur = head
    prev = None
    ahead = None

    # Variable to keep track of the number of nodes reversed in the current block.
    cnt = 0

    # Reverse nodes until end of list is reached or current block has been reversed.
    while (cur != None and cnt < K):
        ahead = cur.next
        cnt += 1
        cur.next = prev
        prev = cur
        cur = ahead

    # Reverse the next block.
    head.next = reverseKElements(ahead, n, b, idx + 1)
    return prev


def getListAfterReverseOperation(head, n, b):

    # If linked list is empty, return head of the linked list.
    if (head == None):
        return head

    # Calling reverseKElements function to modify the given linked list.
    head = reverseKElements(head, n, b, 0)

    # Return the head of the linked list.
    return head


###################################################################################################################    

''' 

    Time Complexity : O(L)
    Space Complexity : O(1)
    
    Where L is the number of nodes in the Linked-List.

'''

# List Node Class
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None


def getListAfterReverseOperation(head, n, b):
    # If linked list is empty, return head of the linked list.
    if (head == None):
        return None

    # Variable to keep track of the current index in the block array.
    idx = 0

    cur, prev, temp = head, None, None
    tail, join = None, None
    isHeadUpdated = False

    # Reverse nodes until the list is empty or entire block array has been considered.
    while (cur != None and idx < n):

        # K represents the size of the current block.
        k = b[idx]

        # Just move to the next block if size of the current block is zero.
        if (k == 0):
            idx += 1
            continue

        join = cur
        prev = None

        # Reverse nodes until end of list is reached or current block has been reversed.
        while (cur != None and k > 0):
            k -= 1
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # Update the head pointer when reversing the first block.
        if (isHeadUpdated == False):
            head = prev # for first block
            isHeadUpdated = True

        # Tail pointer keeps track of the last node before the current k-reversed linked list.
        # We join the tail pointer with the current k-reversed linked list's head.
        if (tail != None): # not for the first block but after that
            tail.next = prev

        # The tail is then updated to the last node of the current k-reversed linked list.
        tail = join # this join is the last node of each block after reversing
        idx += 1

    # If entire block is iterated and reached at end, then we append the remaining nodes to the
    #  tail of the partial modified linked list.
    if (tail != None):
        tail.next = cur

    # Return the head of the linked list.
    return head



###########################################################################################################################    
from os import *
from sys import *
from collections import *
from math import *

# Following is the class structure of the Node class:   
class Node:
    def __init__(self, data):
       	self.data = data
        self.next = None

def getListAfterReverseOperation(head, n, b):
    # Write your code here.
    dummy = Node(-1)
    prev = dummy
    cur = head
    prev.next = head
    k = 0
    while cur and k < n:
        temp1 = cur
        prev1 = prev
        j = b[k]
        if j > 0:
            while cur and j > 0:
                temp2 = cur
                cur = cur.next
                temp2.next = prev1
                prev1 = temp2
                j-=1
            prev.next = prev1
            prev = temp1
            prev.next = cur
        k+=1
    return dummy.next
    