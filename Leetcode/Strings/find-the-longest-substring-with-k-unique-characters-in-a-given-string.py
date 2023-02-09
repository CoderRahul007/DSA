# Given a string you need to print longest possible substring that has exactly M unique characters.
#  If there is more than one substring of longest possible length, then print any one of them.

# Examples: 

#     Input: Str = “aabbcc”, k = 1
#     Output: 2
#     Explanation: Max substring can be any one from {“aa” , “bb” , “cc”}.

#     Input: Str = “aabbcc”, k = 2
#     Output: 4
#     Explanation: Max substring can be any one from {“aabb” , “bbcc”}.

#     Input: Str = “aabbcc”, k = 3
#     Output: 6
#     Explanation: 
#     There are substrings with exactly 3 unique characters
#     {“aabbcc” , “abbcc” , “aabbc” , “abbc” }
#     Max is “aabbcc” with length 6.

#     Input: Str = “aaabbb”, k = 3
#     Output: Not enough unique characters
#     Explanation: There are only two unique characters, thus show error message. 

def longestSubstrWithKUniqueChar(s):
    charArr = [0] * 256
    maxLen = -1
    count = 0
    left = 0
    right = 0

    while right < n:
        if charArr[s[right]] == 0:
            count +=1
        charArr[s[right]] +=1
        
        if count == K :
            maxLen = max(maxLen, right - left + 1)
        if count > K:
            while count > K and left <= right:
                charArr[s[left]] -=1
                if charArr[s[left]] == 0:
                    count-=1
                    left +=1
        right +=1
    return maxLen
