# Problem Statement

# https://www.geeksforgeeks.org/job-sequencing-problem/

# You are given a N x 2 2-D array 'Jobs' of 'N' jobs where Jobs[i][0] denote the deadline of i-th job
#  and Jobs[i][1] denotes the profit associated with i-th job.
# You will make a certain profit if you complete the job within the deadline associated with it.
#  Each job takes 1 unit of time to be completed, and you can schedule only 
# one job at a particular time.

#######################################Greedy Approach

# The idea here is to follow a greedy approach that we should complete the job with the maximum profit
#  in the nearest available slot within its deadline. So, we can sort the jobs in the decreasing order
#  of their profit, and we can maintain a boolean array to keep track of the available slots. So, for 
# each job, we traverse the array backward from the deadline associated with the job to 1, and if any 
# of the slots are empty, we add this profit to the answer, else we ignore this job.
 
# Algorithm
 
# Sort the jobs array in the descending order of the profit associated with each job. We can write our
#  own comparator function to achieve this.
# Create the variable, ‘maxProfit’, and Initialize it to 0.
# Create a variable ‘maxDeadline’ and find the maximum available deadline among all the jobs.
# Create a boolean array named slots of size ‘maxDeadline’ and initialize all the elements to false.
# Run a loop from i = 0 to N and do:
# Run a loop j = jobs[i].deadline to 1 and do:
#     If slots[j] == false, then
#         maxProfit = maxProfit + jobs[i].profit
#         Make slots[j] = true and break out of the loop.
# Return the maxProfit.

# Time Complexity

# O(N * maxDeadline), where ‘N’ denotes the number of elements of the array “jobs,” and ‘maxDeadline’ is 
# the maximum available deadline among all the jobs.
 
# As for every index of the array “jobs”, we may have to search for all the indices of the array “slots”. 
# Hence, the time complexity in the worst case will be O(N * maxDeadline).
# Space Complexity

# O(maxDeadline), where ‘maxDeadline’ is the maximum available deadline among all the jobs.
 
# The slots array/list has a size of maxDeadline.
'''
    Time Complexity - O(N * maxDeadline)
    Space Complexity - O(maxDeadline)

    Where N is size of the array "jobs" and maxDeadline is the maximum among all the deadlines.
'''

def jobScheduling(jobs):

    jobs.sort(key = lambda x: (-x[1], -x[0])) # 1 profit , 0 deadline
    maxProfit = 0
    maxDeadline = 0

    # Find the maximum deadline among all the jobs.
    for i in range(0, len(jobs)):
        maxDeadline = max(maxDeadline, jobs[i][0])
    
    # Create a slots list of size maxDeadline + 1.
    slots=[False] *(maxDeadline + 1)

    # Initialize the array to false initially.

    maxProfit = 0
    for i in range(len(jobs)):
        x = jobs[i][0] # deadline
        while x > 0:
            if slots[x] == False:
                maxProfit = maxProfit + jobs[i][1]
                slots[x] = True
                break
            x -= 1

    return maxProfit


###############################################################################################

# Using Set

# In the above approach, for each index in the jobs array, we may have to traverse a 
# boolean array of slots of size maxDeadline. However, we can optimize the above approach
#  by using a set and applying a binary search on the elements of the set. So, we store 
# the elements from maxDeadline to 1 in the set. We traverse the jobs array, and for each
#  job, we find the nearest element present in the set that is less than or equal to the 
# deadline of that job. If such an element exists in the set, then we add the profit to the 
# answer and remove this element from the set.

 
# Algorithm
 
# Sort the jobs array in the descending order of the profit associated with each job.
#  We can write our own comparator function to achieve this.
# Create two variables, maxProfit, and numberOfJobs. Initialize both of them to 0.
# Create a variable maxDeadline and find the maximum available deadline among all the jobs.
# Create a set named slots that store the elements in decreasing order. Insert all the elements
#  from maxDeadline to 1 into the set.
# Run a loop from i = 0 to N and do:
#     If the set is empty or jobs[i].deadline is less than the last element of the set, then we 
# ignore this job as it can’t be completed and continue in the loop.
#     Apply binary search on the set and find the nearest available slot that is less than or 
# equal to jobs[i].deadline. Let’s name this as availableSlot.
#     maxProfit = maxProfit + jobs[i].profit
#     Increment numberOfJobs by 1.
#     Remove the availableSlot from the set.
# Return the maxProfit and numberOfJobs.
 
# Note that, there is no in-built lower_bound or upper_bound function associated with the set
#  data structure in python. So, we can implement the above approach in python by using a segment tree.
# Time Complexity

# O(N *log max(N, maxDeadline)), where ‘N’ denotes the number of elements of the array “jobs,” and
#  ‘maxDeadline’ is the maximum available deadline among all the jobs.
 
# As for every index of the array “jobs”, we are applying binary search on a set of size maxDeadline.
#  We are also sorting the “jobs” array of size N according to the decreasing order of profit.
#  Hence, the time complexity will be O(N * log max(N, maxDeadline)).
# Space Complexity

# O(maxDeadline), where ‘maxDeadline’ is the maximum available deadline among all the jobs.
 
# The set has a size of ‘maxDeadline’.    

'''
    Time Complexity - O(N * log max(N, maxDeadline))
    Space Complexity - O(maxDeadline)

    Where N is size of the array "jobs" and maxDeadline is the maximum among all the deadlines.
'''

import bisect

def jobScheduling(jobs):

    jobs.sort(key = lambda x: (-x[1], -x[0]))
    maxProfit = 0
    maxDeadline = 0

    # Find the maximum deadline among all the jobs.
    for i in range(0, len(jobs)):
        maxDeadline = max(maxDeadline, jobs[i][0])

    slots = list()

    # Insert all the elements from maxDeadline to 1 into the list.
    for i in range(1, maxDeadline + 1):    
        slots.append(i)

    maxProfit = 0
    for i in range(len(jobs)):

        # If the set is empty or the deadline is less than the last element of the set, then ignore this job.
        if len(slots) == 0 or jobs[i][0] < slots[0]: #  # 1 profit , 0 deadline
            continue

        availableSlot = slots[bisect.bisect(slots, jobs[i][0]) - 1] # Rightmost index to insert, so list remains sorted is
        maxProfit += jobs[i][1]
        slots.remove(availableSlot)

    return maxProfit