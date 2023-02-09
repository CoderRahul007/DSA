# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
#  which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of
# substrings such that each substring contains exactly one unique digit.
# Then for each substring, say the number of digits, then say the digit.
#  Finally, concatenate every said digit.

# For example, the saying and conversion for digit string "3322251":

# Given a positive integer n, return the nth term of the count-and-say sequence.

# Example 1:

# Input: n = 1
# Output: "1"
# Explanation: This is the base case.
# Example 2:

# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"

        prev = self.countAndSay(n-1)
        prev_digit = prev[0]
        ans = ""
        count = 0

        for digit in prev:
            if digit == prev_digit:
                count += 1
            else:
                ans += str(count) + prev_digit
                prev_digit = digit
                count = 1

        ans += str(count) + prev_digit

        return ans

################################################
# easy approach

class Solution:
    def countAndSay(self, n: int) -> str:
        # n = 1: return 1 is the base case
        # n = 2: return count of last entry i.e. 1 1
        # n = 3: return count of last entry i.e. two 1's so 21
        # n = 4: we have one 2 and one 1 so 1211
        # n = 5: , we have one 1 and one 2 and two 1's so -> 111221
        # n = 6: we have three 1's, two 2's and one 1 so -> 312211
        # n = 7: we have one 3, one 1, two 2's and two 1's -> 13112221
        # ...
        # n = i: return counts in front of the number for entry of i-1 case
        prev = ""
        cur = "1"

        for i in range(n-1):
            prev = cur
            cur = ""
            cnt = 1
            for s in range(len(prev)):
                if s+1 < len(prev) and prev[s] == prev[s+1]:
                    cnt += 1
                else:
                    cur = cur+str(cnt)+str(prev[s])
                    cnt = 1

        return cur
