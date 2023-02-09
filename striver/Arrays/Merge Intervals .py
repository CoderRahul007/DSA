# Problem Statement
# You are given N number of intervals, where each interval contains two integers denoting the start time and
#  the end time for the interval.
# The task is to merge all the overlapping intervals and return the list of merged intervals sorted by 
# increasing order of their start time.
# Two intervals [A,B] and [C,D] are said to be overlapping with each other if there is at least one integer 
# that is covered by both of them.
# For example:

# For the given 5 intervals - [1, 4], [3, 5], [6, 8], [10, 12], [8, 9].

# Since intervals [1, 4] and [3, 5] overlap with each other, we will merge them into a single interval as [1, 5].

# Similarly, [6, 8] and [8, 9] overlap, merge them into [6,9].

# Interval [10, 12] does not overlap with any interval.

# Final List after merging overlapping intervals: [1, 5], [6, 9], [10, 12].

def mergeIntervals(intervals):
    # Write your code here.
    res=[]
    intervals.sort(key = lambda x: x.start)
    res.append(intervals[0])
    j=0
    for i in range(len(intervals)):
        if intervals[i].start <= res[j].end: # if next  element start is less than previpus one end  then its a overlapping
            res[j].end=max(intervals[i].end,res[j].end) # the end will be maxium of ends of these two
        else:
            res.append(intervals[i]) # else push it
            j+=1
    return res

# O(nlogn)