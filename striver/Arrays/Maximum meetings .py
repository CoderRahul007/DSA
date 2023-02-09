# Problem Statement
# You are given the schedule of N meetings with their start time Start[i] and end time End[i]. 
# But you have only 1 meeting room. So, you need to tell the meeting numbers you can organize 
# in the given room, such that the number of meetings organized is maximum.
# Note:

# The start time of one chosen meeting can’t be equal to the end time of the other chosen meeting.
#  Also for the same end time, a meeting with a smaller index is preferred. 

def maximumMeetings(start, end):
    # Write your Code here.
    t = []
    n = len(start)
    for i in range(n):
        t.append([start[i] , end[i] , i+1])
    t.sort(key = lambda x: x[1])
    ans = []
    ans.append(t[0][2])
    limit = t[0][1]
    for i in range(1 , n):
        if limit < t[i][0]:
            ans.append(t[i][2])
            limit = t[i][1]
    return ans

# T - nlogn    
    
    