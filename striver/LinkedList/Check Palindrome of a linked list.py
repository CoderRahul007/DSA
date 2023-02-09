from sys import *
from collections import *
from math import *

from sys import stdin

#Following is the class structure of the LinkedListNode class:
class Node:
    def __init__(self,data):
        
        self.data = data
        self.next = None
            
def reverse(head):
    if not head:
        return None
    prev = None
    post = None
    while head:
        post = head.next
        head.next = prev
        prev = head
        head = post
    return prev
        
    
def isPalindrome(head):
    if not head or not head.next :
        return True
    slow = head
    fast = head
    while fast.next and fast.next.next : # We first travel to mid point of our Linked List.
        slow = slow.next
        fast = fast.next.next
        
    # Lets take example:- 1 -> 2 -> 3 -> 2 -> 1 -> NULL
    
       # After this while loop.....slow will point to 3
        # Our reverse function will reverse the remaining Linked List        
    slow.next = reverse(slow.next)
    slow = slow.next
    # 1-> 2-> 3-> 1-> 2 -> Null
    # *Now......slow is pointing to "1"
    
    flag = True
    while slow:
        if head.data != slow.data:
            flag = False
            break
        slow = slow.next
        head = head.next
    return flag