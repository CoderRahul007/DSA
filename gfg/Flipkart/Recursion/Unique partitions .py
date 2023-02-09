# Given a positive integer n, generate all possible unique ways to represent n as sum of positive integers.

# Example 1:

# Input: n = 3
# Output: 3 2 1 1 1 1
# Explanation: For n = 3, 
# {3}, {2, 1} and {1, 1, 1}.

 

# Example 2:

# Input: n = 4 
# Output: â€‹4 3 1 2 2 1 1 1 1 
# Explanation: For n = 4, 
# {4}, {3, 1}, {2, 2}, {1, 1, 1, 1}.

# A utility function to print an
# array p[] of size 'n'
def printArray(p, n):
	for i in range(0, n):
		print(p[i], end = " ")
	print()

def printAllUniqueParts(n):
	p = [0] * n	 # An array to store a partition
	k = 0		 # Index of last element in a partition
	p[k] = n	 # Initialize first partition
				# as number itself

	# This loop first prints current partition,
	# then generates next partition.The loop
	# stops when the current partition has all 1s
	while True:
		
			# print current partition
			printArray(p, k + 1)

			# Generate next partition

			# Find the rightmost non-one value in p[].
			# Also, update the rem_val so that we know
			# how much value can be accommodated
			rem_val = 0
			while k >= 0 and p[k] == 1:
				rem_val += p[k]
				k -= 1

			# if k < 0, all the values are 1 so
			# there are no more partitions
			if k < 0:
				print()
				return

			# Decrease the p[k] found above
			# and adjust the rem_val
			p[k] -= 1
			rem_val += 1

			# If rem_val is more, then the sorted
			# order is violated. Divide rem_val in
			# different values of size p[k] and copy
			# these values at different positions after p[k]
			while rem_val > p[k]:
				p[k + 1] = p[k]
				rem_val = rem_val - p[k]
				k += 1

			# Copy rem_val to next position
			# and increment position
			p[k + 1] = rem_val
			k += 1

# Driver Code
print('All Unique Partitions of 2')
printAllUniqueParts(2)

print('All Unique Partitions of 3')
printAllUniqueParts(3)

print('All Unique Partitions of 4')
printAllUniqueParts(4)


# Solution: We print all partition in sorted order and numbers within a partition are also 
# printed in sorted order (as shown in the above examples). The idea is to get the next
#  partition using the values in the current partition. We store every partition in an 
# array p[]. We initialize p[] as n where n is the input number. In every iteration.
#  we first print p[] and then update p[] to store the next partition. So the main problem 
# is to get the next partition from a given partition. 

# Steps to get next partition from current partition: 
# We are given current partition in p[] and its size. We need to update p[] to store next
#  partition. Values in p[] must be sorted in non-increasing order. 

# Find the rightmost non-one value in p[] and store the count of 1’s encountered before 
# a non-one value in a variable rem_val (It indicates sum of values on right side to be updated). Let the index of non-one value be k.
# Decrease the value of p[k] by 1 and increase rem_val by 1. Now there may be two cases: 
# a) If p[k] is more than or equal to rem_val. This is a simple case (we have the sorted 
# order in new partition). Put rem_val at p[k+1] and p[0…k+1] is our new partition.
# b) Else (This is a interesting case, take initial p[] as {3, 1, 1, 1}, p[k] is decreased 
# from 3 to 2, rem_val is increased from 3 to 4, divide rem_val in different values of size
#  p[k] and copy these values at different positions after p[k], so the next partition should be {2, 2, 2}).
# Copy p[k] to next position, increment k and reduce count by p[k] while p[k] is less than 
# rem_val. Finally, put rem_val at p[k+1] and p[0…k+1] is our new partition. This step is 
# like dividing rem_val in terms of p[k] (4 is divided in 2’s).
# Following is the implementation of above algorithm: 

##########################################################################################

# 	void helper(vector<vector<int>>&ans,vector<int>&curr,int i,int n)
# {
#     if(n==0)
#     {
#         ans.push_back(curr);
#         return;
#     }
#     if(i<1)
#     {
#         return;
#     }
#     if(i<=n)
#     {
#         curr.push_back(i);
#         helper(ans,curr,i,n-i);
#         curr.pop_back();
#         helper(ans,curr,i-1,n);
#     }
#     else
#     {
#         helper(ans,curr,i-1,n);
#     }
# }
#     vector<vector<int>> UniquePartitions(int n) {
#         // Code here
#          vector<vector<int>>ans;
#         vector<int>curr;
#         helper(ans,curr,n,n);
#         return ans;
#     }


##########################################

# void uniquePartitionsHelper(int reqSum,int i,int n,vector<int>temp)
# {
#     if(reqSum==0)
#     {
#         reverse(temp.begin(),temp.end());
#         s.insert(temp);
#         return;
#     }
    
    
#      //i can be a max of n-1
#     if(i==n)
#     return;
    
#     if(i>reqSum)
#     return;
    
#     //now i is less than or equal to reqSum
    
#     //either i will take i or not
    
#     //if i dont take i
#     uniquePartitionsHelper(reqSum,i+1,n,temp);
    
#     //if i take i
#     temp.push_back(i);
#     uniquePartitionsHelper(reqSum-i,i,n,temp);
   
# }


	# void UniquePartitionsRec(int n,vector<int>v,int i,vector<vector<int>>&ans)
	# {
	#     if(n==0)
	#     {
	#         ans.push_back(v);
	#         return ;
	#     }
	#     for(int j=i;j>=1;j--)
	#     {
	#         if(n-j>=0)
	#         {
	#             v.push_back(j);
	#             UniquePartitionsRec(n-j,v,j,ans);
	#             v.pop_back();
	#         }
	#     }
	#     return ;
	# }
    # vector<vector<int>> UniquePartitions(int n) {
    #     // Code here
    #     vector<int>v;
    #     vector<vector<int>>ans;
    #     UniquePartitionsRec(n,v,n,ans);
    #     return ans;
    # }