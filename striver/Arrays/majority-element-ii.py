# Problem Statement
# You are given an array/list 'ARR' of integers of length ‘N’. You are supposed 
# to find all the elements that occur strictly more than floor(N/3) times in the given array/list.
# Input Format :

# The first line contains a single integer ‘T’ denoting the number of test cases. The test cases follow.

# The first line of each test case contains a single integer ‘N’ denoting the number of elements in the array.

# The second line contains ‘N’ single space-separated integers denoting the elements of the array/list.

# Output Format :

# For each test case, return all the majority elements separated by a single space.

# The output of every test case will be printed in a separate line.

# You may return the majority of elements in any order.



################################################################################################################################
#  Moore's Voting Algorithm Approach
# The idea is to use a modification of Moore's voting algorithm to find candidate
#  elements that may occur more than N/3 times in the given array. We will use the 
# fact that if we remove 3 distinct elements from the array, the elements which 
# occurred more than N/3 times do not change.

 

# The steps are as follows:

# We can prove using the pigeonhole principle that there are at most 2 elements 
# possible that can occur more than N/3 times, we will use the variable ‘FIRST_CANDIDATE’
#  to store the first element that can possibly occur more than ‘N’/3 times and another 
# variable ‘SECOND_CANDIDATE’ to store the second element that can possibly occur more 
# than N/3 times. Also, we will use the variables ‘FIRST_COUNT’ and ‘SECOND_COUNT’, 
# both of which will be initialized to 0, to store the frequency of the ‘FIRST_CANDIDATE’ 
# and ‘SECOND_COUNT’ respectively.
# Iterate through the array, let’s say our current element is ‘ARR[i]’.
#     If ‘ARR[i]’ is equal to ‘FIRST_CANDIDATE’ then increment ‘FIRST_COUNT’ by 1
#     If ‘ARR[i]’ is equal to ‘SECOND_CANDIDATE’ then increment ‘SECOND_COUNT’ by 1.
#     Otherwise, if ‘FIRST_COUNT’ is equal to 0, set ‘FIRST_CANDIDATE’ equal to ‘ARR[i]’ 
# and increment ‘FIRST_COUNT’ by 1.
#     Else if ‘SECOND_COUNT’ is equal to 0, set ‘SECOND_CANDIDATE’ equal to ‘ARR[i]’ and 
# increment ‘SECOND_COUNT’ by 1.
#     Else decrement both ‘FIRST_COUNT’ and ‘SECOND_COUNT’ by 1. By doing this, we are basically 
# removing 3 distinct elements from our array which will not affect the answer.
# Iterate through the array once again and count the number of occurrences of ‘FIRST_CANDIDATE’
#  and ‘SECOND_CANDIDATE’.
# Store ‘FIRST_CANDIDATE’ in the answer if it occurs more than ‘N’/3 times in the given array/list,
#  similarly add ‘SECOND_CANDIDATE’ to the answer if it occurs more than ‘N’/3 times in the given array/list.
# Return the stored elements.

# Time Complexity

# O(N), where ‘N’ is the number of elements in the given array/list.


# We are iterating through the array twice, which takes O(N) time. Thus, the overall time complexity will be O(N).
# Space Complexity

# O(1).

# We are not using any extra space. Thus, the space complexity will be O(1).
'''
    Time Complexity: O(N)
    Space Complexity: O(1)

    Where 'N' is the number of elements in the given array/list.
'''

def majorityElementII(arr):

    n = len(arr)

    # Array for storing final answer.
    majorityElement = []

    # Variables for storing the elements which may occur more than n/3 times.
    firstCandidate = 0
    secondCandidate = 0

    # Variables for storing the frequency of the candidate elements.
    firstCount = 0
    secondCount = 0

    # Iterate through the array.
    for i in range(n):

        # Increment firstCount if the current element is equal to firstCandidate.
        if (arr[i] == firstCandidate):
            firstCount = firstCount + 1

        # Increment secondCount if the current element is equal to secondCandidate.
        elif (arr[i] == secondCandidate):
            secondCount = secondCount + 1

        # Change value of the firstCandidate to the current element if firstCount is equal to 0.
        elif (firstCount == 0):
            firstCandidate = arr[i]
            firstCount = 1

        # Change value of the secondCandidate to the current element if secondCount is equal to 0.
        elif (secondCount == 0):
            secondCandidate = arr[i]
            secondCount = 1

        # Otherwise decrement firstCount and secondCount by 1.
        else:
            firstCount = firstCount - 1
            secondCount = secondCount - 1

    firstCount = 0
    secondCount = 0

    # Iterate through the array to find frequency of firstCandidate and secondCandidate.
    for i in range(n):

        # Increment firstCount if the current element is equal to firstCandidate.
        if (arr[i] == firstCandidate):
            firstCount = firstCount + 1

        # Increment secondCount if the current element is equal to secondCandidate.
        elif(arr[i] == secondCandidate):
            secondCount = secondCount + 1

    # Include firstCandidate in the answer if its frequency is more than n/3.
    if (firstCount > n / 3):
        majorityElement.append(firstCandidate)

    # Include secondCandidate in the answer if its frequency is more than n/3.
    if (secondCount > n / 3):
        majorityElement.append(secondCandidate)

    # Return all stored majority elements.
    return majorityElement