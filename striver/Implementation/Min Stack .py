# Question: Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(),
# isEmpty(), isFull() and an additional operation getMin() which should return minimum element from the SpecialStack.
#  All these operations of SpecialStack must be O(1). To implement SpecialStack, you should only use standard
#  stack data structure and no other data structure like arrays, list etc.


class stack:
  
  def __init__(self):
  
    self.array = []
    self.top = -1
    self.max = 100  
  
  # Stack's member method to check 
  # if the stack is empty
  def isEmpty(self):
  
    if self.top == -1:
      return True
    else:
      return False  
  
  # Stack's member method to check
  # if the stack is full  
  def isFull(self):  
      
    if self.top == self.max - 1:
      return True
    else:
      return False   
  
  # Stack's member method to 
  # insert an element to it   
  
  def push(self, data):
  
    if self.isFull():
      print('Stack OverFlow')
      return
    else:
      self.top += 1
      self.array.append(data)     
  
  # Stack's member method to 
  # remove an element from it 
  def pop(self):
  
    if self.isEmpty():
      print('Stack UnderFlow')
      return
    else: 
      self.top -= 1
      return self.array.pop()
  
# A class that supports all the stack  
# operations and one additional 
# operation getMin() that returns the 
# minimum element from stack at 
# any time.  This class inherits from
# the stack class and uses an 
# auxiliary stack that holds 
# minimum elements  
class SpecialStack(stack):
  
  def __init__(self):
    super().__init__()
    self.Min = stack()  
  
  # SpecialStack's member method to 
  # insert an element to it. This method 
  # makes sure that the min stack is also
  # updated with appropriate minimum
  # values 
  def push(self, x):
  
    if self.isEmpty():
      super().push(x)
      self.Min.push(x)
    else:
      super().push(x)
      y = self.Min.pop()
      self.Min.push(y)
      if x <= y:
        self.Min.push(x)
      else:
        self.Min.push(y)  
  
  # SpecialStack's member method to  
  # remove an element from it. This 
  # method removes top element from 
  # min stack also. 
  def pop(self):
  
    x = super().pop()
    self.Min.pop()
    return x  
  
  # SpecialStack's member method 
  # to get minimum element from it.
  def getmin(self):
  
    x = self.Min.pop()
    self.Min.push(x)
    return x
  
# Driver code
if __name__ == '__main__':
    
  s = SpecialStack()
  s.push(10)
  s.push(20)
  s.push(30)
  print(s.getmin())
  s.push(5)
  print(s.getmin())

# Complexity Analysis: 

# Time Complexity: 
# For insert operation: O(1) (As insertion ‘push’ in a stack takes constant time)
# For delete operation: O(1) (As deletion ‘pop’ in a stack takes constant time)
# For ‘Get Min’ operation: O(1) (As we have used an auxiliary stack which has it’s top as the minimum element)
# Auxiliary Space: O(n). 
# Use of auxiliary stack for storing values.

##########################################################################################################
# little Space Optimized

# Space Optimized Version 

# The above approach can be optimized. We can limit the number of elements 
# in the auxiliary stack. We can push only when the incoming element of the 
# main stack is smaller than or equal to the top of the auxiliary stack. 
# Similarly during pop, if the pop-off element equal to the top of the auxiliary stack,
# remove the top element of the auxiliary stack. Following is the modified implementation of push() and pop(). 


''' SpecialStack's member method to 
insert an element to it. This method
makes sure that the min stack is 
also updated with appropriate minimum
values '''
  
def push(x):
    if (isEmpty() == True):
        super.append(x)
        min.append(x)
      
    else:
        super.append(x)
        y = min.pop()
        min.append(y)
  
        ''' push only when the incoming 
           element of main stack is smaller 
        than or equal to top of auxiliary stack '''
        if (x <= y):
            min.append(x)
      
  
  
''' SpecialStack's member method to 
   remove an element from it. This method
   removes top element from min stack also. '''
def pop():
    x = super.pop()
    y = min.pop()
  
    ''' Push the popped element y back 
       only if it is not equal to x '''
    if (y != x):
        min.append(y)
    return x
  
  

# Complexity Analysis:  

