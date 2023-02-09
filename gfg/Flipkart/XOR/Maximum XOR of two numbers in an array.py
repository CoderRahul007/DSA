# Given an array of non-negative integers of size N.
#  Find the maximum possible XOR between
#  two numbers present in the array.

# Example 1:

# Input:
# Arr = {25, 10, 2, 8, 5, 3}
# Output: 28
# Explanation:
# The maximum result is 5 ^ 25 = 28.

# Example 2:

# Input :
# Arr = {1, 2, 3, 4, 5, 6, 7}
# Output : 7
# Explanation :
# The maximum result is 1 ^ 6 = 7.

#    let ni and nj be the numbers such that xor between them produces maximum
#     value among other pairs. let m be the max value.

#     m = ni ^ nj
#     => m ^ nj = (ni ^ nj) ^ nj
#     =>        = ni ^ (nj ^ nj) # xor is associative
#     =>        = ni ^ 0
#     =>        = ni

#     so, m ^ nj = ni

#     We note that m is 31-bit integer so we guess bits of m and and with each nj,
#     we check if the combination of m and nj will produce ni.

#     So time complexity becomes O(32N) = O(N)
 
#  Algorithm

# Calculate the number of bits, maxBits to be used. It is the length of the maximum number in the binary representation.
# Loop from i = maxBits - 1 to i = 0, i.e. from the leftmost bit to the rightmost bit. In each iteration, do the following
#     Left shift maxXOR to free the next bit.
#     The variable currXOR is set to maxXOR | 1 by setting 1 in the rightmost bit of maxXOR. 
# Note that | is the bitwise inclusive OR operator.
#     Compute all the possible prefixes of length maxBits - i by iterating over arr.
#         Put in the HashSet, the prefix of the current number of length maxBits - 1, 
#        this is done using arr >> i in the code.
#     Now iterate through the prefix, and check if currXOR could be achieved using p1^p2.
#         By Using the self-inverse property of XOR, currXOR = p1^p2 can be rewritten as p1 == currXOR^p2.
#         So simply check for each p, if currXOR^p is in the prefix HashSet or not. If it is there, then maxXOR will be equal to the currXOR.
#     Return maxXOR.


# https://www.youtube.com/watch?v=PTvFn17ZDRg
def findMaximumXOR(nums):
    max, mask = 0, 0
    for i in range(32)[::-1]:
        print("mask before " , bin(mask))
        mask |= 1 << i
        print("mask after " , bin(mask))
        prefixes = {n & mask for n in nums} # if ith bit of num is 1 then its added in prefixes
        print('prefixes '  , prefixes)

        tmpMax = max | (1 << i) # setting ith bit and adding to max 

        if any(prefix ^ tmpMax in prefixes for prefix in prefixes):
            max = tmpMax
    return max


arr = [3, 10, 5, 25, 2, 8]
print(findMaximumXOR(arr))

# The time complexity of the above program is O(N*log(M)), 
# where N is the size of the array and M is the maximum element of the array.

# The space complexity is O(N).