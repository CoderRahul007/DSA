# Approach: This is a two-step process. 
#     The first step gives the element that maybe the majority element in the array. If there is a majority element in an array, then this step will definitely return majority element, otherwise, it will return candidate for majority element.
#     Check if the element obtained from the above step is majority element. This step is necessary as there might be no majority element.
        
# Algorithm: 
#     Loop through each element and maintains a count of majority element, and a majority index, maj_index
#     If the next element is same then increment the count if the next element is not same then decrement the count.
#     if the count reaches 0 then changes the maj_index to the current element and set the count again to 1.
#     Now again traverse through the array and find the count of majority element found.
#     If the count is greater than half the size of the array, print the element
#     Else print that there is no majority element

# Program for finding out majority element in an array

# Function to find the candidate for Majority

# Write a function which takes an array and prints the majority element (if it exists),
#  otherwise prints “No Majority Element”. A majority element in an array A[] of size n is
#  an element that appears more than n/2 times (and hence there is at most one such element). 

# Examples : 

# Input : {3, 3, 4, 2, 4, 4, 2, 4, 4}
# Output : 4
# Explanation: The frequency of 4 is 5 which is greater
# than the half of the size of the array size. 

# Input : {3, 3, 4, 2, 4, 4, 2, 4}
# Output : No Majority Element
# Explanation: There is no element whose frequency is
# greater than the half of the size of the array size.

# https://www.youtube.com/watch?v=n5QY3x_GNDg

def findCandidate(A):
	maj_index = 0
	count = 1
	for i in range(len(A)):
		if A[maj_index] == A[i]:
			count += 1
		else:
			count -= 1
		if count <= 0:
			maj_index = i
			count = 1
	return A[maj_index]

# Function to check if the candidate occurs more than n/2 times


def isMajority(A, cand):
	count = 0
	for i in range(len(A)):
		if A[i] == cand:
			count += 1
	if count > len(A)/2:
		return True
	else:
		return False

# Function to print Majority Element


def printMajority(A):
	# Find the candidate for Majority
    cand = findCandidate(A)
    print("cand" , cand)

    # Print the candidate if it is Majority
    if isMajority(A, cand) == True:
        print(cand)
    else:
        print("No Majority Element")


# Driver code
A = [1, 3, 3, 1, 2]

# Function call
printMajority(A)
