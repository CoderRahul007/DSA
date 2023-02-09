# Given a string s and an integer k, return the length of the longest substring
# of s such that the frequency of each character in this substring is greater than or equal to k.


# Example 1:

# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
# Example 2:

# Input: s = "ababbc", k = 2
# Output: 5
# Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/solutions/882149/longest-substring-with-at-least-k-repeating-characters/


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_unique = len(collections.Counter(s))
        maxSubstring = 0

        for i in range(1, max_unique+1):
            counter = collections.Counter()
            left = 0
            for right in range(len(s)):
                while len(counter) > i:
                    counter[s[left]] -= 1
                    if not counter[s[left]]:
                        del counter[s[left]]
                    left += 1
                counter[s[right]] += 1
                if min(counter.values()) >= k:
                    maxSubstring = max(maxSubstring, right-left+1)
        return maxSubstring


# 3

# TC - O(n)
# SC - O(1)
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0

        for ind in range(1, 1 + len(Counter(s))):
            left = 0
            cnt = 0
            counter = Counter()
            for right, c in enumerate(s):
                counter[c] += 1
                if counter[c] == k:
                    cnt += 1

                while len(counter) > ind:
                    cur = s[left]
                    left += 1
                    counter[cur] -= 1
                    if counter[cur] == k - 1:
                        cnt -= 1
                    if counter[cur] == 0:
                        counter.pop(cur)
                if len(counter) == ind and cnt == ind:
                    res = max(res, right - left + 1)
        return res
