# Problem Statement
# You have been given an array/list 'ARR' consisting of 'N' integers. 
# Your task is to find the majority element in the array. If there is no majority element present, print -1.
# Note:

# A majority element is an element that occurs more than floor('N' / 2) times in the array.

# Input Format:

# The first line of input contains an integer 'T' representing the number of test cases.

# The first line of each test case contains a single positive integer ‘N’ representing the size of the array/list.

# The second line of each test case contains ‘N’ single space-separated integers representing
#  the array elements of 'ARR'.

# Output Format :

# For each test case, print an integer denoting the majority element present in the array.
#  Print-1 in case of no majority element.

def findMajorityElement(arr, n):
	# Write your code here.
    mp = {}
    for i in arr:
        if i not in  mp:
            mp[i] = 1
        else:
            mp[i] += 1
    for k , v in mp.items():
        if v > n//2:
            return k
    return -1

#############################################################################################################3

#  Boyer-Moore majority vote algorithm

# We can find the majority element in linear time and constant space
#  using Moore’s voting algorithm. It is based on the fact that since the 
# majority element occurs more than floor('N' / 2) times, its frequency will
#  be greater than the combined frequencies of all other elements. 

 

# The algorithm gives the correct answer only if the majority element exists 
# in the array. So, in the end, we have to check the frequency of the majority element to confirm.

 

# The steps are as follows:
 
# We will maintain ‘majorityElement’ to keep track of the possible candidate of the majority element.
# We will initialize ‘count’ to 0 to store the count of ‘majorityElement'.
# Loop through array elements.
#     If ‘count’ is 0:
#         We set ‘majorityElement’ to the current element, set ‘count’ to 1, and continue iterating.
#     Else:
#         If the current element is equal to the ‘majorityElement’, we increment the ‘count’ by 1.
#         Else, we decrement the ‘count’ by 1.
# Now, we again traverse through the array and find the count of ‘majorityElement’.
# If the count is greater than floor('N' / 2), we return ‘majorityElement’ as the answer. Else, we return -1.

# Time Complexity

# O(N), where ‘N’ denotes the size of the given array/list. Hence, the time complexity is linear.
 
# Since we are traversing the array exactly two times in O(2 * N) time. Thus the overall time complexity is O(N).
# Space Complexity

# O(1)
 
# Since constant space is used, space complexity will be O(1).

'''
    Time Complexity: O(N)
    Space Complexity: O(1)

    Where 'N' is the size of array/list.
'''

def findMajorityElement(arr, n):
	# Variable to store the majority element in the array, it it is present.
	majorityElement = -1
	count = 0

	# Iterating the array to know if there is a possible majority element present.
	for i in range(n):
		# If count becomes 0, set current element as a possible candidate for majority element, reset count to 1.
		if count == 0:
			majorityElement = arr[i]
			count = 1
			
			continue

		# Increment the count if the current element of the array is equal to the current majority element, else decrement it.
		if arr[i] == majorityElement:
			count += 1
		else:
			count -= 1

	count = 0

	# Checking if majority element occurs more than 'n' / 2 times.
	for i in range(n):
		if arr[i] == majorityElement:
			count += 1

	# If the count of the majority element is greater than 'n' / 2, then return it.
	if count > n / 2:
		return majorityElement

	# If no majority element found, return -1.
	return -1
