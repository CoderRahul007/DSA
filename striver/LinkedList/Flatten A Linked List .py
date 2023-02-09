# Problem Statement
# You are given a linked list containing N nodes, where every node in the linked list 
# contains two pointers, first one is ‘NEXT’ which points to the next node in the list
#  and the second one is ‘CHILD’ pointer to a linked list where the head is this node. 
#  And each of these child linked lists is in sorted order.
# Your task is to flatten this linked such that all nodes appear in a single layer or
#  level while the nodes should maintain the sorted order.

#  https://takeuforward.org/data-structure/flattening-a-linked-list/

############################################################
class Node:
    def __init__(self, data):

        self.data = data
        self.next = None
        self.child = None

    def __del__(self):
        if(self.next):
            del self.next

def merge(head1 , head2):
    while head1.child and head2 :
        if head1.child.data <= head2.data:
            head1 = head1.child 
        else:
            temp = head2.child
            head2.child = head1.child
            head1.child = head2
            head1 = head2
            head2 = temp
    if not head1.child :
        head1.child = head2
    
        
def flattenLinkedList(head):
    # write your code here
    down = head
    while down.next != None:
        merge(down , down.next)
        temp = down.next
        down.next = None
        down = temp
    return head


########################################################################################

# class TUF
# {
#     Node mergeTwoLists(Node a, Node b) {
        
#         Node temp = new Node(0);
#         Node res = temp; 
        
#         while(a != null && b != null) {
#             if(a.data < b.data) {
#                 temp.bottom = a; 
#                 temp = temp.bottom; 
#                 a = a.bottom; 
#             }
#             else {
#                 temp.bottom = b;
#                 temp = temp.bottom; 
#                 b = b.bottom; 
#             }
#         }
        
#         if(a != null){
#           temp.bottom = a; 
#         } else {
#           temp.bottom = b;
#         }
#             
#        
#         return res.bottom; 
    
#     }
#     Node flatten(Node root)
#     {
       
#             if (root == null || root.next == null) 
#                 return root; 
      
#             // recur for list on right 
#             root.next = flatten(root.next); // go till end
      
#             // now merge 
#             root = mergeTwoLists(root, root.next); // last two roots
      
#             // return the root 
#             // it will be in turn merged with its left 
#             return root; 
#     }
# }
# Time Complexity: O(N), where N is the total number of nodes present

# Reason: We are visiting all the nodes present in the given list.

# Space Complexity: O(1)

# Reason: We are not creating new nodes or using any other data structure.