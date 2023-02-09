'''
    Time Complexity: O(N + M)
    Space complexity: O(1)
  
    where N and M are lengths of string A and B respectively
'''
#  Iterative Approach

# First of all, we will delete the zeros from the end of both the strings.
#  For example: Convert 1.0.0 to 1, and  2.2.0 to 2.2 etc.
 
# Now, the idea is to use an iterative approach to compare both strings.
 
# We will use four-pointers start1,end1 (pointing to version A) and start2,end2 
# (pointing to version B) all initialized to 0. We will move end1 to the first dot
#  to the right of start1 ( or the end of the string if no such dot exists) and we 
#  will move end2 to the first dot to the right of start2 ( or the end of the string if no such dot exists) now If :

# end1 > end2
#     Version A is the latest
# end2 > end1 
#     Version B is the latest
# end2 = end1
#     In this case, we will compare both the strings from their respective start points 
#     and endpoints and output the result of the comparison. If both the strings are equal we will move 
#     start1 to end1 and start2 to end2 and will do the same process iteratively.

 

# If we reach the end of both the strings without terminating this means that both the 
# strings are equal and we will return 0 in this case.

# Function to remove zeros from end

def removeZerosFromEnd(a):
    
    # First initialising answer as complete string then removing zeros from end
    p = len(a) - 1

    # Traversing the string backwards
    for i in range(len(a) - 1, 0, -2):
        
        # Checking if the current character is 0 and there is dot to the left of it
        # If yes, then decreasing length of desired string
        if (a[i] == '0'  and a[i - 1] == '.'):
            p -= 2
            
        #Otherwise ending the loop
        else:
            break
            
    # Returning the final string
    return a[0 : p + 1]

def compareVersions(a, b):
    
    # Removing zeros from end of both strings
    a = removeZerosFromEnd(a)
    b = removeZerosFromEnd(b)
    
    # Initialising the four pointers
    start1 = 0
    start2 = 0
    end1 = 0
    end2 = 0
    
    # Traversing both strings
    while(True):
        
        # Finding first dot to the right of start1 in string a
        while (end1 < len(a) and a[end1] != '.'):
            end1 += 1
            
        # Finding first dot to the right of start2 in string b
        while (end2 < len(b) and b[end2] != '.'):
            end2 += 1
            
        # Finding the greater one among end1 and end2
        if (end1 > end2):
            return 1
        
        elif((end1 < end2)):
            return -1
        
        # Comparing both the strings character by character
        for i in range(start1, end1):
            if(a[i] > b[i]):      
                return 1
            
            elif(b[i] > a[i]):
                return -1
            
        # Check if we reached end of both strings
        if (end1 == len(a) and end2 == len(b)):
            return 0
        
        # Check if we reached end of string a
        if (end1 == len(a)):
            return -1
        
        # Check if we reached end of string b
        if (end2 == len(b)):
            return 1
        
        # Updating values of all the four pointers
        start1 = end1
        start2 = end2
        end1 += 1
        end2 += 1

        