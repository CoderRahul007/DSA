class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        i = 0
        ln = len(needle)
        lh = len(haystack)
        while i < lh-ln+1:
            if haystack[i : i + ln] == needle:
                return i
            i +=1
        return -1