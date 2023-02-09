# boundary case
# if m == 0 then len(s2)
# if n == 0 then len(s1)
# operarion can be insert / delete / replace

# What are the subproblems in this case?
# The idea is to process all characters one by one starting from either from left or right sides of both strings.
# Let us traverse from right corner, there are two possibilities for every pair of character being traversed.

# m: Length of str1 (first string)
# n: Length of str2 (second string)

#     If last characters of two strings are same, nothing much to do. Ignore last characters and get count for remaining strings. So we recur for lengths m-1 and n-1.
#     Else (If last characters are not same), we consider all operations on ‘str1’, consider all three operations on last character of first string, recursively compute minimum cost for all three operations and take minimum of three values.
#         Insert: Recur for m and n-1
#         Remove: Recur for m-1 and n
#         Replace: Recur for m-1 and n-1


def editDistanceRecur(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.
    if str1[m-1] == str2[n-1]:
        return editDistanceRecur(str1, str2, m-1, n-1)

    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    return 1 + min(editDistanceRecur(str1, str2, m, n-1),    # Insert
                   editDistanceRecur(str1, str2, m-1, n),    # Remove
                   editDistanceRecur(str1, str2, m-1, n-1)    # Replace
                   )


str1 = "sunday"
str2 = "saturday"
print(editDistanceRecur(str1, str2, len(str1), len(str2)))
# The time complexity of above solution is exponential.
# In worst case, we may end up doing O(3^m) operations.
#  The worst case happens when none of characters of two strings match.
#   Below is a recursive call diagram for worst case.


def minDisMemo(s1, s2, n, m, dp):

  # If any string is empty,
  # return the remaining characters of other string
  if(n == 0):
      return m
  if(m == 0):
      return n

  # To check if the recursive tree
  # for given n & m has already been executed
  if(dp[n][m] != -1):
      return dp[n][m]

  # If characters are equal, execute
  # recursive function for n-1, m-1
  if(s1[n - 1] == s2[m - 1]):
    if(dp[n - 1][m - 1] == -1):
        dp[n][m] = minDisMemo(s1, s2, n - 1, m - 1, dp)
        return dp[n][m]
    else:
        dp[n][m] = dp[n - 1][m - 1]
        return dp[n][m]

  # If characters are nt equal, we need to
  # find the minimum cost out of all 3 operations.
  else:
    if(dp[n - 1][m] != -1):
      m1 = dp[n - 1][m]
    else:
      m1 = minDisMemo(s1, s2, n - 1, m, dp)

    if(dp[n][m - 1] != -1):
      m2 = dp[n][m - 1]
    else:
      m2 = minDisMemo(s1, s2, n, m - 1, dp)
    if(dp[n - 1][m - 1] != -1):
      m3 = dp[n - 1][m - 1]
    else:
      m3 = minDisMemo(s1, s2, n - 1, m - 1, dp)

    dp[n][m] = 1 + min(m1, min(m2, m3))
    return dp[n][m]


    # Driver code
str1 = "voldemort"
str2 = "dumbledore"

n = len(str1)
m = len(str2)
dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]

print(minDisMemo(str1, str2, n, m, dp))


def editDistDP(str1, str2, m, n):
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j    # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i    # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])    # Replace

    return dp[m][n]


# Driver code
str1 = "sunday"
str2 = "saturday"

print(editDistDP(str1, str2, len(str1), len(str2)))

# Time Complexity: O(m x n)
# Auxiliary Space: O(m x n)

# Space Optimized Solution-----------------------------------------------------------------

# A Space efficient Dynamic Programming
# based Python3 program to find minimum
# number operations to convert str1 to str2


def EditDistDP(str1, str2):

        len1 = len(str1)
        len2 = len(str2)

        # Create a DP array to memoize result
        # of previous computations
        DP = [[0 for i in range(len1 + 1)] for j in range(2)]

        # Base condition when second String
        # is empty then we remove all characters
        for i in range(0, len1 + 1):
            DP[0][i] = i
        print("Base condition ", DP)

        # Start filling the DP
        # This loop run for every
        # character in second String
        for i in range(1, len2 + 1):
		
            # This loop compares the char from
            # second String with first String
            # characters
            for j in range(0, len1 + 1):

                # If first String is empty then
                # we have to perform add character
                # operation to get second String
                if (j == 0):
                    DP[i % 2][j] = i

                # If character from both String
                # is same then we do not perform any
                # operation . here i % 2 is for bound
                # the row number.
                elif(str1[j - 1] == str2[i-1]):
                    DP[i % 2][j] = DP[(i - 1) % 2][j - 1]
                
                # If character from both String is
                # not same then we take the minimum
                # from three specified operation
                else:
                    DP[i % 2][j] = (1 + min(DP[(i - 1) % 2][j],
                                        min(DP[i % 2][j - 1],
                                    DP[(i - 1) % 2][j - 1])))
                
        # After complete fill the DP array
        # if the len2 is even then we end
        # up in the 0th row else we end up
        # in the 1th row so we take len2 % 2
        # to get row
        print(DP[len2 % 2][len1], "")

	
str1 = "food"
str2 = "money"

EditDistDP(str1, str2)


