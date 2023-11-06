# import collections
# class Solution(object):
#     def subarraysDivByK(self, A, K):
#         P = [0]
#         for x in A:
#             P.append((P[-1] + x) % K)
#         print(P)
#         count = collections.Counter(P)
#         print(count)
#         l=[v*(v-1)/2 for v in count.values()]
#         print(l)
#         return sum(v*(v-1)/2 for v in count.values())


# Let there be a subarray (i, j) whose sum is divisible by k
#   sum(i, j) = sum(0, j) - sum(0, i-1)
# Sum for any subarray can be written as q*k + rem where q 
# is a quotient and rem is remainder
# Thus,     
#     sum(i, j) = (q1 * k + rem1) - (q2 * k + rem2)
#     sum(i, j) = (q1 - q2)k + rem1-rem2
     
# We see, for sum(i, j) i.e. for sum of any subarray to be
# divisible by k, the RHS should also be divisible by k.
# (q1 - q2)k is obviously divisible by k, for (rem1-rem2) to 
# follow the same, rem1 = rem2 where
#     rem1 = Sum of subarray (0, j) % k
#     rem2 = Sum of subarray (0, i-1) % k 
from collections import defaultdict
class Solution(object):
    def subarraysDivByK(self, A, K):
        res = 0
        count = 0
        letter = defaultdict(int)
        letter[0] = 1
        for i in A:
            res+=i
            if res%K in letter:
                count+= letter[res%K]
            letter[res%K] += 1
        print(letter)
        return count
# class Solution:
#     def subarraysDivByK(self, A: List[int], K: int) -> int:
#         count = 0
#         seen = defaultdict(int)
#         for remainder in accumulate(A, lambda x, y: (x + y) % K, initial=0):
#             count += seen[remainder]
#             seen[remainder] += 1
#         return count


#---------------------------------------------------------------------
# Python program to find 
# count of subarrays with 
# sum divisible by k. 

# Handles all the cases 
# function to find all 
# sub-arrays divisible by k 
# modified to handle 
# negative numbers as well 
# def subCount(arr, n, k): 

# 	# create auxiliary hash 
# 	# array to count frequency 
# 	# of remainders 
# 	mod =[] 
# 	for i in range(k + 1): 
# 		mod.append(0) 
	
# 	# Traverse original array 
# 	# and compute cumulative 
# 	# sum take remainder of this 
# 	# current cumulative 
# 	# sum and increase count by 
# 	# 1 for this remainder 
# 	# in mod[] array 
# 	cumSum = 0
# 	for i in range(n): 
# 		cumSum = cumSum + arr[i] 
		
# 		# as the sum can be negative, 
# 		# taking modulo twice 
# 		mod[((cumSum % k)+k)% k]= mod[((cumSum % k)+k)% k] + 1
	
	
# 	result = 0 # Initialize result 
	
# 	# Traverse mod[] 
# 	for i in range(k): 
	
# 		# If there are more than 
# 		# one prefix subarrays 
# 		# with a particular mod value. 
# 		if (mod[i] > 1): 
# 			result = result + (mod[i]*(mod[i]-1))//2
	
# 	# add the elements which 
# 	# are divisible by k itself 
# 	# i.e., the elements whose sum = 0 
# 	result = result + mod[0] 
	
# 	return result 
	
# # driver code 

# arr = [4, 5, 0, -2, -3, 1] 
# k = 5
# n = len(arr) 

# print(subCount(arr, n, k)) 
# arr1 = [4, 5, 0, -12, -23, 1] 

# k1 = 5
# n1 = len(arr1) 
# print(subCount(arr1, n1, k1)) 

# # This code is contributed 
# # by Anant Agarwal. 

s=Solution()
print(s.subarraysDivByK([4,5,0,-2,-3,1],5))
print(s.subarraysDivByK([4,5],5))