#####################################################################################
#  Bruteforce

# The possible answer can be from 1 to max( positions[i] ) so we select one integer at a time form 
# 1 to max( positions[i] ) and see if it is possible for that integer to be our answer.
# Now how will we find whether an integer X is our possible answer or not? We can try to add the maximum
#  number of players such that the distance between any two players is more than one equal to X.
# How can we implement this? We can sort the positions first and can assume the first player is in the 
# room first that is empty( positions[0] ). Now we will give a new room positions[i] to the next player 
# only if the difference between the current room ( positions[i] ) and the previous allocated room is 
# greater than or equal to X.
# If by doing this we can allocate rooms to at least C players, the answer exists otherwise not.
# Optimization: once we find  X for which the answer does not exist then we can simply stop our search 
# because the answer will be possible for all X’s greater than current X.
# The answer is the maximum possible X.

# Time Complexity

# O(N * max), where N is the total number of rooms and max is the maximum possible position for any room.

# As we have to traverse all the possible answers and the answers are up to max. For each possible answer, we have to traverse all the positions of the room which is N. Hence, the overall Time Complexity is O(N * max).
# Space Complexity

# O(1).

# https://www.codingninjas.com/codestudio/problems/chess-tournament_981299?topList=striver-sde-sheet-problems&leftPanelTab=0
from os import *
from sys import *
from collections import *
from math import *

def chessTournament(pos, n , cnt):
    pos.sort()
    ans = 0
    mp = pos[n-1]
    for i in range(1 , mp):
        prev = pos[0]
        c = 1 # 1 team member has occupied 
        for j in range(1  , len(pos)):
            if pos[j]-prev >= i:
                prev = pos[j]
                c+=1
        if c < cnt:
            break
        else:
            ans = i
    return ans


# using Binary search 
# since we have the sorted array
'''
    Time Complexity: O(N * log(max))
    Space Complexity: O(1),

    where N is the total number of rooms and max is the maximum possible position for any room.

'''

def chessTournament(positions, n, c):

    # Sorting all positions of empty rooms.
    positions.sort()

    # l is the least possible answer and r is the max possible answer.
    ans = 0
    l = 1
    r = positions[n - 1]

    # We will find answer by using binary search.
    while (l <= r):

        # Lets check wether the allocation is possible for mid.
        mid = (l + r) // 2

        # previous_room stores the previous occupied empty room.
        count = 1
        previousRoom = positions[0]

        for i in range(1, n):

            # If the difference between current and previous room >= mid we will allocate it.
            if (positions[i] - previousRoom >= mid):
                count += 1
                previousRoom = positions[i]

        # Compressing length to right half if allocation is possible.
        if (count >= c):
            l = mid + 1
            ans = mid
        else:
            r = mid - 1

    # Return the variable ans
    return ans
