# You are given N elements and your task is to Implement a Stack in which you can get minimum element in O(1) time.

# An approach that uses O(1) time and O(n) extra space is discussed here.
# In this article, a new approach is discussed that supports minimum with O(1) extra space.
#  We define a variable minEle that stores the current minimum element in the stack.
#  Now the interesting part is, how to handle the case when minimum element is removed. 
# To handle this, we push “2x – minEle” into the stack instead of x so that previous minimum 
# element can be retrieved using current minEle and its value stored in stack. Below are detailed 
# steps and explanation of working.
# Push(x) : Inserts x at the top of stack. 
 

# If stack is empty, insert x into the stack and make minEle equal to x.
# If stack is not empty, compare x with minEle. Two cases arise:
# If x is greater than or equal to minEle, simply insert x.
# If x is less than minEle, insert (2*x – minEle) into the stack and make minEle equal to x.
#  For example, let previous minEle was 3. Now we want to insert 2. We update minEle as 2 and 
# insert 2*2 – 3 = 1 into the stack.
# Pop() : Removes an element from top of stack. 
 

# Remove element from top. Let the removed element be y. Two cases arise:
# If y is greater than or equal to minEle, the minimum element in the stack is still minEle.
# If y is less than minEle, the minimum element now becomes (2*minEle – y), so update
#  (minEle = 2*minEle – y). This is where we retrieve previous minimum from current minimum
#  and its value in stack. For example, let the element to be removed be 1 and minEle be 2.
#  We remove 1 and update minEle as 2*2 – 1 = 3.
# Important Points: 
 

# Stack doesn’t hold actual value of an element if it is minimum so far.
# Actual minimum element is always stored in minEle
class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        #CODE HERE
        if not self.s:
            self.s.append(x)
            self.minEle = x
        else:
            if self.minEle <= x:
                self.s.append(x)
            elif self.minEle > x:
                ans = 2*x - self.minEle
                self.minEle = x
                self.s.append(ans)
    
    def pop(self):
        #CODE HERE
        if not self.s:
            return -1
        temp = self.s.pop()
        if temp >= self.minEle:
            return temp
        else:
            ans = self.minEle
            self.minEle = 2*self.minEle - temp
            return ans

    def getMin(self):
        #CODE HERE
        if not self.s:
            return -1
        return self.minEle