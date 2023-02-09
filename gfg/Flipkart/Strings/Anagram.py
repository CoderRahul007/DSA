from collections import Counter
class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        c1 = Counter(a)
        c2 = Counter(b)
        
        if c1 == c2:
            return True
        else:
            return False
        


# bool isAnagram(string a, string b){
#         if(a.length()!=b.length()) return false; 
#         unordered_map<char,int> m ;
#         for(int i=0 ; i<a.length() ; i++)
#             m[a[i]]++ ;
#         for(int i=0 ; i<b.length() ; i++)
#             m[b[i]]-- ;
#         for(auto it : m)
#             if(it.second!=0) return false ;
            
#         return true ;
#     }        