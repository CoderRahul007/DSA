# Suppose there is a circle. There are N petrol pumps on that circle. You will be given two sets of data.
# 1. The amount of petrol that every petrol pump has.
# 2. Distance from that petrol pump to the next petrol pump.
# Find a starting point where the truck can start to get through the complete 
# circle without exhausting its petrol in between.
# Note :  Assume for 1 litre petrol, the truck can go 1 unit of distance.

# Example 1:

# Input:
# N = 4
# Petrol = 4 6 7 4
# Distance = 6 5 3 5
# Output: 1
# Explanation: There are 4 petrol pumps with
# amount of petrol and distance to next
# petrol pump value pairs as {4, 6}, {6, 5},
# {7, 3} and {4, 5}. The first point from
# where truck can make a circular tour is
# 2nd petrol pump. Output in this case is 1
# (index of 2nd petrol pump).

class Solution:
    
    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self,lis, n):
        #Code here
        kami = 0 # to store petrol deficiency, - values while traveling  
        bal = 0 # to store balance after reaching to next petrol pump
        start = 0
        for i , tup in enumerate(lis):
            bal += tup[0] - tup[1] # calculate balance for each 
            if bal < 0:  # if -ve then 
                kami += bal  # store it in kami, as this is petrol deficiency to reach next petrol pump
                start = i+1 # update start to just next petrol pump, (like front+1)
                bal = 0 # update bal to 0, as we are going to start from another node
        if kami + bal > 0:  # kami + bal > 0 mean traversal is possible 
            return start
        return -1
