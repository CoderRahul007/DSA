'''

Consider all 0’s in arr[] as -1.
Create a hash table that holds the count of each sum[i] value, where sum[i] = sum(arr[0]+..+arr[i]), for i = 0 to n-1.
Now start calculating cumulative sum and then we get increment count by 1 for that sum represented as index in the hash table. Sub-array by each pair of positions with same value of cumulative sum constitute a continuous range with equal number of 1’s and 0’s.
Now traverse the hash table and get the frequency of each element in the hash table. Let frequency be denoted as freq. For each freq > 1 we can choose any two pair of indices of sub-array by (freq * (freq – 1)) / 2 number of ways .
Do the same for all freq and sum up the result that will be the number all possible sub-arrays containing equal number of 1’s and 0’s.
Also add freq of the sum 0 in the hash table to the final result.

Explanation:
Considering all 0’s as -1, if sum[i] == sum[j], where sum[i] = sum(arr[0]+..+arr[i]) and sum[j] = sum(arr[0]+..+arr[j]) and ‘i’ is less than ‘j’, then sum(arr[i+1]+..+arr[j]) must be 0. It can only be 0 if arr(i+1, .., j) contains equal number of 1’s and 0’s.
'''
# def countSubarrWithEqualZeroAndOne(arr, n): 
#     mp = dict() 
#     Sum = 0
#     count = 0
  
#     for i in range(n): 
  
#         # Replacing 0's in array with -1 
#         if (arr[i] == 0): 
#             arr[i] = -1
  
#         Sum += arr[i] 
  
#         # If Sum = 0, it implies number of  
#         # 0's and 1's are equal from arr[0]..arr[i] 
#         if (Sum == 0): 
#             count+=1
  
#         if (Sum in mp.keys()): 
#             count += mp[Sum] 
  
#         mp[Sum] = mp.get(Sum, 0) + 1
#     print(mp)
  
#     return count 



# Python3 implementation to count 
# subarrays with equal number 
# of 1's and 0's 

# function to count subarrays with 
# equal number of 1's and 0's 
def countSubarrWithEqualZeroAndOne (arr, n): 

	# 'um' implemented as hash table 
	# to store frequency of values 
	# obtained through cumulative sum 
	um = dict() 
	curr_sum = 0
	
	# Traverse original array and compute 
	# cumulative sum and increase count 
	# by 1 for this sum in 'um'. 
	# Adds '-1' when arr[i] == 0 
	for i in range(n): 
		curr_sum += (-1 if (arr[i] == 0) else arr[i]) 
		if um.get(curr_sum): 
			um[curr_sum]+=1
		else: 
			um[curr_sum]=1
	
	count = 0
	print(um)
	# traverse the hash table 'um' 
	for itr in um: 
		
		# If there are more than one 
		# prefix subarrays with a 
		# particular sum 
		if um[itr] > 1: 
			count += ((um[itr] * int(um[itr] - 1)) / 2) 
	print(count)
	# add the subarrays starting from 
	# 1st element and have equal 
	# number of 1's and 0's 
	if um.get(0): 
		count += um[0] 
	
	# required count of subarrays 
	return int(count)  

print(countSubarrWithEqualZeroAndOne([1,0,0,1,0,1,1],7))