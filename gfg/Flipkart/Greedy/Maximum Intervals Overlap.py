# Consider a big party where N guests came to it and a log register for 
# guest’s entry and exit times was maintained. Find the minimum time at 
# which there were maximum guests at the party. Note that entries in the 
# register are not in any order.

# Note: Guests are leaving after the exit times.

# Example 1:

# Input:
# N = 5
# Entry= {1, 2,10, 5, 5}
# Exit = {4, 5, 12, 9, 12}
# Output: 3 5
# Explanation: At time 5 there were 
#              guest number 2, 4 and 5 present.

# Example 2:

# Input:
# N = 7
# Entry= {13, 28, 29, 14, 40, 17, 3}
# Exit = {107, 95, 111, 105, 70, 127, 74}
# Output: 7 40
# Explanation: At time 40 there were 
#              all 7 guests present in the party.


class Solution:

    def findMaxGuests(self, entry, exit, N):
        # code here
            entry.sort()
            exit.sort()
           
            i = 0
            j = 0
            res = 1
            curr = 0
           
            minTime = entry[0]
       
            while i < N and j < N:
                if entry[i] <= exit[j]: # means number of people entered before exit time is less so at that time all are present so ++s
                   curr +=1
                   i+=1
                else:
                    curr -=1 #means they have exited so --
                    j +=1
                if curr > res:
                    res = curr
                    minTime = entry[i-1]
            
            return [res , minTime]        