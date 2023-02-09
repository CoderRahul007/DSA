# Rearrange array such that `A[A[i]]` is set to `i` for every element `A[i]`
# Given an unsorted integer array A of size n, whose elements lie in the range
#  0 to n-1, rearrange the array such that A[A[i]] is set to i for every array
#  element A[i]. Do this in linear time and without using any extra constant space.

# For example,

# Input:  {1, 3, 4, 2, 0}
# Output: {4, 0, 3, 1, 2}
 
# Explanation:
 
# A[0] = 1, A[1] becomes 0
# A[1] = 3, A[3] becomes 1
# A[2] = 4, A[4] becomes 2
# A[3] = 2, A[2] becomes 3
# A[4] = 0, A[0] becomes 4

# The above solution uses extra space that violates the problem constraints. We can solve this problem without using any extra space by taking advantage of the fact that array elements lie in range 0 to n-1. For each element A[i] present in the array, increment value present at index A[i] % n by i × n. Finally, traverse the modified array and set A[i] = A[i] / n. For example, consider array {1, 3, 4, 2, 0}. After incrementing value present at index A[i] % n for each element A[i] by i × n, the array becomes:

# {1 + 5 × 4, 3, 4 + 5 × 3, 2 + 5 × 1, 0 + 5 × 2} = {21, 3, 19, 7, 10}.

# Now if we take A[i] / n for each index i, we get {4, 0, 3, 1, 2}. Following is the C, Java, and Python implementation based on this idea:


# Function to rearrange a list such that `A[A[i]` is set to `i`
# for every element `A[i]`
def rearrange(A):
 
    n = len(A)
 
    # for each element `A[i]`, increment value present at index
    # `(A[i] % n)` by `i×n`
    for i in range(n):
        A[A[i] % n] += i * n
 
    # traverse the modified list and set `A[i] = A[i] / n`
    for i in range(n):
        A[i] = A[i] // n
 
 
if __name__ == '__main__':
 
    A = [1, 3, 4, 2, 0]
 
    rearrange(A)
    print(A)