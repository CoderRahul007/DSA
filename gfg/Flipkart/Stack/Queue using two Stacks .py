# Implement a Queue using 2 stacks s1 and s2 .
# A Query Q is of 2 Types
# (i) 1 x (a query of this type means  pushing 'x' into the queue)
# (ii) 2   (a query of this type means to pop element from queue and print the poped element)

# Example 1:

# Input:
# 5
# 1 2 1 3 2 1 4 2

# Output: 
# 2 3

# Explanation: 
# In the first testcase
# 1 2 the queue will be {2}
# 1 3 the queue will be {2 3}
# 2   poped element will be 2 the queue 
#     will be {3}
# 1 4 the queue will be {3 4}
# 2   poped element will be 3.

def Push(x,stack1,stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    #code here
    stack1.append(x)
    

#Function to pop an element from queue by using 2 stacks.
def Pop(stack1,stack2):
    
    '''
    stack1: list
    stack2: list
    '''
    k = -1
    while stack1:
        k = stack1.pop()
        stack2.append(k)
    if stack2:
        stack2.pop()
    while stack2:
        stack1.append(stack2.pop())
    return k