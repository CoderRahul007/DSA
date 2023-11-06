# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         if s == t:
#             return True
        
#         hashmap = {} # for one to one mapping
#         print(list(zip(s, t)))
#         for chars, chart in zip(s, t):

#             if chars in hashmap.keys() and hashmap[chars] != chart:
#                 return False 
#             elif chart in hashmap.values() and hashmap.get(chars) != chart:
#                 return False
#             else:
#                 hashmap[chars] = chart

#         return True


# Since the mapping of characters must be order preserving, 
# the two strings are isomorphic if and only if the map from the characters of s to t,
#  where both s and t are viewed as ordered sets of characters, defined by s[i] --> t[i] for all i in {0, ..., s.size()-1}.
#  is a bijection whose image is exactly the string t. The characters of s and t in all test cases run from only the ASCII values 0 to 127, 
# so we need only two arrays each of size 127 for O(1) space total. The first array, func, is defined such that, for any i in {0, ..., s.size()-1},
#  func[s[i]] = -1 if s[i] has not been mapped to a character of t yet, and func[s[i]] equals some character of t otherwise, and image[t[i]] 
# equals 0 if t[i] does not yet have a character preimage in s, and image[t[i]] = 1 otherwise. It is intuitively easy to see that this mapping is 
# not a bijection if and only if while looping from i=0 to i=s.size()-1 we find some i such that s[i] does not yet have an image in t but its
#  prospective image t[i] already has a preimage, or s[i] already has an image, i.e., s[i] it occurs as a character in some earlier index in s,
#  but this image of s[i] does not equal its prospective image t[i]; in the former case, the map cannot be order-preserving, and in the second case
# , the map cannot be well-defined if it is forced to be a bijection. This proves both the correctness of the following algorithm and the fact that
#  all we need to do per iteration in the for-loop from i=0 to i=s.size()-1 are O(1) constant-time checks and updates, so that the total runtime is 
# O(n).

# class Solution {
# public:
#     bool isIsomorphic(string s, string t) {
#         if (s.size()==0) return true;
#         int func[128];
#         bool image[128];
#         for (int i=0; i<128; ++i) {func[i]=-1; image[i]=0;}
#         for (int i=0; i<s.size(); ++i) {
#             if (func[s[i]] == -1 && image[t[i]] == 1) return false;
#             if (func[s[i]] != -1 && func[s[i]] != t[i]) return false;
#             func[s[i]]=t[i]; image[t[i]]=1;
#         }
#         return true;
#     }
# };

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sarr=[-1]*128
        tarr=[-1]*128
        if s==t:
            return True
        for i in range(len(s)):
            si=ord(s[i])
            ti=ord(t[i])
            if sarr[si]==-1:
                sarr[si]=ti
            if tarr[ti]==-1:
                tarr[ti]=si
            if sarr[si]!=ti or tarr[ti]!=si:
                return False
        print(sarr,tarr,end='/n')
        return True
        
s= Solution()
print(s.isIsomorphic('egg','add'))
print(s.isIsomorphic('aa','ab'))