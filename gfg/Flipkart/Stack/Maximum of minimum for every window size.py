# Given an integer array. The task is to find the maximum of the minimum of every window size in the array.
# Note: Window size varies from 1 to the size of the Array.

# Example 1:

# Input:
# N = 7
# arr[] = {10,20,30,50,10,70,30}
# Output: 70 30 20 10 10 10 10 
# Explanation: 
# 1.First element in output
# indicates maximum of minimums of all
# windows of size 1.
# 2.Minimums of windows of size 1 are {10},
#  {20}, {30}, {50},{10}, {70} and {30}. 
#  Maximum of these minimums is 70. 
# 3. Second element in output indicates
# maximum of minimums of all windows of
# size 2. 
# 4. Minimums of windows of size 2
# are {10}, {20}, {30}, {10}, {10}, and
# {30}.
# 5. Maximum of these minimums is 30 
# Third element in output indicates
# maximum of minimums of all windows of
# size 3. 
# 6. Minimums of windows of size 3
# are {10}, {20}, {10}, {10} and {10}.
# 7.Maximum of these minimums is 20. 
# Similarly other elements of output are
# computed.

# Example 2:

# Input:
# N = 3
# arr[] = {10,20,30}
# Output: 30 20 10
# Explanation: First element in output
# indicates maximum of minimums of all
# windows of size 1.Minimums of windows
# of size 1 are {10} , {20} , {30}.
# Maximum of these minimums are 30 and
# similarly other outputs can be computed

# https://www.youtube.com/watch?v=CK8PIAF-m2E
class Solution:
    
    #Function to find maximum of minimums of every window size.
    def maxOfMin(self,arr,n):
        # code here
        s = []
        left = [-1]*n
        right = [n]*n
        
        for i in range(n):
            while s and arr[s[-1]] >= arr[i] :
                s.pop()
            if s:
                left[i] = s[-1]
            s.append(i)
        while s:
            s.pop()
        
        for i in range(n-1 , -1 , -1):
            while s and arr[s[-1]] >= arr[i]:
                s.pop()
            if s:
                right[i] = s[-1]
            s.append(i)
        

        ans = [0]*(n+1)
        for i in range(n):
            len = right[i] - left[i] -1
            ans[len] = max(ans[len] , arr[i])
        
        for i in range(n-1 , 0 , -1):
            ans[i] = max(ans[i] , ans[i+1])
        
        return ans[1:]


###################################################################################################

class Solution:
    
    #Function to find maximum of minimums of every window size.
    def maxOfMin(self,arr,n):
        # code here
        st = []
        ans = [0]*n
        for i in range(n):
            while st and arr[i] < arr[st[-1]]:
                top =  st.pop()
                win = i - (-1 if not st else st[-1]) -1 -1 # -1 agian bcz 0 based indexing in result
                ans[win] = max(ans[win] , arr[top])
            st.append(i)
        
        while st:
            top = st.pop()
            win = n - (-1 if not st else st[-1]) -1 -1
            ans[win] = max(ans[win] , arr[top])
            
        for i in range(n-2 , -1 , -1):
            ans[i] = max(ans[i] , ans[i+1])
        return ans