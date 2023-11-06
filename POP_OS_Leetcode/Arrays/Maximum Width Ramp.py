# Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.

# Find the maximum width of a ramp in A.  If one doesn't exist, return 0.

 

# Example 1:

# Input: [6,0,8,2,1,5]
# Output: 4
# Explanation: 
# The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.

# Example 2:

# Input: [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: 
# The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.

# Problem to solve : for every index, we need to find farthest larger element on its right.

# Not exactly “find” for every index, rather consider. The problem is to find maximum of all such distances, so trick is that for many indices,
#  we can eliminate/reduce that calculation.

# For 6 0 8 2 1 5, when I know that for 0, that idx2 is 5, I needn’t calculate it for numbers occurring between 0 and 5 for the case of idx2=5, 
# since their distance to 5 would anyways be less than the one between 0 to 5.

# Classical two pointer problem. Right pointer expands the range and left pointer contracts it. 
# The trick is that left pointer iterates over original array and right pointer iterates over an array which stores maximum no. 
# on the right for each index.

# How do make sure expanding right pointer is covering all the cases? Since the second array, let's call it rMax array,
#  stores maximum element on the right for each element, it'll always be in decreasing order.
#  So for a particular left, once the condition stops satisfying that element at right is smaller than it, 
# we know we have the answer for that index. All the elements on the right will now be smaller than the one pointing at left. 
# This can be verified with below example:

# index: 0 1 2 3 4 5
# input: 6 0 8 2 1 5
# rMax: 8 8 8 5 5 5

# left and right both start at 0.

# Code:

# public int maxWidthRampII(int[] A) {
#     int n = A.length;
#     int[] rMax = new int[n];
#     rMax[n - 1] = A[n - 1];
#     for (int i = n - 2; i >= 0; i--) {
#       rMax[i] = Math.max(rMax[i + 1], A[i]);
#     }
#     int left = 0, right = 0;
#     int ans = 0;
#     while (right < n) {
#       while (left < right && A[left] > rMax[right]) {
#         left++;
#       }
#       ans = Math.max(ans, right - left);
#       right++;
#     }
#     return ans;
#   }


# Heap Based Solution
import heapq
class Solution:
    def maxWidth(self,A):
        if not A:
            return 0
        st=[]
        st.append((A[-1],len(A)-1))
        for i in range(len(A)-2,-1,-1):
            val=st[-1][0]
            if A[i]>val:
                st.append((A[i],i))
        i=0
        m=0
        while len(st)!=0 and i<len(A):
            while len(st)!=0 and A[i]<=st[-1][0]:
                num=st.pop()
                m=max(m,num[1]-i)
            i+=1
        return m
            
    def maxWidthRamp2(self, A):
        queue = [(A[i],i) for i in range(len(A))]
        print(queue)
        heapq.heapify(queue)
        minVal,minPos = heapq.heappop(queue)
        print(minPos,minVal)
        print(queue)
        maxWidth = 0
        while queue:
            val,pos = heapq.heappop(queue)
            print('While',val,pos)
            if val >= minVal:
                maxWidth = max(maxWidth,pos-minPos)
                print('maxwidth',maxWidth)
            if pos<minPos:
                minPos = pos
                minVal = val  
                print('if',minPos,minVal)
        return maxWidth
s=Solution()
print(s.maxWidth([6,0,8,2,1,5]))

# Essentially, we have this problem to solve : Given an array, for every index, we need to find farthest larger element on its right.

# Approach 1

# Not exactly “find” for every index, rather consider. The problem is to find maximum of all such distances, so trick is that for many indices, we can eliminate that calculation.

# For 6 0 8 2 1 5, when I know that for 0, right end of the ramp (let’s call it idx2) is 5, I needn’t calculate it for numbers occurring between 0 and 5 for the case of idx2=5, since their distance to 5 would anyways be less than the one between 0 to 5.

# Classical two pointer problem. Right pointer expands the range and left pointer contracts it. The trick is that left pointer iterates over original array and right pointer iterates over an array which stores maximum no. on the right for each index.
# O(n)

# public int maxWidthRampI(int[] A) {
#   int n = A.length;
#   int[] rMax = new int[n];
#   rMax[n - 1] = A[n - 1];
#   for (int i = n - 2; i >= 0; i--) {
#     rMax[i] = Math.max(rMax[i + 1], A[i]);
#   }
#   int left = 0, right = 0;
#   int ans = 0;
#   while (right < n) {
#     while (left < right && A[left] > rMax[right]) {
#       left++;
#     }
#     ans = Math.max(ans, right - left);
#     right++;
#   }
#   return ans;
# }

# This approach performs fastest on leetcode.

# Approach 2

# Sort indices in a separate array based on elements.

# For 7 2 5 4, indices array would be [1, 3, 2, 0]. Now these indices are in non-decreasing order of elements. So for any i < j, if index[i] < index[j] (i.e. the smaller element appears before the larger element in original array), it qualifies to be a candidate for the solution. So, iterate and maintain the min index encountered till now.

# O(nlogn)
# Code:

# public int maxWidthRampII(int[] A) {
#   int n = A.length;
#   Integer[] b = new Integer[n];
#   for (int i = 0; i < n; i++) {
#     b[i] = i;
#   }
#   Arrays.sort(b, Comparator.comparingInt(i -> A[i]));
#   int mn = n;
#   int ans = 0;
#   for (int i = 0; i < n; i++) {
#     ans = Math.max(ans, b[i] - mn);
#     mn = Math.min(mn, b[i]);
#   }
#   return ans;
# }

# Approach 3

# Stack based.

# Keep a stack of decreasing order elements.

# Let’s take an example of : [6,0,8,2,1,5]

# Decreasing order stack : 6,0.

# There’s no point of adding 8 to stack.
# Since for any element on the right for which 8 would be a part of solution (i.e. 8 is on the left end of ramp) ,
#  0 can also be the left end for that ramp and provides a larger length of ramp since index of 0 is less than that of 8. 
# This assures as that 8 will never be the left end of our largest ramp.

# Similar explanation applies for 2,1 and 5.

# Now after we have stack, start iterating the array from end considering :

# Current element to be the right end of ramp and top element of the stack to be left end of the ramp. If stack’s top element satisfies the condition, we have a candidate ramp.

# The trick here is: Now we can pop that element out of the stack. Why?
# Let’s say we were right now at index j of the array and stack’s top is at index i.

# So ramp is i..j.

# As we are iterating backwards in the array, the next possible right end of the ramp will be j-1. Even if formes a ramp with i, it’s length would be shorter than our current ramp (i.e. j-i).

# So, no point in keeping in 0 in stack now.

# Keep popping elements off the stack whenever we have a candidate ramp. Since the current candidate ramp is the best ramp considering the stack’s top element to the left end of that ramp

# Code:

# public int maxWidthRampIII(int[] A) {
#   int n = A.length;
#   Stack<Integer> st = new Stack<>();
#   for (int i = 0; i < n; i++) {
#     if (st.empty() || A[i] < A[st.peek()]) {
#       st.push(i);
#     }
#   }
#   int ans = 0;
#   for (int i = n - 1; i >= 0; i--) {
#     while (!st.empty() && A[i] >= A[st.peek()]) {
#       ans = Math.max(i - st.pop(), ans);
#     }
#   }
#   return ans;
# }
