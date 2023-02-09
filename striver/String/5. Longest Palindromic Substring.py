
# Dynamic Programming

# If the string length is less than or equal to 1 then return the string, as one length string is always palindromic.
# Initialize a ‘DP’ array of data type boolean, ‘DP’[i][j] will store false if STR[i, j] 
# is not palindromic otherwise it will store true.
# Store all the diagonal elements (DP[i][i]) as true, as STR[i, i] will always be palindromic.
# For substring of length 2, check if STR[i] is equal to STR[i + 1] then store DP[i][i + 1] as true.
# Run a loop for the length of a substring greater than 2, fill the DP array diagonally.
#     To calculate DP[i][j], check the value of DP[i + 1][j - 1], if the value is true and STR[i]
#  is same as STR[j], then we make DP[i][j] true otherwise false.
#     For every DP[i][j] true, update the length and starting index of the substring.
# Return the substring of the string having starting index as start and of maximum length.

# Time Complexity

# O(N ^ 2), where N is the length of the given string as 


# We are traversing the ‘DP’ array once.
# Space Complexity

# O(N ^ 2), where N is the length of the given string. 
# We are using a ‘DP’ array of N*N dimensions.

'''
    Time Complexity = O(N ^ 2)
    Space Complexity = O(N ^ 2)
    
    Where N is the length of the string.
'''

def longestPalinSubstring(str):
    n = len(str)

    if n < 1:
        return ""

    '''
        dp[i][j] will be true if str[i..j] is palindrome.
        Else dp[i][j] will be false.
    '''
    dp = [[False for j in range(n)] for i in range(n)]

    maxLength = 1

    # Single letter is always be palindromic.
    for i in range(n):
        dp[i][i] = True

    start = 0

    # Substring of length 2.
    for i in range(n - 1):
        if str[i] == str[i + 1]:
            dp[i][i + 1] = True

            if maxLength < 2:
                start = i
                maxLength = 2

    '''
        Check for lengths greater than 2.
        k is length of substring.
    '''
    for length in range(3,n + 1):

        # Fix the starting index.
        for i in range(n - length + 1):
            # Ending index of length 'length'.
            j = i + length - 1

            # Condition of str[i, j] to be palindromic.
            if (dp[i + 1][j - 1] is True and str[i] == str[j]):
                dp[i][j]= True

                # Update the starting index and the length.
                if (length > maxLength):
                    start = i
                    maxLength = length

    return str[start : start + maxLength]

##############################################################################################
# for without lowest start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, end = 0, 0
        for i in range(n, -1, -1): # from n to 0
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j] and (dp[i+1][j-1] or j-i==1):
                    if j - i > end - start:
                        end = j
                        start = i
                    dp[i][j] = True

        return s[start:end+1]


################################################################################################
# Expand Around centre
#  Expanding around the centres

# If the string length is less than or equal to 1 then return the string, as a single character is always palindromic.
# The idea is to generate all even length and odd length palindromes and keep track of the longest palindrome seen so far.  Run a loop where ‘i’ will be from 0 to ‘N’ - 1.
#     To generate odd length palindrome, fix center ‘i’, and expand in both directions for longer palindromes.
#  Odd length palindromes will have a character at the center.
#     Similarly, for even length palindrome, fix the center as ‘i’, ‘i’ + 1, and expand in both directions. 
# Even palindrome will have a partition between ith char and i+1th char as the center.
#     If the length of the current palindromic substring length is greater then update the starting length 
# of the string and length of the palindromic substring.
# Return the substring of the string having starting index as ‘START’ and of maximum length.

 

# For expanding :

#     For expanding around a center ‘i’ for odd length, initialize two variables ‘LEFT’ and ‘RIGHT’ to ‘i’ 
# and go until ‘LEFT and ’RIGHT' are in range and STR[LEFT] == STR[RIGHT]. Decrement the ‘LEFT’ and increment the ‘RIGHT’.
#     For expanding around a centre ‘i’ and ‘i’ + 1 for even length, initialise two variables ‘LEFT’ = ‘i’ 
# and ‘RIGHT’ = ‘i’ + 1, and go until ‘LEFT’ and ‘RIGHT’ are in range and STR[LEFT] == STR[RIGHT]. 
# Decrement the ‘LEFT’ and increment the ‘RIGHT’.
#     Return the length of the palindromic substring.

# Time Complexity

# O(N ^ 2), where N is the length of the given string.

# As we are expanding twice for every index and expanding could take O(N) in the worst case.
# Space Complexity

# O(1).
# center 2*n -1
'''
    Time Complexity : O(N ^ 2)
    Space Complexity: O(1)
    
    Where N is the length of the string.
'''

def expandAroundCenter(str, left, right):

    start = left
    end = right
    n = len(str)

    # Expand the center.
    while (start >= 0 and end < n and str[start] == str[end]):
        start -= 1
        end += 1

    return end - start - 1


def longestPalinSubstring(str):
    n = len(str)

    if n < 1:
        return ""

    start = 0
    end = 0
    for i in range(n):
        # Longest odd length palindrome with center points as i.
        len1 = expandAroundCenter(str, i, i)

        # Longest even length palindrome with center points as i and i + 1.
        len2 = expandAroundCenter(str, i, i+1)

        length = max(len1, len2)

        if (length > end - start + 1):
            start = i - (length - 1) // 2
            end = i + (length) // 2

    return str[start : end + 1]

###################################################################################################
# Leetcode
# Intuitively, we list all the substrings, pick those palindromic, and get the longest one. 
# this approach takes O(n^3) time complexity, where n is the length of s.

# Two Pointers:
# This approach takes O(n^2) time complexity, O(1) space complexity, where n is the length of s.

# For each character s[i], we get the first character to its right which isn't equal to s[i].
# Then s[i, right - 1] inclusive are equal characters e.g. "aaa".
# Then we make left = i - 1, while s[left] == s[right], s[left, right] inclusive is palindrome,
#  and we keep extending both ends by left -= 1, right += 1.
# Finally we update the tracked longest palindrome if needed.

# Incase of any doubts, feel free to ask in comments.
# Incase you like the solution, please upvote as it just feels nice.

# Note: There is another Dynamic programming approach to this same question.

class Solution:
    def longestPalindrome(self, s):
        answer = ""
        
        def helper(left, right):
            # get the longest palindrome, l, r are the middle indexes
            # from inner to outer
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1; right += 1
            return s[left+1:right]

        for index in range(len(s)):
            # odd case, like "aba"
            tmp = helper(index, index)
            if len(tmp) > len(answer):
                answer = tmp
            # even case, like "abba"
            tmp = helper(index, index+1)
            if len(tmp) > len(answer):
                answer = tmp
        return answer