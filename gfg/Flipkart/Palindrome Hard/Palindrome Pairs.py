# https://www.youtube.com/watch?v=SSq0xH51pZQ
class Solution:
        def palindromepair(self, N, arr):
            # code here 
            def isPal(w):
                st = 0
                end = len(w)-1
                
                while st < end:
                    if w[st] != w[end]:
                        return False
                    st+=1
                    end-=1
                return True
            out = []
            d = {w:i for i , w in enumerate(arr)}
            for i in range(N):
                w = arr[i]
                if w == "": # if word is empty then any other palindrome words in the arr will be true
                    for j in range(N):
                        w1 = arr[j]
                        if i != j and isPal(w1):
                            return 1
                    continue

                bw = w[::-1]
                if bw in d and d[bw] != i: # is reverse of a word is present then that must be the pair
                    return 1
                for k in range(1 , len(w)):
                    if isPal(w[:k]) and w[k:][::-1] in d: # is palindrome of length k and its reverse of a word is present then its true
                        return 1
                    if isPal(w[k:]) and w[:k][::-1] in d:
                        return 1
            return 0


 

# Given an array of strings arr[] of size N, find if there exists 2 strings arr[i] and arr[j] 
# such that arr[i]+arr[j] is a palindrome i.e the concatenation of string arr[i] and arr[j] results into a palindrome.


# Example 1:

# Input:
# N = 6
# arr[] = {"geekf", "geeks", "or","keeg", "abc", 
#           "bc"}
# Output: 1 
# Explanation: There is a pair "geekf"
# and "keeg".

# Example 2:

# Input:
# N = 5
# arr[] = {"abc", "xyxcba", "geekst", "or", "bc"}
# Output: 1
# Explanation: There is a pair "abc"
# and "xyxcba".


