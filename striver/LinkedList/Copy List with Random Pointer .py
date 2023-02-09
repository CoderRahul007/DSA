# Given a linked list having two pointers in each node. The first one points to the next node of the list,
#  however, the other pointer is random and can point to any node of the list or null. The task is to create
#   a deep copy of the given linked list and return its head. We will validate whether the linked list is a
#    copy of the original linked list or not.
# A deep copy of a Linked List means we do not copy the references of the nodes of the original Linked List 
# rather for each node in the original Linked List, a new node is created.
# For example,

#######################################  Recursive Approach

# The basic idea behind the recursive solution is to consider the linked list like a binary tree. 
# Every node of the Linked List has 2 pointers. So we consider these nodes as belonging to a binary tree.
#  The head of the list becomes the root of the tree. So what we basically have to do now is to traverse 
# the binary tree and clone it. The main issue that we need to tackle here is that of loops. So we can 
# have, 1 1 2 0 -1, we need to handle this in the code. 
# We start from the root node, and we keep traversing the tree (list), and we keep generating new nodes
#  whenever we find a node for which the clone has not been generated. For example, we were at node A, 
# and we used the next pointer to go to node B, and we created B’, which is a new node B with the same
#  data. Also, say there was a random pointer from A to B. In this case, we don’t have to create yet 
# another copy of node B because B’ already exists. We need to take care of this as well.
 
# Steps are as follows:

# Base case: If the current node is not present in the linked list, return null.
# Check if we have already processed the current node (using HashMap), then simply return the cloned version of it.
# Else, create a new node with the data same as the old node, i.e. copy the node.
# Save this value in the HashMap. This is needed to avoid the loops which might be there while traversing the list.
# Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
# Finally, update the next and random pointers for the new node created and return it.

# Time Complexity

# O(N), where ‘N’ is the number of nodes in the list.
 
# Since we are traversing the linked list only once. Therefore, the overall time complexity will be O(N).
# Space Complexity

# O(N), Where ‘N’ is the number of nodes in the list.

 
# We are using O(H) extra space for the call stack where ‘H’ is the height of the recursion tree, 
# and height of a recursion tree could be ‘N’ in the worst case. Thus, the final space complexity is O(N).
'''
	Time complexity: O(N)
	Space complexity: O(N)

	Where 'N' is the number of nodes in the list.
'''

class LinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None
        
def cloneRandomListHelper(head, visitedHash):
    
    if head is None:
        return None
    
    '''
        If we have already processed the current node, 
        then we simply return the cloned version of it.
    '''
    if head in visitedHash.keys():
        return visitedHash.get(head)
    
    '''
        Create a new node with the label same
        as old node. (i.e. copy the node).
    '''
    node = LinkedListNode(head.data)
    
    '''
        Save this value in the hash map. This is needed
        since there might be loops during traversal due to 
        randomness of random pointers and this would
	    help us avoid them.
    '''
    visitedHash[head] = node
    
    '''
        Recursively copy the remaining linked list starting
        once from the next pointer and then from the random pointer.
	    Thus we have two independent recursive calls.
	    Finally we update the next and random pointers for the new node created.
    '''   
    node.next = cloneRandomListHelper(head.next, visitedHash)
    node.random = cloneRandomListHelper(head.random, visitedHash)
    
    return node
    
def cloneRandomList(head):
    
    '''
        HashMap which holds old nodes as keys
        and new nodes as its values.
    '''
    visitedHash = {}
    
    return cloneRandomListHelper(head, visitedHash)



################# Iterative Approach#####################################################

#  Iterative Approach

# The iterative solution to this problem does not model it as a tree and instead simply treats it as a LinkedList. 
# The idea is to use Hashing. Below is the algorithm:

#     We can solve this problem in two passes.
#     In the first pass over the original list, we can create an exact clone of the list with consistent next pointers. 
#     Note that the random pointers are not yet cloned.
#     Additionally, we have a HashMap that maintains the old node to new node mapping. We will need it later on.
#     In the second pass, we clone the random pointer. The way we do it like this. The random pointer for ‘A’ ('A' is the cloned version of node A)
#      is the HashMap value of the node pointed to by the random pointer of A.

