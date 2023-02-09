# Given a set of N jobs where each jobi has a deadline and profit associated with it.

# Each job takes 1 unit of time to complete and only one job can be scheduled at a time.
#  We earn the profit associated with job if and only if the job is completed by its deadline.

# Find the number of jobs done and the maximum profit.

# Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job.


# Example 1:

# Input:
# N = 4
# Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
# Output:
# 2 60
# Explanation:
# Job1 and Job3 can be done with
# maximum profit of 60 (20+40).

# Example 2:

# Input:
# N = 5
# Jobs = {(1,2,100),(2,1,19),(3,2,27),
#         (4,1,25),(5,1,15)}
# Output:
# 2 127
# Explanation:
# 2 jobs can be done with
# maximum profit of 127 (100+27).


# class Solution:
    
#     #Function to find the maximum profit and the number of jobs done.
#     def JobScheduling(self,Jobs,n):
        
#         Jobs.sort(key=lambda x: x.profit, reverse=True)
#         done = [False]*n
#         day = 0
#         profit = 0
#         for i in range(n):
#             for j in range(min(n-1 , Jobs[i].deadline-1) , -1  , -1):
#                 if not done[j]:
#                     day +=1
#                     profit += Jobs[i].profit
#                     done[j] = True
#                     break
#         return [day , profit]

##################################################################################
# It can be optimized using Priority Queue(max heap).

 

# The algorithm goes as follow:

 

# Sort the jobs based on their deadlines.
# Iterate from the end and calculate the available slots between every two consecutive deadlines. 
# Include the profit, deadline, and job ID of ith job in the max heap.
# While the slots are available and there are jobs left in the max heap,
#  include the job ID with maximum profit and deadline in the result.
# Sort the result array based on their deadlines.

 

# Here is the implementation of the above algorithm.

 

# Program to find the maximum profit
# job sequence from a given array
# of jobs with deadlines and profits
import heapq
 
 
def printJobScheduling(arr):
    n = len(arr)
 
    # arr[i][0] = job_id, arr[i][1] = deadline, arr[i][2] = profit
 
    # sorting the array on the
    # basis of their deadlines
    arr.sort(key=lambda x: x[1])
    print(arr)
    # initialise the result array and maxHeap
    result = []
    maxHeap = []
 
    # starting the iteration from the end
    for i in range(n - 1, -1, -1):
 
        # calculate slots between two deadlines
        if i == 0:
            slots_available = arr[i][1]
        else:
            slots_available = arr[i][1] - arr[i - 1][1]
        
        print( "slots_available " ,slots_available)
        print("arr[i][1] " ,arr[i][1])
        print(" arr[i-1][1]" ,arr[i-1][1])
 
        # include the profit of job(as priority), deadline
        # and job_id in maxHeap
        # note we push negative value in maxHeap to convert
        # min heap to max heap in python
        heapq.heappush(maxHeap, (-arr[i][2], arr[i][1], arr[i][0]))
 
        while slots_available and maxHeap:
 
            # get the job with max_profit
            profit, deadline, job_id = heapq.heappop(maxHeap)
 
            # reduce the slots
            slots_available -= 1
 
            # include the job in the result array
            result.append([job_id, deadline])
 
    # jobs included might be shuffled
    # sort the result array by their deadlines
    result.sort(key=lambda x: x[1])
 
    for job in result:
        print(job[0], end=" ")
    print()
 
 
# Driver COde
arr = [['a', 2, 100],  # Job Array
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]
 
print("Following is maximum profit sequence of jobs")
 
# Function Call
printJobScheduling(arr)
 

# Output

# Following is maximum profit sequence of jobs
# a c e 

# Time complexity : O(nlog(n))

# Space complexity : O(n)        

# Explanation of the second solution and implementation in C++:
# We first sort the jobs in decreasing order of their deadline

# Say we have 2 jobs A and B with
# A.dead < B.dead
# 1 2
# Then it is obvious that job B must be done no matter what is profit is as it's execution is not occupying the other job.

# Consider with 3 jobs A, B and C
# A.dead < B.dead == C.dead == D.dead
# 1 2 2 2

# Then among B, C and D , We must execute the job with more profit, that is why a Max Heap is used to store jobs (based on profit) in a buffer.

# For eg. Consider 4 Jobs (sorted in descending order of Deadline)-

# JobId Dead Profit
# 1 4 20
# 2 1 10
# 3 1 40
# 4 1 30

# i = 0

# avail_slot = JobID-1.Dead - JobID-2.Dead = 3
# Meaning 3 slots are left that are 2, 3 and 4 that we can do the Job 4 in, slot 1 can be used by Job2.

# We push the Job in maxHeap and check whether slots are left (It basically means is there time available to execute the jobs) and their are Jobs in the Max Heap that needs execution.
# And then we execute the Jobs in Max heap till either no slots are left or No jobs are left in heap.

# CODE : https://ide.geeksforgeeks.o...


# bool cmp(Job &A,Job &B){
# return A.dead > B.dead;
# }
# struct heapCmp{
# bool operator() (const Job &A,const Job &B){
# return A.profit < B.profit;
# }
# };

# class Solution
# {
# public:
# //Function to find the maximum profit and the number of jobs done.
# vector<int> JobScheduling(Job arr[], int n)
# {
# // your code here
# sort(arr,arr+n,cmp);

# priority_queue <job, vector="" <job="">, heapCmp> mxHeap;

# int profit = 0, jobs = 0;
# for(int i=0;i<n;i++){ int="" avail_slot="i==n-1" ?="" arr[i].dead="" :="" arr[i].dead="" -="" arr[i+1].dead;="" mxheap.push(arr[i]);="" while(avail_slot="" &&="" !mxheap.empty()){="" avail_slot--;="" job="" top="mxHeap.top();" mxheap.pop();="" profit="" +="top.profit;" jobs++;="" }="" }="" return="" {jobs,="" profit};="" }="" };="" <="" code="">            