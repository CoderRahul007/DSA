# Given a 5x6 snakes and ladders board, find the minimum number of dice throws required
#  to reach the destination or last cell (30th cell) from the source (1st cell).

# You are given an integer N denoting the total number of snakes and ladders and an 
# array arr[] of 2*N size where 2*i and (2*i + 1)th values denote the starting and 
# ending point respectively of ith snake or ladder. The board looks like the following.


                                   

# Example 1:

# Input:
# N = 8
# arr[] = {3, 22, 5, 8, 11, 26, 20, 29, 
#        17, 4, 19, 7, 27, 1, 21, 9}
# Output: 3
# Explanation:
# The given board is the board shown
# in the figure. For the above board 
# output will be 3. 
# a) For 1st throw get a 2. 
# b) For 2nd throw get a 6.
# c) For 3rd throw get a 2.

from collections import deque
class Solution:
    def minThrow(self, N, arr):
        # code here
        #creating the board
        board = [-1]*31   
        for i in range(0,2*N,2):
            board[arr[i]] = arr[i+1]
        #print(board)
        
        queue = deque()
        queue.append([1,0])#square,moves
        visited = set()
        while queue:
            #moves += 1
            a,b = queue.popleft()
            for i in range(1,7):
                next_ = a + i
            
               
          		#check if there is a snake or ladder at that postion
                if board[next_] != -1:
                    next_ = board[next_]

                #if the boaRd is equal to 30 return moves
                if next_ == 30:
                    return b + 1
                if next_ not in visited:
                    visited.add(next_)
                    queue.append([next_ , b + 1])