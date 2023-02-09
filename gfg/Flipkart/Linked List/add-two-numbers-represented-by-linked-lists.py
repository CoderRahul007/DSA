
# 2
# 4 5
# 3
# 3 4 5
# out - 795

def addTwoLists(self, p1, p2):
    # code here
    # return head of sum list
    c = 0

    head = Node(-1)
    
    last = head
    
    while p1 != None or p2 != None:      
        num = c
        
        if(p1 != None):
            num, p1 = num + p1.data, p1.next
        
        if(p2 != None):
            num, p2 = num + p2.data, p2.next
        
        c = num // 10
        num = num % 10
        
        new_node = Node(num)
        new_node.next = None
        last.next = new_node
        last = new_node

            
    
    if(c > 0):
        new_node = Node(c)
        last.next = new_node
        last = new_node
    
    
    return head.next


# N = 2
# valueN[] = {4,5}
# M = 3
# valueM[] = {3,4,5}
# Output: 3 9 0  
# Explanation: For the given two linked
# list (4 5) and (3 4 5), after adding
# the two linked list resultant linked
# list will be (3 9 0).
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        dummy = Node(None)
        curr = dummy
        carry = 0
        first = self.reverse(first)
        second = self.reverse(second)
        while first or second or carry == 1:
            msum = 0
            if first:
                msum += first.data
                first = first.next
            if second:
                msum += second.data
                second = second.next
            msum += carry
            carry = msum//10
            newNode = Node(msum%10)
            curr.next = newNode
            curr = curr.next
        return self.reverse(dummy.next)
    #Function to add two numbers represented by linked list.
    def reverse(self,head):
        mprev = None
        current = head
        mnext = None
       
        while current:
            mnext = current.next
            current.next = mprev
            mprev = current
            current = mnext
        return mprev