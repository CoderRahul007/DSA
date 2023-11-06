# This approach relies on the same premise as the previous approach.
#  But, we need not use an array of size 2n+1\text{2n+1}2n+1, since it
#  isn't necessary that we'll encounter all the countcountcount values possible.
#  Thus, we make use of a HashMap mapmapmap to store the entries in the form of (index,count)(index, count)(index,count). 
# We make an entry for a countcountcount in the mapmapmap whenever the countcountcount is encountered 
# first, and later on use the correspoding index to find the length of the largest subarray with equal 
# no. of zeros and ones when the same countcountcount is encountered again.

# The following animation depicts the process:
class Solution:
    def findMaxLength(self, nums):
        d={}
        d[0]=-1 # index 0  count -1
        maxlen=0
        c=0
        for i in range(len(nums)):
            c+=(1 if nums[i]==1 else -1)
            if c in d:
                print(i-d[c],i,d[c])
                maxlen=max(maxlen,i-d[c]) 
                ''' if  count is not found in d then add it with corresponding index
                else the len is presentIndex -  index of found count for 0 add -1 else for 1 add 1      '''
            else:
                d[c]=i
        print(d)
        return maxlen

s=Solution()
print(s.findMaxLength([1,0,1]))
print(s.findMaxLength([1,0,1,1,0]))