 
# Method 2: The second method uses the process of Hashing to arrive at the result and is
#  solved at a lesser time of O(n2). 



# Approach: This involves traversing through the array. For every element arr[i], 
# find a pair with sum "-arr[i]". This problem reduces to pair sum and can be solved in O(n) time using hashing.



# Algorithm: 

# Create a hashmap to store a key-value pair.
# Run a nested loop with two loops, the outer loop from 0 to n-2 and the inner loop from i+1 to n-1
# Check if the sum of ith and jth element multiplied with -1 is present in the hashmap or not
# If the element is present in the hashmap, print the triplet else insert the j'th element in the hashmap.


def findTriplets(arr , n):
    res = 0    
    for i in range(n-1):
        s = set()
        for j in range(i+1 , n):            
            x = -(arr[i] + arr[j])
            if x in s:
                print(x, arr[i], arr[j])
                res+=1                
            else:
                s.add(arr[j])
    return res

# Sort the array in ascending order.
# Traverse the array from start to end.
# For every index i, create two variables l = i + 1 and r = n - 1
# Run a loop until l is less than r if the sum of array[i], array[l] and array[r] is 
# equal to zero then print the triplet and break the loop
# If the sum is less than zero then increment the value of l, 
# by increasing the value of l the sum will increase as the array is sorted, so array[l+1] > array [l]
# If the sum is greater than zero then decrement the value of r, 
# by decreasing the value of r the sum will decrease as the array is sorted, so array[r-1] < array [r].

def findTripletsOptimised(arr , n):
    arr.sort()
    res = 0

    for i in range(n-1):
    
        # initialize left and right
        l = i + 1
        r = n - 1
        x = arr[i]
        while (l < r):
        
            if (x + arr[l] + arr[r] == 0):
                # print elements if it's sum is zero
                print(x, arr[l], arr[r])
                l+=1
                r-=1
                res+=1
            

            # If sum of three elements is less
            # than zero then increment in left
            elif (x + arr[l] + arr[r] < 0):
                l+=1

            # if sum is greater than zero then
            # decrement in right side
            else:
                r-=1
        
    return res

n = 5
arr = [0, -1, 2, -3, 1]
print(findTriplets(arr , n))
print(findTripletsOptimised(arr , n))
