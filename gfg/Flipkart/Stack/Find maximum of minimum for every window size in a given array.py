# Given an integer array of size n, find the maximum of the minimum’s of every window size in the array.
#  Note that window size varies from 1 to n.
# Example:

 
# Input: arr[] = {10, 20, 30, 50, 10, 70, 30} 
# Output: 70, 30, 20, 10, 10, 10, 10
# The first element in the output indicates the maximum of minimums of all 
# windows of size 1. 
# Minimums of windows of size 1 are {10}, {20}, {30}, {50}, {10}, 
# {70} and {30}. Maximum of these minimums is 70
# The second element in the output indicates the maximum of minimums of all 
# windows of size 2. 
# Minimums of windows of size 2 are {10}, {20}, {30}, {10}, {10}, 
# and {30}. Maximum of these minimums is 30
# The third element in the output indicates the maximum of minimums of all 
# windows of size 3. 
# Minimums of windows of size 3 are {10}, {20}, {10}, {10} and {10}. 
# Maximum of these minimums is 20
# Similarly, other elements of output are computed. 

############################################### Naive
# Complexity Analysis:  

# Time Complexity: O(n3). 
# As there is a use of triple nested loop in this approach.
# Auxiliary Space: O(1) 
# As no extra data structure has been used to store the values.
# A naive method to find maximum of
# minimum of all windows of different sizes
INT_MIN = -1000000
def printMaxOfMin(arr, n):
	
	# Consider all windows of different
	# sizes starting from size 1
	for k in range(1, n + 1):
		
		# Initialize max of min for
		# current window size k
		maxOfMin = INT_MIN;

		# Traverse through all windows
		# of current size k
		for i in range(n - k + 1):
			
			# Find minimum of current window
			min = arr[i]
			for j in range(k):
				if (arr[i + j] < min):
					min = arr[i + j]

			# Update maxOfMin if required
			if (min > maxOfMin):
				maxOfMin = min
				
		# Print max of min for current window size
		print(maxOfMin, end = " ")

# Driver Code
arr = [10, 20, 30, 50, 10, 70, 30]
n = len(arr)
printMaxOfMin(arr, n)

################################################################################################################

# Efficient Solution: We can solve this problem in O(n) time. The idea is to use extra space.
#  Below are detailed steps.
# Step 1: Find indexes of next smaller and previous smaller for every element. Next smaller is the 
# nearest smallest element on right side of arr[i]. Similarly, a previous smaller element is the 
# nearest smallest element on the left side of arr[i]. 
# If there is no smaller element on the right side, then the next smaller is n. If there is no smaller
#  on the left side, then the previous smaller is -1.
# For input {10, 20, 30, 50, 10, 70, 30}, array of indexes of next smaller is {7, 4, 4, 4, 7, 6, 7}. 
# For input {10, 20, 30, 50, 10, 70, 30}, array of indexes of previous smaller is {-1, 0, 1, 2, -1, 4, 4}
# This step can be done in O(n) time using the approach discussed in next greater element.
# Step 2: Once we have indexes of next and previous smaller, we know that arr[i] is a minimum of a window of
#  length “right[i] – left[i] – 1”. Lengths of windows for which the elements are minimum are {7, 3, 2, 1, 7, 1, 2}.
#  This array indicates, the first element is minimum in the window of size 7, the second element is minimum in
#  the window of size 3, and so on.
# Create an auxiliary array ans[n+1] to store the result. Values in ans[] can be filled by iterating through 
# right[] and left[] 

#     for (int i=0; i < n; i++)
#     {
#         // length of the interval
#         int len = right[i] - left[i] - 1;

#         // arr[i] is a possible answer for
#         // this length len interval
#         ans[len] = max(ans[len], arr[i]);
#     }
# We get the ans[] array as {0, 70, 30, 20, 0, 0, 0, 10}. Note that ans[0] or answer for length 0 is useless.
# Step 3: Some entries in ans[] are 0 and yet to be filled. For example, we know maximum of minimum for lengths 1, 2, 3 and 7 are 70, 30, 20 and 10 respectively, but we don’t know the same for lengths 4, 5 and 6. 
# Below are few important observations to fill remaining entries 
# a) Result for length i, i.e. ans[i] would always be greater or same as result for length i+1, i.e., ans[i+1]. 
# b) If ans[i] is not filled it means there is no direct element which is minimum of length i and therefore either the element of length ans[i+1], or ans[i+2], and so on is same as ans[i] 
# So we fill rest of the entries using below loop. 

#     for (int i=n-1; i>=1; i--)
#         ans[i] = max(ans[i], ans[i+1]);
# Below is implementation of above algorithm.  


# An efficient Python3 program to find
# maximum of all minimums of windows of
# different sizes
 
def printMaxOfMin(arr, n):
     
    s = [] # Used to find previous
           # and next smaller
 
    # Arrays to store previous and next
    # smaller. Initialize elements of
    # left[] and right[]
    left = [-1] * (n + 1)
    right = [n] * (n + 1)
 
    # Fill elements of left[] using logic discussed on
    # https:#www.geeksforgeeks.org/next-greater-element
    for i in range(n):
        while (len(s) != 0 and
               arr[s[-1]] >= arr[i]):
            s.pop()
 
        if (len(s) != 0):
            left[i] = s[-1]
 
        s.append(i)
 
    # Empty the stack as stack is going
    # to be used for right[]
    while (len(s) != 0):
        s.pop()
 
    # Fill elements of right[] using same logic
    for i in range(n - 1, -1, -1):
        while (len(s) != 0 and arr[s[-1]] >= arr[i]):
            s.pop()
 
        if(len(s) != 0):
            right[i] = s[-1]
 
        s.append(i)
 
    # Create and initialize answer array
    ans = [0] * (n + 1)
    for i in range(n + 1):
        ans[i] = 0
 
    # Fill answer array by comparing minimums
    # of all. Lengths computed using left[]
    # and right[]
    for i in range(n):
         
        # Length of the interval
        Len = right[i] - left[i] - 1
 
        # arr[i] is a possible answer for this
        #  Length 'Len' interval, check if arr[i]
        # is more than max for 'Len'
        ans[Len] = max(ans[Len], arr[i])
 
    # Some entries in ans[] may not be filled
    # yet. Fill them by taking values from
    # right side of ans[]
    for i in range(n - 1, 0, -1):
        ans[i] = max(ans[i], ans[i + 1])
 
    # Print the result
    for i in range(1, n + 1):
        print(ans[i], end = " ")
 
# Driver Code
if __name__ == '__main__':
 
    arr = [10, 20, 30, 50, 10, 70, 30]
    n = len(arr)
    printMaxOfMin(arr, n)

# Output: 
# https://www.youtube.com/watch?v=MJzZgHFc00U
# 70 30 20 10 10 10 10
# Complexity Analysis:  

# Time Complexity: O(n). 
# Every sub-task in this approach takes Linear time.
# Auxiliary Space : O(n). 
# Use of stack for calculating next minimum and arrays to store the intermediate results.