# Problem Statement
# You are given an unsorted array/list 'ARR' of 'N' integers. Your task is to return the length of the longest
#  consecutive sequence.
# The consecutive sequence is in the form ['NUM', 'NUM' + 1, 'NUM' + 2, ..., 'NUM' + L] where 'NUM' is 
# the starting integer of the sequence and 'L' + 1 is the length of the sequence.
# Note:

# If there are any duplicates in the given array we will count only one of them in the consecutive sequence.

# For example-

# For the given 'ARR' [9,5,4,9,10,10,6].

# Output = 3
# The longest consecutive sequence is [4,5,6].

def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here.
    arr.sort()
    c = 0
    m = 0
    for i in range(n-1):
        if arr[i] + 1 == arr[i+1]:
            c+= 1
            m = max(c , m)
        elif arr[i+1] == arr[i]:
            continue
        else:
            c = 0
    return m+1

##############################################################################################################

#  Using Hash Table

# We can improve our time complexity of searching the next consecutive element in
#  the array by using a Hash Table which can check the presence of an element in O(1).  
# The steps are as follows:
 
# Store all the elements in the Hash table first.
# For every element check, if it is a starting element of sequence or not. by simply 
# checking if ‘ARR[i]’ - 1 is present in a hashtable or not. If it is present so it
#  means ‘ARR[i]’ can’t be the first element of the sequence.
# If the element is the first element then count the total number of elements that 
# can occur in sequence by incrementing the element by 1 in each iteration of the while loop.
# If the count is more than the longest consecutive sequence then we update it.

# Time Complexity

# O(N), where ‘N’ is the size of an array.

 

# A solution seems to be quadratic as while loop is in for loop but if we look closer
#  then in the worst case, while loop will only iterate if the current element is the 
# first of sequence and so the while loop will only take O(N) throughout the whole 
# algorithm and nested loop actually run in O(N+N)  i.e O(N). Hence the total time complexity is O(N).
# Space Complexity

# O(N), where ‘N’ is the size of the array.

 
'''  
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the length of the given array.
'''

def lengthOfLongestConsecutiveSequence(arr, n):
    # To store length of longest consecutive sequence.
    mx = 0            
    # To store all the unique elements of array.
    sett = set()
    
    for element in arr:
        sett.add(element)
        
    for element in arr:
        
        previousConsecutiveElement = element-1
        
        if(not previousConsecutiveElement in sett):
            
            # Element is the first value of consecutive sequence.
            j = element
            len = 1
            
            while j + 1 in sett:
                
                # The next consecutive element by will be j + 1.
                j += 1
                len +=1
            
            # Update maximum length of consecutive subsequence.
            mx = max(mx , len)
     
    return mx if mx > 0 else 1