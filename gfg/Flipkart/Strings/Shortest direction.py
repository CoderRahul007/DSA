class Solution:
    def shortestPath(self, s):
        # code here
        x = 0
        y = 0
        ans = ""
        for i in s:
            if i == "E":
                x+=1
            elif i == "N":
                y+=1
            elif i == "S":
                y-=1
            elif i == "W":
                x-=1
        while x or y:
            if x > 0:
                ans+= "E"
                x-=1
            elif y > 0:
                ans+= "N"
                y-=1
            elif y < 0:
                ans+= "S"


# A person wants to go from origin to a particular location, 
# he can move in only 4 directions(i.e East, West, North, South) 
# but his friend gave him a long route, help a person to find minimum 
# Moves so that he can reach to the destination.

# Note: You need to print the lexicographically sorted string.
#  Assume the string will have only ‘E’ ‘N’ ‘S’ ‘W’ characters.

# Example 1:

# Input:
# S = "SSSNEEEW"
# Output: EESS
# Explanation: Following the path SSSNEEEW
# and EESS gets you at the same final point.
# There's no shorter path possible.

# â€‹Example 2:

# Input: 
# S = "NESNWES"
# Output: E
# Explanation: Following the path NESNWES
# and E gets you at the same final point.
# There's no shorter path possible.
