'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
'''
class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        arr=string.split()     
        if len(arr)!=len(pattern):
            return False
        patt={}
        strng={}
        for i in range(len(pattern)):       
            p=patt.get(pattern[i],None) #NOne
            s=strng.get(arr[i],None)# a
            if p==None and s== None:
                patt[pattern[i]]=arr[i] #cat
                strng[arr[i]]=pattern[i] #b
            elif p!=None and s !=None and p!=arr[i] and s!=pattern[i]:           
                return False
            elif p== None and s!=None and s!=pattern[i]:
                return False
            elif s==None and p!=None and p!=arr[i]:
                return False  
        return True
s=Solution()
print(s.wordPattern("abba","dog cat cat dog"))
print(s.wordPattern("aba","dog cat cat"))
print(s.wordPattern("abc","dog cat dog"))
print(s.wordPattern("abba","dog dog dog dog"))
print(s.wordPattern("aaa",
"aa aa aa aa"
))