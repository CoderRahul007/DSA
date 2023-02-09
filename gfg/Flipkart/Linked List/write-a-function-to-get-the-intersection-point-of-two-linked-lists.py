# int detectLoop(Node* head){
#    Node* fast= head->next->next,*slow = head->next;
#    while(fast!=NULL && fast->next!=NULL){
#        if(fast==slow)
#            break;
#        fast = fast->next->next;
#        slow = slow->next;
#    }
#    if(fast==slow){
#        slow =head;
#        while(fast!=slow){
#            fast = fast->next;
#            slow = slow->next;
#        }
#    }
#    return slow->data;
# }
# int intersectPoint(Node* head1, Node* head2)
# {

#    Node* t2 = head2;
#    while(t2->next!=NULL){
#        t2=t2->next;
#    }
#    t2->next = head2;
#    int num = detectLoop(head1);
#    return num;
# }


# We can apply floyds cycle detection logic here:

# traverse till the end of the head2 then link that end node to the head2 which will form a loop.
# now use rabbit tortoise approach to detect the point of intersection of the loop.
# It takes O(1) space which is better than stacks.

class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
     
 
 
def getIntersectionNode(head1,head2):
   
  #finding the total number of elements in head1 LinkedList
    c1=getCount(head1)
   
  #finding the total number of elements in head2 LinkedList
    c2=getCount(head2)
   
  #Traverse the bigger node by 'd' so that from that node onwards, both LinkedList
  #would be having same number of nodes and we can traverse them together.
    if c1 > c2:
        d=c1-c2
        return _getIntersectionNode(d,head1,head2)
    else:
        d=c2-c1
        return _getIntersectionNode(d,head2,head1)
   
   
def _getIntersectionNode(d,head1,head2):
     
     
    current1 = head1
    current2 = head2
     
     
    for i in range(d):
        if current1 is None:
            return -1
        current1=current1.next
     
    while current1 is not None and current2 is not None:
     
    # Instead of values, we need to check if there addresses are same
    # because there can be a case where value is same but that value is
    #not an intersecting point.
        if current1 is current2:
            return current1.data # or current2.data ( the value would be same)
     
        current1=current1.next
        current2=current2.next
   
  # Incase, we are not able to find our intersecting point.
    return -1
   
#Function to get the count of a LinkedList
def getCount(node):
    cur=node
    count=0
    while cur is not None:
        count+=1
        cur=cur.next
    return count
     


if __name__ == '__main__':
  # Creating two LinkedList
  # 1st one: 3->6->9->15->30
  # 2nd one: 10->15->30
  # We can see that 15 would be our intersection point
   
  # Defining the common node
   
  common=Node(15)
   
  #Defining first LinkedList
   
  head1=Node(3)
  head1.next=Node(6)
  head1.next.next=Node(9)
  head1.next.next.next=common
  head1.next.next.next.next=Node(30)
   
  # Defining second LinkedList
   
  head2=Node(10)
  head2.next=common
  head2.next.next=Node(30)
   
  print("The node of intersection is ",getIntersectionNode(head1,head2))