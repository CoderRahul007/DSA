def ninjaAndLadoos(A, B, m, n, K):
    # Write your code here.
        i, j, k = 0, 0, 0
    
        # Keep taking smaller of the current
        # elements of two sorted arrays and
        # keep incrementing k
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                k += 1
                if k == K:
                    return A[i]
                i += 1
            else:
                k += 1
                if k == K:
                    return B[j]    
                j += 1
    
        # If array B[] is completely traversed
        while i < len(A):
            k += 1
            if k == K:
                    return A[i]
            i += 1
    
    
        # If array A[] is completely traversed
        while j < len(B):
            k += 1
            if k == K:
                    return B[j]
            j += 1
# O(n)
################################################################################

# Divide and Conquer

# We can make our algorithm more efficient by using a divide and conquer approach.

# First we divide ‘K’ by 2 i.e. ‘K’ / 2 and this value will be pointing to the indices of both the ROW’s. 
# Now based on the comparison between both values we will call our recursive function.

 

# Here is the algorithm :

#     First we handle the base cases:
#         If any of these ‘ROWs’ is empty then we will return ‘K’th’ element of other ‘ROW’.
#         If  ‘K’ = 1 then return min( ROW1[0], ROW2[0] ).
#     Initialize a variable ‘i’ which will point to the index of ‘ROW1’ and ‘j’ will point to the index of ‘ROW2’.
#         ‘i’ = min( M, K / 2) , ‘j’ = min(N, K / 2)
#     Now compare the values at ROW1[i] and ROW2[j] and do the following:
#         If ROW1[i - 1] > ROW2[j - 1] that means our ‘K’th’ value is present in the right of the ROW2[j].
#          Now ‘K’ will become ‘K’ - ‘j’.
#             Return ninjaAndLadoos(ROW1, ROW2 + j, M, N - j,  K - j).
#         Else value will be present in the right of ‘ROW1[i]’. So, now ‘K’ will become ‘K’ - ‘j’.
#             Return ninjaAndLadoos(ROW1 + i, ROW2, M - i, N,  K).

# Time Complexity

# O(log(K))  where ‘K’ is the ‘K'th’ person which is given in the input of every test case.

 

# In each recursive call, we check only the  ‘K’ / 2 elements of both arrays and in the subsequent calls, 
# we are reducing the sizes of both arrays by ‘K’/2. Hence, the overall time complexity is O(log(K)).
# Space Complexity

# O(log(K))  where ‘K’ is the K'th person which is given in the input of every test case.

 

# The maximum depth of the recursion stack space can be log(K). Hence, space complexity is O(log(K)).

"""
    Time complexity: O(log(K))
    Space complexity: O(log(K))

    where K denotes the Kth person in line waiting to be served.
"""


def ninjaAndLadoos(row1, row2, m, n, k):
    
    # If length of first array is smaller then length of second then swap both the arrays.
    if m > n:
        return ninjaAndLadoos(row2, row1, n, m, k)

    if m == 0:
        return row2[k - 1]

    # If k is equal to 1
    if k == 1:
        return min(row1[0], row2[0])

    i = min(m, k // 2)
    j = min(n, k // 2)

    # If row1[i - 1] is greater than row2[j - 1]
    if row1[i - 1] > row2[j - 1]:

        newRow2 = row2[j:]
        return ninjaAndLadoos(row1, newRow2, m, n - j, k - j)

    newRow1 = row1[i:]
    return ninjaAndLadoos(newRow1, row2, m - i, n, k - i)
    
