# GIven two different arrays A and B of size N and M, 
# the task is to merge the two arrays which are unsorted into another array which is sorted.


# Example 1:

# Input: N = 3, M = 3
# A[] = {10, 5, 15}
# B[] = {20, 3, 2}
# Output: 2 3 5 10 15 20
# Explanation: After merging both the 
# array's and sorting it with get the 
# desired output.  


# Example 2:

# Input: N = 4, M = 3
# A[] = {1, 10, 5, 15}
# B[] = {20, 0, 2}
# Output: 0 1 2 5 10 15 20



class Solution:
    def sortedMerge(self, a, b, c, n, m):
        # Your code goes here
        a.sort()
        b.sort()
        
        i = 0
        j = 0
        k = 0
        while i< n and j< m:
            if a[i] < b[j]:
                c[k] = a[i]
                k+=1
                i+=1
            elif a[i]>b[j]:
                c[k] = b[j]
                k+=1
                j+=1
            else:
                c[k] = a[i]
                k+=1
                c[k] =b[j]
                k+=1
                i+=1
                j+=1
        while i < n:
            c[k]=a[i]
            k+=1
            i+=1
        while j < m:
            c[k] = b[j]
            k+=1
            j+=1