# Time Complexity

# O(N), where ‘N’ is the number of nodes in the list. 

# Since we make two passes over the original list with time complexity O(2 * N). Therefore, the overall time complexity will be O(N). 
# Space Complexity

# O(N), where ‘N’ is the number of nodes in the list.
 
# As we are using a HashMap containing a mapping from old list nodes to new list nodes. Since there are N nodes, we have O(N) space complexity.
'''
	Time complexity: O(N)
	Space complexity: O(N)

	Where 'N' is the number of nodes in the list. 
'''

class LinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None

def cloneRandomList(head):
    
    # Initialize two references, one with original list's head.
    origCurr = head
    cloneCurr = None
    
    '''
        Hash map which contains node to node 
        mapping of original and clone linked list.
    '''
    mapp = {}
    
    '''
        Traverse the original list and make
        a copy of that in the clone linked list.
    '''
    while origCurr != None:
        
        cloneCurr = LinkedListNode(origCurr.data)
        mapp[origCurr] = cloneCurr
        origCurr = origCurr.next
        
    # Adjusting the original list reference again.
    origCurr = head
    
    '''
        Traversal of original list again to adjust the next
	    and random references of clone list using hash map.
    '''
    while origCurr != None:
        
        cloneCurr = mapp.get(origCurr,None)
        cloneCurr.next = mapp.get(origCurr.next)
        cloneCurr.random = mapp.get(origCurr.random)
        origCurr = origCurr.next
            
    # Return the head reference of the clone list.
    ans = mapp.get(head,None)
    return ans

##############################################################################################
#  Optimized Iterative Approach

# To optimize the space complexity, we should think of another approach. 
# To reduce the additional space used we will proceed as follows:

#     1. Create the COPY of NODE1 and insert it between NODE1 & NODE2 in the ORIGINAL 
#    linked list. Similarly, create the COPY of node 2 and insert it between NODE2 & NODE3 
#   and so on. Insert the COPY of the Nth node after the Nth node.

#     2. Now COPY the random link in this fashion

#                 ORIGINAL -> next -> random = ORIGINAL -> random -> next

#        This works because ORIGINAL -> next is nothing but a COPY of ORIGINAL and ORIGINAL -> random -> next is nothing but a COPY of random.

#     3. Now restore the ORIGINAL and COPY linked lists in this fashion in a single loop.

#     ORIGINAL -> next = ORIGINAL -> next -> next;
#     COPY -> next = COPY -> next -> next;

#     4. Make sure that ORIGINAL -> next is NULL and return the cloned linked list.
# Time Complexity

# O(N), where ‘N’ is the number of nodes in the list.

 

# Since we make three passes over the original list with a time complexity of O(3 * N). Therefore, the overall time complexity will be O(N).
# Space Complexity

# O(1), i.e. constant space complexity.

 
# Since no extra memory is used except for some variables, thus, the space complexity will be O(1).
'''
    Time complexity: O(N)
	Space complexity: O(1)

	Where 'N' is the number of nodes in the list.
'''

class LinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None

# This function clones a given linked list in O(1) space.
def cloneRandomList(head):
    
    curr = head
    temp = None
    
    # Insert additional node after every node of original list.
    while curr != None:
        temp = curr.next
        
        # Inserting node.
        curr.next = LinkedListNode(curr.data)
        curr.next.next = temp
        curr = temp
        
    curr = head
    
    # Adjust the random pointers of the newly added nodes.
    while curr != None:
        if curr.next != None:
            if curr.random != None:
                curr.next.random = curr.random.next
                
        # Move to the next newly added node by skipping an original node.       
        if curr.next != None:
            curr = curr.next.next
            
        else:
            curr = curr.next
            
    original = head
    copy = None
    
    if head != None:
        copy = head.next
    
    # Save the start of copied linked list.
    temp = copy
    
    # Now separate the original list and copied list.
    while original != None and copy != None:
        
        if original.next != None:
            original.next = original.next.next
            
        if copy.next != None:
            copy.next = copy.next.next
            
        original = original.next
        copy = copy.next
        
    return temp

    # https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)