class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        fast  = head
        slow = head
        
        if head == None:
            return -1
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow.data
            