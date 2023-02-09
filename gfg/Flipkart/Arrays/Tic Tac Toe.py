# A Tic-Tac-Toe board is given after some moves are played. Find out if the given board is valid,
#  i.e., is it possible to reach this board position after some moves or not.

# Note that every arbitrary filled grid of 9 spaces isn’t valid e.g. a grid filled with 
# 3 X and 6 O isn’t valid situation because each player needs to take alternate turns.

# Note :  The game starts with X


# Example 1:

# Input:
# board[] = {'X', 'X', 'O', 
#            'O', 'O', 'X',
#            'X', 'O', 'X'};
# Output: Valid
# Explanation: This is a valid board.


# Example 2:

# Input:
# board[] = {'O', 'X', 'X', 
#            'O', 'X', 'X',
#            'O', 'O', 'X'};
# Output: Invalid
# Explanation: Both X and O cannot win
class Solution:
    def isValid(self, board):
        # code here
        xc = board.count('X')
        oc = board.count('O')
        if xc - oc != 1:
            return False
        win=[[0,1,2],
           [3,4,5],
           [6,7,8],
           [0,3,6],
           [1,4,7],
           [2,5,8],
           [0,4,8],
           [2,4,6]]
        
        ow = False
        xw = False
        for i in range(8):
            if board[win[i][0]] == 'O' and board[win[i][1]] == 'O' and board[win[i][2]] == 'O':
                ow = True
            if board[win[i][0]] == 'X' and board[win[i][1]] == 'X' and board[win[i][2]] == 'X':
                xw = True
        if ow :
            return False
        return True