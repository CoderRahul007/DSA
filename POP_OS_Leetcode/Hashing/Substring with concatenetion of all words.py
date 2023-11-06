class Solution:
    def findSubstring(self, s, words):
        wrdsTotalLen=len(words)*len(words[0])
        wrdLen=len(words[0])
        j=0
        res=[]
        while j<=len(s)-wrdsTotalLen:
            visWord=[0]*(len(words)+1)
            S=s[j:lw]
            for i in range(len(words)):
                idx=S.find(words[i-1])
                if idx!=-1:
                    ls[i]=1
                    S=S[:i]+S[i+len(words[i-1]):]
            found=False
            for i in range(1,len(ls)):
                if ls[i]!=1:
                    found=True
                    break
            if not found:
                res.append(j)
            j+=1
        return res
s=Solution()
s1 = "barfoothefoobarman"
words = ["foo","bar"]
print(s.findSubstring(s1,words))