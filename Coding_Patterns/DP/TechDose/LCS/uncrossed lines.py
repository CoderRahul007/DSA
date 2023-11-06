# Given two arrays A[] and B[], the task is to find the maximum number of uncrossed lines
#  between the elements of the two given arrays.
#  A straight line can be drawn between two array elements A[i] and B[j] only if:

# A[i] = B[j]
# The line does not intersect any other line.

# Input: A[] = {3, 9, 2}, B[] = {3, 2, 9}
# Output: 2
# Explanation:
# The lines between A[0] to B[0] and A[1] to B[2] does not intersect each other.

# Input: A[] = {1, 2, 3, 4, 5}, B[] = {1, 2, 3, 4, 5}
# Output: 5

# Python3 program for
# the above approach

# Function to count maximum number
# of uncrossed lines between the
# two given arrays
def uncrossedLines(a, b,
                   n, m):

    # Stores the length of lcs
    # obtained upto every index
    dp = [[0 for x in range(m + 1)]
          for y in range(n + 1)]

    # Iterate over first array
    for i in range(n + 1):

        # Iterate over second array
        for j in range(m + 1):

            if (i == 0 or j == 0):

                # Update value in dp table
                dp[i][j] = 0

            # If both characters
            # are equal
            elif (a[i - 1] == b[j - 1]):

                # Update the length of lcs
                dp[i][j] = 1 + dp[i - 1][j - 1]

            # If both characters
            # are not equal
            else:

                # Update the table
                dp[i][j] = max(dp[i - 1][j],
                               dp[i][j - 1])

    # Return the answer
    return dp[n][m]


# Driver Code
if __name__ == "__main__":

    # Given array A[] and B[]
    # A = [3, 9, 2]
    # B = [3, 2, 9]

    A = [1, 2, 3, 4, 5]
    B = [1, 2, 3, 4, 5]
    N = len(A)
    M = len(B)

    # Function Call
    print(uncrossedLines(A, B, N, M))

# This code is contributed by Chitranayal

# A = [1 ,2 , 3 , 4 , 5]
# B = [1 , 2 , 3 , 4  ,5]
# print(lcsDp(A , B))
