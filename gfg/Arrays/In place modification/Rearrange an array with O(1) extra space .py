# Given an array arr[] of size N where every element is in the range from 0 to n-1.
#  Rearrange the given array so that arr[i] becomes arr[arr[i]]

# Example 1:

# Input:
# N = 2
# arr[] = {1,0}
# Output: 0 1
# Explanation: 
# arr[arr[0]] = arr[1] = 0.
# arr[arr[1]] = arr[0] = 1.

 

# Example 2:

# Input:
# N = 5
# arr[] = {4,0,2,1,3}
# Output: 3 4 2 0 1
# Explanation: 
# arr[arr[0]] = arr[4] = 3.
# arr[arr[1]] = arr[0] = 4.
# and so on.

def arrange( arr, n): 
    #Your code here
    for i in range(n):
        x = arr[i]
        y = arr[x]
        arr[i] = x + (y % n) *n

    print(arr)
    for i in range(n):
        arr[i]//=n
    print(arr)

arr = [4,0,2,1,3]
n = 5
# arr = [1 , 0]
# n 
arrange(arr , n)

def rearrange(arr, n):
 
    # First step: Increase all values
    # by (arr[arr[i]] % n) * n
    for i in range(0, n):
        arr[i] += (arr[arr[i]] % n) * n
 
    # Second Step: Divide all values
    # by n
    for i in range(0, n):
        arr[i] = int(arr[i] // n)



# Approach: The array elements of the given array lies from 0 to n-1.
#  Now an array element is needed that can store two different values at the same time. To achieve this, 
# every element at ith index is incremented by (arr[arr[i]] % n)*n.After the increment operation of first step,
#  every element holds both old values and new values. Old value can be obtained by arr[i]%n and a new value can be obtained by arr[i]/n.

# How this can be achieved? 
# Let’s assume an element is a and another element is b, both the elements are less than n. 
# So if an element a is incremented by b*n. 
# So the element becomes a + b*n so when a + b*n is divided by n then the value is b and a + b*n % n is a.

# Algorithm:  

# Traverse the array from start to end.
# For every index increment the element by array[array[index] ] % n. To get the ith element find the modulo with n, i.e array[index]%n.
# Again Traverse the array from start to end
# Print the ith element after dividing the ith element by n, i.e. array[i]/n.