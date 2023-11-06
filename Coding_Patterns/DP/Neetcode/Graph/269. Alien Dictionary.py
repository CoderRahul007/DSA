# Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. Find the order of characters in the alien language.
# Note: Many orders may be possible for a particular test case, thus you may return any valid order and output will be 1 if the order of string returned by the function is correct else 0 denoting incorrect string returned.
 

# Example 1:

# Input: 
# N = 5, K = 4
# dict = {"baa","abcd","abca","cab","cad"}
# Output:
# 1
# Explanation:
# Here order of characters is 
# 'b', 'd', 'a', 'c' Note that words are sorted 
# and in the given language "baa" comes before 
# "abcd", therefore 'b' is before 'a' in output.
# Similarly we can find other orders.

class Solution:
    def alienOrder(words):
        adj = { c: set() for w in words for c in w }

        for i in range(len(words) - 1):
            w1 , w1 = words[i] , words[i + 1]
            minLen = min(len(w1) , len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: # if the ordering is wrong then return ""
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]: # to add all the succeding characters to the key w1[j]
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = {} # False = visited , True = current Path i.e cycle
        res = []

        def dfs(c): # post order DFS
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)
