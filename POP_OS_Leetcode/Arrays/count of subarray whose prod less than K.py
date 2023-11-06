# Intuition

# Because log⁡(∏ixi)=∑ilog⁡xi\log(\prod_i x_i) = \sum_i \log x_ilog(∏i​xi​)=∑i​logxi​,
#  we can reduce the problem to subarray sums instead of subarray products. 
# The motivation for this is that the product of some arbitrary subarray may be way too large 
# (potentially 1000^50000), and also dealing with sums gives us some more familiarity as it
#  becomes similar to other problems we may have solved before.

# Algorithm

# After this transformation where every value x becomes log(x), let us take prefix sums prefix[i+1] = nums[0] + nums[1] + ... + nums[i].
#  Now we are left with the problem of finding, for each i, the largest j so that nums[i] + ... + nums[j] = prefix[j] - prefix[i] < k.

# Because prefix is a monotone increasing array, this can be solved with binary search. We add the width of the interval [i, j] to our answer, 
# which counts all subarrays [i, k] with k <= j.

# Python
import bisect
import math
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k == 0: return 0
        k = math.log(k)

        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + math.log(x))
        print(prefix)

        ans = 0
        for i, x in enumerate(prefix):
            j = bisect.bisect(prefix, x + k - 1e-9, i+1)
            ans += j - i - 1
        return ans
def SecndApproach(arr,k):
    l=0
    ans=0
    p=1
    for r,v in enumerate(arr):
        p*=v
        print('P',p)
        while p>=k:
            p/=arr[l]
            print('p',p)
            l+=1
            print('l',l)
        ans+=r-l+1
        print('Ans',ans)
    return ans

s=Solution()
print(s.numSubarrayProductLessThanK([10,5,2,6],100))

print('-------------------------------------------------------')
print(SecndApproach([10,5,2,6],100))