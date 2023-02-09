# Find out the maximum sub-array of non negative numbers from an array.

# The sub-array should be contiguous i.e., a sub-array created by choosing the
#  second and fourth element and skipping the third element is invalid.

# Maximum sub-array is defined in terms of the sum of the elements in the sub-array.
#  Sub-array A is greater than sub-array B if sum(A) > sum(B).

# Example:
# A : [1, 2, 5, -7, 2, 3]
# The two sub-arrays are [1, 2, 5] [2, 3].
# The answer is [1, 2, 5] as its sum is larger than [2, 3]

# NOTE 1: If there is a tie, then compare with segment's length and return segment which has maximum length.
# NOTE 2: If there is still a tie, then return the segment with minimum starting index.

# Example 1:

# Input:
# N = 3
# A[] = {1, 2, 3}
# Output: 1 2 3
# Explanation: In the given array every
# element is non-negative.

# Example 2:

# Input:
# N = 2
# A[] = {-1, 2}
# Output: 2
# Explanation: The only subarray [2] is
# the answer.