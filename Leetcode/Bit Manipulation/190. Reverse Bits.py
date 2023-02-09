# Reverse bits of a given 32 bits unsigned integer.

# Note:

# Note that in some languages, such as Java, there is no unsigned integer type.
#  In this case, both input and output will be given as a signed integer type. 
#  They should not affect your implementation, as the integer's internal binary 
#  representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation.
#  Therefore, in Example 2 above, the input represents the signed integer -3 and the 
#  output represents the signed integer -1073741825.
 

# Example 1:

# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents
#  the unsigned integer 43261596, so return 964176192 which its binary representation 
#  is 00111001011110000010100101000000.
# Example 2:

# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101 represents 
# the unsigned integer 4294967293, so return 3221225471 which its binary representation 
# is 10111111111111111111111111111111.


#############################################################################################################
class Solution:
    def reverseBits(self, n: int) -> int:  # Time: O(1) and Space: O(1)
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1) # increase ans  , ans*2 + check if last is 0 or 1
            n >>= 1 # decrease n , n// 2
        return ans
# For example.
# Let n = 19 = 00000000000000000000000000010011
# Output: 11001000000000000000000000000000 = 3355443200.
# We initialize answer to 0, so in binary it's 32 zeroes.
# We loop over 32 times, since every integer is gonna have 32 possible 0/1.
# 1st line in the loop: n & 1, we check if last bit of n is set, is it 1 or 0,
#  ans << 1 we shift all bits that we already have in our answer to the left, 
# so after this shifting the bit on the right is 0, plus by using + we set the 
# last bit in the answer to the value that we got in n & 1.
# 2nd line in the loop we shift bits of our initial number n to the right,
# since we've already checked the last bit of n, so we just move on to the next bit.

# 0: answer = 0: 00000000000000000000000000000000
# answer << 1 = 00000000000000000000000000000000 +
# n=00000000000000000000000000010011 & 1=00000000000000000000000000000001 = 00000000000000000000000000000001
# ans = 00000000000000000000000000000001
# n = 00000000000000000000000000001001

# 1: answer = 1: 00000000000000000000000000000001
# answer << 1 = 00000000000000000000000000000010 +
# n=00000000000000000000000000001001 & 1=00000000000000000000000000000001 = 00000000000000000000000000000001
# ans = 00000000000000000000000000000011
# n = 00000000000000000000000000000100

# 2: answer = 3: 00000000000000000000000000000011
# answer << 1 = 00000000000000000000000000000110 + n & 1 = 00000000000000000000000000000000
# ans = 00000000000000000000000000000110
# n = 00000000000000000000000000000010

# 3: answer = 6: 00000000000000000000000000000110
# answer << 1 = 00000000000000000000000000001100 + n & 1 = 00000000000000000000000000000000
# ans = 00000000000000000000000000001100
# n = 00000000000000000000000000000001

# 4: answer = 12: 00000000000000000000000000001100
# answer << 1 = 00000000000000000000000000011000 + n & 1 = 00000000000000000000000000000001
# ans = 00000000000000000000000000011001
# n = 00000000000000000000000000000000

# And after that in our example, we'll just shift ** 00000000000000000000000000011001 all the way to the left,
# which will result in 11001000000000000000000000000000.