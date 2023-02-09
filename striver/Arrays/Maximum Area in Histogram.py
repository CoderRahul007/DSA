
class Solution():
    def maxHist(self, row):
        # Create an empty stack. The stack holds
        # indexes of hist array / The bars stored
        # in stack are always in increasing order
        # of their heights.
        stack = []
 
        # Top of stack
        top_val = 0
 
        # Initialize max area in current
        max_area = 0
        # row (or histogram)
 
        area = 0  # Initialize area with current top
 
        # Run through all bars of given
        # histogram (or row)
        i = 0
        while (i < len(row)):
 
            # If this bar is higher than the
            # bar on top stack, push it to stack
            if (len(stack) == 0) or (row[stack[-1]] <= row[i]): # if incoming value greater than stack top or stack empty
                stack.append(i)
                i += 1
            else:
 
                # If this bar is lower than top of stack,
                # then calculate area of rectangle with
                # stack top as the smallest (or minimum
                # height) bar. 'i' is 'right index' for
                # the top and element before top in stack
                # is 'left index'
                top_val = row[stack.pop()] # 3
                area = top_val * i 
                # i is the right smaller since its less than the top of stack 
                # left smaller will  be 0 since stack is empty
 
                if (len(stack)):
                    area = top_val * (i - stack[-1] - 1) # since the stack elements are in
                    # increasing order so left smaller will be the top of stack
                    # i right smaller  and stack[-1] is the left smaller
                max_area = max(area, max_area)
 
        # Now pop the remaining bars from stack
        # and calculate area with every popped
        # bar as the smallest bar
        while (len(stack)):
            top_val = row[stack.pop()]
            area = top_val * i
            if (len(stack)):
                area = top_val * (i - stack[-1] - 1)
 
            max_area = max(area, max_area)
 
        return max_area

###########################################################################################################
# other sol
#  Stack Based Approach

# For every bar ‘X’, we calculate the area with ‘X’ as the smallest bar in the rectangle.
#  If we calculate such an area for every bar ‘X’ and find the maximum of all areas, our
#  task is done. How to calculate the area with ‘X’ as the smallest bar? We need to know
#  the index of the first smaller (smaller than ‘X’) bar on the left of ‘X’ and the index
#  of the first smaller bar on the right of ‘X’. Let us call these indexes ‘LEFT_INDEX' and ‘RIGHT_INDEX’ respectively.

 

# We traverse all histograms from left to right, maintaining a stack of histograms. 
# Every histogram is pushed to stack once. A histogram is popped from the stack when 
# a histogram of smaller height is seen. When a histogram is popped, we calculate the 
# area with the popped histogram as the smallest histogram. How do we get the left and 
# right indexes of the popped histogram – the current index tells us the ‘RIGHT_INDEX’ 
# and the index of the previous item in the stack is the ‘LEFT_INDEX'.

 

# Create an empty stack.
# Start from the first histogram bar, and do the following for every bar ‘heights[i]’ where ‘I’ varies from 0 to ‘N’-1.

# If the stack is empty or heights[i] is higher than the bar at top of the stack, then push ‘I’ to the stack.
# If this bar is smaller than the top of the stack, then keep removing the top of the stack while the top of
#  the stack is greater. Let the removed bar be heights[tp]. Calculate the area of the rectangle with heights[tp]
#  as the smallest bar. For heights[tp], the ‘left index’ is the previous (previous to tp) item in the stack and 
# the ‘RIGHT_INDEX'  is ‘I’ (current index).
# If the stack is not empty, then one by one remove all bars from the stack and do step 4 for every removed bar.

# Time Complexity

# O(N), where ‘N’ is the number of elements in the given array/list.

 

# Since every bar is pushed and popped only once, so the overall total time complexity will be O(N).
# Space Complexity

# O(N), where N is the number of elements in the given array/list.

 
'''
    Time Complexity = O(N)
    Space Complexity = O(N)
    
    Where N is the number of elements in the given array/list.
'''

def largestRectangle(heights):

    n = len(heights)

    ''' 
        The stack holds indexes of heights[] array. 
        The bars stored in stack are always in increasing 
        order of their heights.
    '''
    stack = list()

    # Initialize max area.
    maxArea = 0

    # To store top of stack.
    topOfStack = 0

    # To store area with top bar as the smallest bar.
    areaWithTop = 0

    # Run through all bars of given histogram.
    i = 0
    while i < n:
        ''' 
            If this bar is higher than the bar on top stack, 
            push it to stack.
        '''
        if len(stack) == 0 or (heights[stack[-1]] <= heights[i]):
            stack.append(i)
            i += 1
            print("incoming value greater than stack top ")
            print("After i insert")
            print(stack)
    
        else:
            topOfStack = stack.pop()
            print("incoming value less than stack top")
            print("topofstack " , topOfStack)
            ''' 
                Calculate the area with heights[topOfStack] 
                stack as smallest bar.
            '''
            if len(stack) == 0:                
                print("stack is empty after pop")
                print(topOfStack , heights[topOfStack] , i)
                areaWithTop = heights[topOfStack] * i  
                print("areawithtop " , areaWithTop)
            else:
                print("stack is not empty after pop")                
                areaWithTop = heights[topOfStack] * (i - stack[-1] - 1)
                print("areawithtop " , areaWithTop)
        

            # Update max area, if needed.
            if maxArea < areaWithTop:
                maxArea = areaWithTop
            print("maxarea "  , maxArea)
    ''' 
        Now pop the remaining bars from stack and 
        calculate area with every popped 
        bar as the smallest bar.
    '''
    while len(stack) != 0:
        topOfStack = stack.pop()

        if len(stack) == 0:
            areaWithTop = heights[topOfStack] * i
    
        else:
            areaWithTop = heights[topOfStack] * (i - stack[-1] - 1)

        if maxArea < areaWithTop:
            maxArea = areaWithTop
    

    return maxArea        

largestRectangle([3 , 1 , 5 , 6 , 2 , 3])