# Problem Statement
# You have been given a Linked List having ‘N’ nodes and an integer ‘K’.
#  You have to rotate the Linked List by ‘K’ positions in a clockwise direction.
# Example :

#  Given Linked List : 1 2 3 4 -1 and K : 2
#  Then the modified Linked List after K rotation : 3 4 1 2
# For the first test case, after 1st clockwise rotation the modified Linked List will be : 6 1 2 3 4 5
# After, 2nd clockwise rotated the modified Linked List will be : 5 6 1 2 3 4

# For the second test case, after 1st clockwise rotation the modified Linked List will be : 4 2
# After, 2nd clockwise rotated the modified Linked List will be : 2 4
# After, 3rd clockwise rotated the modified Linked List will be : 4 2

# Sample Input 2 :

# 2
# 1 2 3 -1
# 2
# 3 6 9 -1
# 0

# Sample Output 2:

# 2 3 1
# 3 6 9

################################################# Brute Force

# Find the length of the Linked List to check whether the ‘K’ is greater than the Length of the
#  Linked List or not. Take a modulo of ‘K’ with its length if it is greater than the length. 
# Reach the (‘K’+1)th node from last and change the pointers of nodes to get a rotated Linked List.
 

# Here is the algorithm:
 

# Base Condition : If ‘HEAD’ is equal to ‘NULL’ or ‘K’ is equal to 0, then return ‘HEAD’ of the Linked List.
# Create a variable (say, ‘LEN’) which will store the length of the linked list and initialise it to 1.
# Create a temporary node (say, ‘TEMP’) which will be used to find the length of the Linked List and initialise it as ‘HEAD’.
# Run a loop while ‘TEMP’.next is not equal to ‘NULL’:
#     Update ‘TEMP’ as ‘TEMP’.next and increment the ‘LEN’ by 1.
# If ‘LEN’ is less than ‘K’, then update ‘K’ as ‘K’ % ‘LEN’ ( To make ‘K’ come in range of 0 to ‘LEN’).
# Update ‘K’ as ‘LEN’ - ‘K’ (To reach (‘K’+1)th node from end).
# If ‘K’ is equal to ‘LEN’, then:
#     Return ‘HEAD’ (Number of rotations are the same as length which will not change the original list).
# Create a variable (say, ‘COUNT’) which will be used to reach (‘K’ + 1)th node from end and initialise it to 1.
# Create a node (say, ‘CURRENT’) which will store the current node of Linked List and initialise it as ‘HEAD’.
# Run a loop while ‘COUNT’ is less than ‘K’ and ‘CURRENT’ is not equal to ‘NULL’:
#     Update ‘CURRENT’ as  ‘CURRENT’.next and Increment ‘COUNT’ by 1.
# If ‘CURRENT’ is equal to ‘NULL’., then return ‘HEAD’ of the Linked List.
# Update ‘TEMP’.next as ‘HEAD’  (Make the last pointer connect to ‘HRAD’).
# Update ‘HEAD’ as ‘CURRENT’.next (Make Kth node from last the new ‘HEAD’).
# Update ‘CURRENT’.next as ‘NULL’  (Make (‘LEN’ - ‘K’)th point to ‘NULL’).
# Finally, return the ‘HEAD’ of the Linked List.

# Time Complexity

# O(N), where ‘N’ is the size of the Linked List. 
# Since we are traversing all nodes of the Linked List to find the length and after that we are rotating the first ‘K’ nodes of the Linked List. Hence, the overall time complexity will be O(N).
# Space Complexity

# O(1) 
# Since we are not using any extra space, therefore space complexity will be O(1).
'''
    Time Complexity : O(N)
    Space Complexity : O(1)
    
    Where 'N' denotes the size of the linked list.
'''

def rotate(head, k):

    # Base condition.
    if(head == None):
        return head

    len = 1
    temp = head

    # Calculate length of the linked list.
    while(temp.next != None):
        temp = temp.next
        len += 1

    # If k is greater than k bring it in range of 0 - len.
    if(len < k):
        k = k % len

    k = len - k

    # Number of rotations are same as len so no change in LL.
    if(k == len or k == 0):
        return head

    count = 1
    current = head

    while(count < k and current != None):
        current = current.next
        count += 1

    if(current == None):
        return head

    # Changing pointers.
    temp.next = head
    head = current.next
    current.next = None

    return head


######################################################################################################
#  Circular Linked List

# The basic idea of this approach is to first convert a linked list to circular linked
#  list by making the last pointer point to head. Change the pointers of (K+1)th node to get a rotated linked list.
 
# The steps are as follows :
 
#     Base Condition : if ‘HEAD’ is equal to ‘NULL’ or ‘K’ is equal to 0, then return ‘HEAD’ of the linked list.
#     Create a variable (say, ‘LEN’) which will store the length of the linked list and initialise it to 1.
#     Create a temporary node (say, ‘TEMP’) which will be used to find the length of the Linked List and initialise it with ‘HEAD’.
#     Run a loop while ‘TEMP’.next is not equal to ‘NULL’.
#         Update ‘TEMP’ as ‘TEMP’.next and increment the ‘LEN’ by 1.
#     If ‘LEN’ is less than ‘K’, then update ‘K’ as ‘K’ % ‘LEN’ ( To make ‘K’ come in range of 0 to ‘LEN’).
#     If ‘K’ is equal to ‘LEN’, then:
#         return ‘HEAD’ (Number of rotations are the same as length which will not change the original list).
#     Update ‘TEMP'.next as ‘HEAD’. (To make a circular linked list)
#     Re - initialise ‘TEMP’ as ‘HEAD’.
#     Run a loop for ‘i’ = 0 to ‘abs(LEN - K - 1)’ :   (To reach (K+1)th node from end).
#         Update ‘TEMP’ as ‘TEMP’.next
#     Update ‘HEAD’ as ‘TEMP’.next.  (Make Kth node from the last new ‘HEAD’)
#     Update ‘TEMP’.next as ‘NULL’. (Make (K + 1)th node point to ‘NULL’).
#     Finally, return ‘HEAD’

# Time Complexity

# O(N),  where ‘N’ is the size of the Linked List.
 
# We are running a loop from 0 to abs(LEN - K - 1). In the worst case we will be doing ‘N’ number of iterations.

# For example : LEN = 1000, K = 1. abs (LEN - K - 1) = 998, which is approximately equal to ‘N’. Hence, the time complexity is O(N).
# Space Complexity
# O(1).

# Since we are not using any extra space, therefore space complexity will be O(1).
'''
    Time Complexity : O(N)
    Space Complexity : O(1)
    
    Where, ‘N’ is the size of the Linked List.
'''

def rotate(head, k):

    # Base condition.
    if(head == None):
        return head

    len = 1
    tail = head

    # Calculate length of the linked list.
    while(tail.next != None):
        tail = tail.next
        len += 1

    k = k % len

    # Number of rotations are same as len so no change in LL.
    if(len == k or k == 0):
        return head

    # To make a circular linked list.
    tail.next = head

    tail = head

    for i in range(0, abs(len - k - 1), 1):  #  for(int i = 0; i < Math.abs(len - k - 1); i++) 
        tail = tail.next

    # Changing pointers
    head = tail.next
    tail.next = None

    return head