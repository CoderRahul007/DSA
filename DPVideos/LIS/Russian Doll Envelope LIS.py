# This problem can be solved by DP and binary search
# If we sort the width by increasing order and the height by 
# decreasing order, we can perform LIS to find the longest increasing subsequence, 
# which is the maximum number of envelopes we can Russian doll

# We need to sort it this way because in russion dolls can only fit into another if 
# and only if both the width and height are greater than the previous envelope's width and height. 
# So within all the envelopes with the same width, we want to look at the envelopes with the greatest height first, 
# followed by the second greatest, and the rest in in decreasing order.
# Ex: ([1,2], [1,3], [1,4]) => ([1,4], [1,3], [1,2])

# For each envelope, we perform binary search on the env's height. If the height is greater than
#  all previous visited envelopes, then we simply add it to the current LIS. Otherwise, we want 
# to replace the first height in LIS that is greater than or equal to the current envelope's height
import bisect
def maxEnvelopes(envelopes):
	envelopes.sort(key= lambda x: (x[0], -x[1])) # 0th element increasing and 1st element decreasing
	lis = []

	for w, h in envelopes:
		left = binarySearch(lis, h)
		# left is greater than all elements in LIS
		if left == len(lis):
			lis.append(h)
		# Replace the first height that is >= than h with h
		else:
			lis[left] = h

	return len(lis)

# Return the index within nums that h would be in
def binarySearch(nums, h):
	l, r = 0, len(nums)-1

	while l <= r:
		mid = l + (r-l) // 2
		if nums[mid] == h:
			return mid
		if nums[mid] < h:
			l = mid + 1
		else:
			r = mid - 1
	return l

def maxEnvelopes(envelopes):
	tails = []
	for _, b in sorted(envelopes, key = lambda x: (x[0], -x[1])): 
		idx = bisect.bisect_left(tails, b)
		tails[idx:idx+1] = [b]
	return len(tails)


def maxEnvelopesDP(envelopes):
    envelopes.sort(key = lambda x : x[1])
    # print(envelopes)
    
    dp = [1 for _ in range(len(envelopes))]
    
    for i in range(1,len(envelopes)):
        cur_env = envelopes[i]
        
        for j in range(i):
            prev_env = envelopes[j]
            
            if prev_env[0] < cur_env[0] and prev_env[1] < cur_env[1]:
                dp[i] = max(dp[i] , dp[j]+1)
    # print(dp)
    
    return max(dp)
# O(n^2)


# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).