# Time Complexity: 
# For Insert operation: O(1) (As insertion ‘push’ in a stack takes constant time)
# For Delete operation: O(1) (As deletion ‘pop’ in a stack takes constant time)
# For ‘Get Min’ operation: O(1) (As we have used an auxiliary which has it’s top as the minimum element)
# Auxiliary Space: O(n). 
# The complexity in the worst case is the same as above but in other cases, it will take slightly 
# less space than the above approach as repetition is neglected.


##################################################################################################################
# Further optimized

# https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/

# In this article, a new approach is discussed that supports minimum with O(1) extra space.
# We define a variable minEle that stores the current minimum element in the stack. Now the 
# interesting part is, how to handle the case when minimum element is removed. To handle this,
#  we push “2x – minEle” into the stack instead of x so that the previous minimum element can 
#  be retrieved using the current minEle and its value stored in the stack. Below are detailed 
#  steps and an explanation of work.

# Push(x) : Inserts x at the top of stack. 

# If the stack is empty, insert x into the stack and make minEle equal to x.
# If the stack is not empty, compare x with minEle. Two cases arise:
# If x is greater than or equal to minEle, simply insert x.
# If x is less than minEle, insert (2*x – minEle) into the stack and make minEle equal to x.
# For example, let previous minEle was 3. Now we want to insert 2. We update minEle as 2 and insert 2*2 – 3 = 1 
# into the stack.

# Pop() : Removes an element from top of stack. 

# Remove element from top. Let the removed element be y. Two cases arise:
# If y is greater than or equal to minEle, the minimum element in the stack is still minEle.
# If y is less than minEle, the minimum element now becomes (2*minEle – y), so update
#  (minEle = 2*minEle – y). This is where we retrieve previous minimum from current minimum and its value in stack.
#   For example, let the element to be removed be 1 and minEle be 2. We remove 1 and update minEle as 2*2 – 1 = 3.
# Important Points: 

# Stack doesn’t hold actual value of an element if it is minimum so far.
# Actual minimum element is always stored in minEle

class Node:
    # Constructor which assign argument to nade's value 
    def __init__(self, value):
        self.value = value
        self.next = None
  
    # This method returns the string representation of the object.
    def __str__(self):
        return "Node({})".format(self.value)
      
    # __repr__ is same as __str__
    __repr__ = __str__
  
  
class Stack:
    # Stack Constructor initialise top of stack and counter.
    def __init__(self):
        self.top = None
        self.count = 0
        self.minimum = None
          
    # This method returns the string representation of the object (stack).
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top {} \n\nStack :\n{}'.format(self.top,out))
          
    # __repr__ is same as __str__
    __repr__=__str__
      
    # This method is used to get minimum element of stack
    def getMin(self):
        if self.top is None:
            return "Stack is empty"
        else:
            print("Minimum Element in the stack is: {}" .format(self.minimum))
  
  
  
    # Method to check if Stack is Empty or not
    def isEmpty(self):
        # If top equals to None then stack is empty 
        if self.top == None:
            return True
        else:
        # If top not equal to None then stack is empty 
            return False
  
    # This method returns length of stack     
    def __len__(self):
        self.count = 0
        tempNode = self.top
        while tempNode:
            tempNode = tempNode.next
            self.count+=1
        return self.count
  
    # This method returns top of stack     
    def peek(self):
        if self.top is None:
            print ("Stack is empty")
        else: 
            if self.top.value < self.minimum:
                print("Top Most Element is: {}" .format(self.minimum))
            else:
                print("Top Most Element is: {}" .format(self.top.value))
  
    # This method is used to add node to stack
    def push(self,value):
        if self.top is None:
            self.top = Node(value)
            self.minimum = value
          
        elif value < self.minimum:
            temp = (2 * value) - self.minimum
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minimum = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        print("Number Inserted: {}" .format(value))
  
    # This method is used to pop top of stack
    def pop(self):
        if self.top is None:
            print( "Stack is empty")
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if removedNode < self.minimum:
                print ("Top Most Element Removed :{} " .format(self.minimum))
                self.minimum = ( ( 2 * self.minimum ) - removedNode )
            else:
                print ("Top Most Element Removed : {}" .format(removedNode))
  
                  
              
      
# Driver program to test above class 
stack = Stack() 
  
stack.push(3)
stack.push(5) 
stack.getMin()
stack.push(2)
stack.push(1)
stack.getMin()     
stack.pop()
stack.getMin()
stack.pop() 
stack.peek()
