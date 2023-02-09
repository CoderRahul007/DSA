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

#############################################################

class MinStack:

    def __init__(self):
        self.q = deque()
        self.minval = float('inf')

    def push(self, val: int) -> None:
        if not self.q:
            self.minval = val
        else:
            self.minval = min(self.q[0][1], val)
        self.q.appendleft((val, self.minval))

    def pop(self) -> None:
        self.q.popleft()

    def top(self) -> int:
        return self.q[0][0]

    def getMin(self) -> int:
        return self.q[0][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
