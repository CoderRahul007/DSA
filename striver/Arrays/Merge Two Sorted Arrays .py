# Problem Statement
# Ninja has been given two sorted integer arrays/lists ‘ARR1’ and ‘ARR2’ of size ‘M’ and ‘N’.
#  Ninja has to merge these sorted arrays/lists into ‘ARR1’ as one sorted array. You may have 
#  to assume that ‘ARR1’ has a size equal to ‘M’ + ‘N’ such that ‘ARR1’ has enough space to add all the elements of ‘ARR2’ in ‘ARR1’.
# For example:

# ‘ARR1’ = [3 6 9 0 0]
# ‘ARR2’ = [4 10]
# After merging the ‘ARR1’ and ‘ARR2’ in ‘ARR1’. 
# ‘ARR1’ = [3 4 6 9 10]

# Input Format

# The first line of input contains an integer ‘T’ which denotes the number of test cases or queries to be run. Then the test cases follow.

# The first line of each test case contains two space-separated integers ‘M’ and ‘N’, which represent the size of ‘ARR1’ and ‘ARR2’.

# The next lines of each test case contain ‘M’ space-separated integers and ‘N’ zeros (i.e. 0) which represent the number of elements in ‘ARR1’.

# The next lines of each test case contain ‘N’ space-separated integers which represent the number of elements in ‘ARR2’.

# TLE
def ninjaAndSortedArrays(arr1,arr2,m,n):
    # Write your code here.
    i = 0
    j = 0
    while i < m :
        if arr1[i] <= arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            arr1[i] , arr2[j] = arr2[j] , arr1[i]
            k = j
            while k + 1 < n and arr2[k] > arr2[k+1]:
                arr2[k] , arr2[k+1] = arr2[k+1] , arr2[k]
                k+=1
            i+=1
    while j < n:
        arr1[i] = arr2[j]
        i+=1
        j+=1
    return arr1

#########################################################################################################

def ninjaAndSortedArrays(arr1,arr2,m,n):
        i = m-1
        j = n-1
        index = m+n-1
        # start filling from back of array since arr1 has enough space 
        while(i>=0  and j>=0):
            if(arr1[i]<arr2[j]):
                arr1[index] = arr2[j]
                j-=1
            else:
                arr1[index] = arr1[i]
                i-=1
            
            index-=1
        
        while(j>=0):
            arr1[index] = arr2[j]
            j-=1
            index-=1
        
        return arr1