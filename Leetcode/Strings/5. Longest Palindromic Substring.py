class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s):
            return s
        max_length = 1
        start = 0
        for i in range(1, len(s)):
            one_more_letter_word = s[i-max_length:i+1]
            two_more_letter_word = s[i-max_length-1:i+1]

            if self.isPalindrome(two_more_letter_word) and i-max_length-1 >= 0:
                start = i - max_length - 1
                max_length += 2
            elif self.isPalindrome(one_more_letter_word):
                start = i - max_length
                max_length += 1
        return s[start:start+max_length]


#######################################################################################################
# DP Solution

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # create a table to keep track of substrings for dynamic prog
        table = [[False] * n for i in range(n)]
        for i in range(n):
            # the substring with the same character is always equal
            table[i][i] = True

        # setting the longest substring to last found single char string since it's the longest substring found so far
        longest_substr = s[i]

        for start in range(n-1, -1, -1):
            for end in range(start + 1, n):
                if s[start] == s[end]:  # see if characters match

                    # if (a. the substring is only two chars long, then we skip the check for
                    # inner palindromic substring or b. the substring is longer than two chars and the inner
                    # substring is palandromic(which means True in the table))
                    if end - start == 1 or table[start+1][end-1]:
                        # the current substring is palandromic(equivalent to True in the table)
                        table[start][end] = True
                        # if the current substring is not longer than the previous longest substring
                        if len(longest_substr) < end - start + 1:
                            # set the longest substring as the current substring
                            longest_substr = s[start: end + 1]
        return longest_substr
