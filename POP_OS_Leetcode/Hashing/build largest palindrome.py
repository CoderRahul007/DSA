# For each letter, say it occurs v times. We know we have v // 2 * 2
#  letters that can be partnered for sure. For example, if we have 'aaaaa', 
#  then we could have 'aaaa' partnered, which is 5 // 2 * 2 = 4 letters partnered.

# At the end, if there was any v % 2 == 1, then that letter could have been a unique center.
#  Otherwise, every letter was partnered. To perform this check, we will check for v % 2 == 1 
#  and ans % 2 == 0, 
# the latter meaning we haven't yet added a unique center to the answer.
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d=dict()
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        res=0
        for v in d.values():
            partner=(v//2)*2
            res+=partner
            if res%2 ==0 and v%2 ==1:
                res+=1 # after one time increment of res it will always be odd and will 
                #never be even becz partner is even
        return res