# Input: strings: "XXXXZY", "XXY", "XXZ"
# Output: XXXXZY is interleaved of XXY and XXZ
# The string XXXXZY can be made by 
# interleaving XXY and XXZ
# String:    XXXXZY
# String 1:    XX Y
# String 2:  XX  Z

# Input: strings: "XXY", "YX", "X"
# Output: XXY is not interleaved of YX and X
# XXY cannot be formed by interleaving YX and X.
# The strings that can be formed are YXX and XYX

# requirements -> 
# len(str1) + len(str2) == len(str3)
# | len(str1) - len(str2) | = 1



def isInterleavedCommonChar(a , b , c):   # this approach doesnt handle common keys
    if not a and not b and not c:  # if all strings are empty then its true
        return True
    if not c:  # if only c is empty then false
        return False
    x = a and a[0] == c[0]  and isInterleavedCommonChar(a[1:] , b , c[1:])
    y = b and b[0] == c[0] and isInterleavedCommonChar(a , b[1:] , c[1:])
    return x or y


def isInterleavingMemo(X, Y, S, T):  # Time(O(m*n))
 
    # return true if the end of all strings is reached
    if not X and not Y and not S:
        return True
 
    # return false if the end of string 'S' is reached,
    # but 'X' or 'Y' is not empty
    if not S:
        return False
 
    # calculate a unique key by using delimiter `|`
    key = (X, Y, S)
 
    # if the subproblem is seen for the first time
    if key not in T:
 
        # if string 'X' is not empty and its first character matches with the
        # first character of 'S', recur for the remaining substring
        x = (len(X) and S[0] == X[0]) and isInterleavingMemo(X[1:], Y, S[1:], T)
 
        # if string 'Y' is not empty and its first character matches with the
        # first character of 'S', recur for the remaining substring
        y = (len(Y) and S[0] == Y[0]) and isInterleavingMemo(X, Y[1:], S[1:], T)
 
        T[key] = x or y
 
    return T[key]


def isInterleaveDP(A, B, C):
    if len(A) + len(B) != len(C):
        return 0
    f = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    f[0][0] = 1
    for i in range(len(A) + 1):
        for j in range(len(B) + 1):
            if i > 0 and A[i - 1] == C[i + j - 1]:
                f[i][j] = f[i][j] or f[i - 1][j]
            if j > 0 and B[j - 1] == C[i + j - 1]:
                f[i][j] = f[i][j] or f[i][j - 1]
    return f[-1][-1]


# A Dynamic Programming based python3 program
# to check whether a string C is an interleaving
# of two other strings A and B.

# The main function that returns true if C is
# an interleaving of A and B, otherwise false.
def isInterleaved(A, B, C):

	# Find lengths of the two strings
	M = len(A)
	N = len(B)

	# Let us create a 2D table to store solutions of
	# subproblems. C[i][j] will be true if C[0..i + j-1]
	# is an interleaving of A[0..i-1] and B[0..j-1].
	# Initialize all values as false.
	IL = [[False] * (N + 1) for i in range(M + 1)]

	# C can be an interleaving of A and B only of sum
	# of lengths of A & B is equal to length of C.
	if ((M + N) != len(C)):
		return False

	# Process all characters of A and B
	for i in range(0, M + 1):
		for j in range(0, N + 1):
			
			# two empty strings have an empty string
			# as interleaving
			if (i == 0 and j == 0):
				IL[i][j] = True

			# A is empty
			elif (i == 0):
				if (B[j - 1] == C[j - 1]):
					IL[i][j] = IL[i][j - 1]
			
			# B is empty
			elif (j == 0):
				if (A[i - 1] == C[i - 1]):
					IL[i][j] = IL[i - 1][j]
			
			# Current character of C matches with
			# current character of A, but doesn't match
			# with current character of B
			elif (A[i - 1] == C[i + j - 1] and
				B[j - 1] != C[i + j - 1]):
				IL[i][j] = IL[i - 1][j]

			# Current character of C matches with
			# current character of B, but doesn't match
			# with current character of A
			elif (A[i - 1] != C[i + j - 1] and
				B[j - 1] == C[i + j - 1]):
				IL[i][j] = IL[i][j - 1]

			# Current character of C matches with
			# that of both A and B
			elif (A[i - 1] == C[i + j - 1] and
				B[j - 1] == C[i + j - 1]):
				IL[i][j] = (IL[i - 1][j] or IL[i][j - 1])
		
	return IL[M][N]

# A function to run test cases
def test(A, B, C):

	if (isInterleaved(A, B, C)):
		print(C, "is interleaved of", A, "and", B)
	else:
		print(C, "is not interleaved of", A, "and", B)

# Driver Code
if __name__ == '__main__':
	test("XXY", "XXZ", "XXZXXXY")
	test("XY", "WZ", "WZXY")
	test("XY", "X", "XXY")
	test("YX", "X", "XXY")
	test("XXY", "XXZ", "XXXXZY")
	
# This code is contributed by ashutosh450




dic = {}
print(isInterleavingMemo(dic))


print(isInterleavedCommonChar("XXY", "XXZ" , "XXXXYZ"))


#time O(2^(M+N))