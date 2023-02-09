# The tower of Hanoi is a famous puzzle where we have three rods and N disks. 
# The objective of the puzzle is to move the entire stack to another rod.
#  You are given the number of discs N. Initially, these discs are in the rod 1.
#  You need to print all the steps of discs movement so that all the discs reach 
# the 3rd rod. Also, you need to find the total moves.
# Note: The discs are arranged such that the top disc is numbered 1 and the 
# bottom-most disc is numbered N. Also, all the discs have different sizes and
#  a bigger disc cannot be put on the top of a smaller disc. Refer the provided
#  link to get a better clarity about the puzzle.

# Example 1:

# Input:
# N = 2
# Output:
# move disk 1 from rod 1 to rod 2
# move disk 2 from rod 1 to rod 3
# move disk 1 from rod 2 to rod 3
# 3
# Explanation: For N=2 , steps will be
# as follows in the example and total
# 3 steps will be taken.

# Example 2:

# Input:
# N = 3
# Output:
# move disk 1 from rod 1 to rod 3
# move disk 2 from rod 1 to rod 2
# move disk 1 from rod 3 to rod 2
# move disk 3 from rod 1 to rod 3
# move disk 1 from rod 2 to rod 1
# move disk 2 from rod 2 to rod 3
# move disk 1 from rod 1 to rod 3
# 7
# Explanation: For N=3 , steps will be
# as follows in the example and total
# 7 steps will be taken.

class Solution:
    def toh(self, N, fromm, to, aux):
        # Your code here
        if N==1:
            print("move disk " + str(1) + " from rod " + str(fromm) + " to rod " + str(to))
            return 1
        self.toh(N-1,fromm,aux,to)
        print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
        self.toh(N-1,aux,to,fromm)
        return 2**N-1