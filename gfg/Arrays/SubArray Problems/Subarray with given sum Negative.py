# Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
# Output: Sum found between indexes 2 and 4
# Explanation: Sum of elements between indices
# 2 and 4 is 20 + 3 + 10 = 33

# Input: arr[] = {10, 2, -2, -20, 10}, sum = -10
# Output: Sum found between indexes 0 to 3
# Explanation: Sum of elements between indices
# 0 and 3 is 10 + 2 - 2 - 20 = -10

# Input: arr[] = {-10, 0, 2, -2, -20, 10}, sum = 20
# Output: No subarray with given sum exists
# Explanation: There is no subarray with the given sum

# Python3 program to print subarray with sum as given sum 

# Function to print subarray with sum as given sum 
def subArraySum(arr, n, Sum): 
    curr_sum = 0
    Map = {}
    for i in range(len(arr)):
        curr_sum += arr[i]

        if curr_sum == Sum:
            print("Sum Found from index 0 to " , i)
            break
        if (curr_sum - Sum ) in Map :
            print("Sum found from ", Map[curr_sum-Sum] , "to ", i)
            break
        Map[curr_sum] = i

# Driver program to test above function 
if __name__ == "__main__": 

	arr = [10, 2, -2, -20, 10] 
	n = len(arr) 
	Sum = -10

	subArraySum(arr, n, Sum) 

# This code is contributed by Rituraj Jain
