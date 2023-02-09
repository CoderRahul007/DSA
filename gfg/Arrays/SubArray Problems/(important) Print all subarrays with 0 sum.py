# Input:  arr = [6, 3, -1, -3, 4, -2, 2,
#              4, 6, -12, -7]
# Output:
# Subarray found from Index 2 to 4
# Subarray found from Index 2 to 6
# Subarray found from Index 5 to 6
# Subarray found from Index 6 to 9
# Subarray found from Index 0 to 10

# subarray is equal to 0 or not. The complexity of this solution would be O(n^2).
# A better approach is to use Hashing.
# Do following for each element in the array


# Maintain sum of elements encountered so far in a variable (say sum).
# If current sum is 0, we found a subarray starting from index 0 and ending at index current index
# Check if current sum exists in the hash table or not.
# If current sum already exists in the hash table then it indicates that this sum was the sum of some sub-array elements arr[0]…arr[i] and now the same sum is obtained for the current sub-array arr[0]…arr[j] which means that the sum of the sub-array arr[i+1]…arr[j] must be 0.
# Insert current sum into the hash table

# Python3 program to print all subarrays
# in the array which has sum 0

# Function to get all subarrays
# in the array which has sum 0
def findSubArrays(arr, n):

        # create a python dict
        hashMap = {}

        # create a python list
        # equivalent to ArrayList
        out = []

        # tracker for sum of elements
        sum1 = 0
        for i in range(n):

            # increment sum by element of array
            sum1 += arr[i]

            # if sum is 0, we found a subarray starting
            # from index 0 and ending at index i
            if sum1 == 0:
                out.append((0, i))
            found_sum_indexes = []

            # If sum already exists in the map
            # there exists at-least one subarray
            # ending at index i with 0 sum
            print("hashmap before" , hashMap.items())
            print("Before output " , out)
            if sum1 in hashMap:

                # map[sum] stores starting index
                # of all subarrays
                found_sum_indexes = hashMap.get(sum1) # index of sum1 found               
                for it in range(len(found_sum_indexes)):
                    out.append((found_sum_indexes[it] + 1, i))

            found_sum_indexes.append(i)
            hashMap[sum1] = found_sum_indexes
            print("hashmap after" , hashMap.items())
            print("After output " , out)
        return out

# Utility function to print
# all subarrays with sum 0
def printOutput(output):
	for i in output:
		print ("Subarray found from Index " +
				str(i[0]) + " to " + str(i[1]))

def countOfSubarrs(arr , n):
    c = 0
    map = {}
    s = 0
    map[0] = 1
    i= -1
    while i < n-1:
        i+=1
        s+=arr[i]
        if s in map:
            c+=map[s]
            map[s] = map[s]+1
        else:
            map[s] =1
    return c

# Driver Code
if __name__ == '__main__':
	arr = [6, 3, -1, -3, 4, -2,
			2, 4, 6, -12, -7]
	n = len(arr)
	out = findSubArrays(arr, n)
	
	# if we did not find any subarray with 0 sum,
	# then subarray does not exists
	if (len(out) == 0):
		print ("No subarray exists")
	else:
		printOutput (out)


# https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup/hashmap-and-heaps/count-of-all-subarrays-with-zero-sum-official/ojquestion


