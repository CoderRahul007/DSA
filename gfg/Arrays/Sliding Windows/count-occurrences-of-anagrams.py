def areAnagrams( text , ptr ):
    d = {}
    for i in text:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in ptr:
        if i in d:
            d[i] -= 1
    for v in d.values():
        if d.values() != 0:
            return False
    return True

def countOccurence( text , ptr):
    res = 0
    for i in range(len(text)-len(ptr)+1):
        if areAnagrams(text[i : i+len(ptr)], ptr):
            res+=1
    return res

# Above is the naive solution

# We can achieve O(n) time complexity under the assumption that alphabet size is fixed which is typically true as we have maximum 256 possible characters in ASCII. The idea is to use two count arrays:

# 1) The first count array store frequencies of characters in pattern.
# 2) The second count array stores frequencies of characters in current window of text.

# The important thing to note is, time complexity to compare two count arrays is O(1) as the number of elements in them are fixed (independent of pattern and text sizes). Following are steps of this algorithm.
# 1) Store counts of frequencies of pattern in first count array countP[]. Also store counts of frequencies of characters in first window of text in array countTW[].

# 2) Now run a loop from i = M to N-1. Do following in loop.
# …..a) If the two count arrays are identical, we found an occurrence.
# …..b) Increment count of current character of text in countTW[]
# …..c) Decrement count of first character in previous window in countWT[]

# 3) The last window is not checked by above loop, so explicitly check it.

# not working
def search( ptr, text):
	    mt = {}
	    mp = {}
	    c = 0
	    if len(text) < len(ptr):
	        return 0
	    for i in range(len(ptr)):
	        mp[ptr[i]] =   mp[ptr[i]] + 1 if ptr[i] in mp else 1
	        mt[text[i]] =   mt[text[i]]+1 if text[i] in mt else 1
	    if mt == mp:
	        c+=1
	    for i in range(len(ptr) , len(text)):
	        mt[text[i]] = mt[text[i]] + 1 if text[i] in mt else 1
	        mt[text[i-len(ptr)]] = mt[text[i-len(ptr)]] - 1 if text[i-len(ptr)] in mt else 0
	       
	        if mt == mp:
	            c+=1
	    return c

# A Simple Python program to count anagrams of a
# pattern in a text with the help of sliding window problem
string = "forxxorfxdofr"
ptr = "for"
n = len(string)
k = len(ptr)
temp = []
d = {}
for i in ptr:
	if i in d:
		d[i] += 1
	else:
		d[i] = 1
i = 0
j = 0
count = len(d)

ans = 0


while j < n:
	if string[j] in d:
		d[string[j]] -= 1
		if d[string[j]] == 0:
			count -= 1
	if (j-i+1) < k:
		j += 1
	elif (j-i+1) == k:
		if count == 0:
			ans += 1

		if string[i] in d:
			d[string[i]] += 1
			if d[string[i]] == 1:
				count += 1

		i += 1
		j += 1
print(ans)

# class Solution {

#     int search(String pat, String txt) {
#         // code here
#         if(txt.length() < pat.length()){
#            return 0;
#        }
       
#        int countpat[] = new int[26];
#        int counttxt[] = new int[26];
      
#        for(int i = 0; i < pat.length(); i++){
      
#            countpat[pat.charAt(i)-'a']++;
#            counttxt[txt.charAt(i)-'a']++;
#        }
       
#        int count = 0;
#        if(Arrays.equals(countpat, counttxt)){
#                count++;
#        }
           
#        for(int i = pat.length(); i < txt.length(); i++){
           
           
#            counttxt[txt.charAt(i)-'a']++;
#            counttxt[txt.charAt(i-pat.length())-'a']--;
           
#            if(Arrays.equals(countpat, counttxt)){
#                count++;
#            }
           
#        }
       
#        return count;
#     }
# }        