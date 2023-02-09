# https://www.codingninjas.com/codestudio/problems/ayush-gives-ninjatest_1097574?topList=striver-sde-sheet-problems&leftPanelTab=0



########################################################################################################################################
# Brute force.
# The answer could be between maximum of all available time  and the sum of the time required to study all chapters. 
# So in this solution we have all the possible answers and let’s say we are at X so we want to find whether X can be the maximum time of a day Ayush studies or not.
# We also want to allocate chapters sequentially so we will keep track of the chapters using currentChapter 
# variable which would be initialized with 1 as we are on the first chapter at the beginning.
# Now we will iterate through all the days and try to allocate as many chapters in a day as possible with the 
# total time required to study them as less than or equal to X.
# If we can cover all the chapters in N days using the above rule then we will say that it is possible for X to 
# be the answer we will return X because it would also be the minimum possible

# Time Complexity

# O(K * M), where ‘K’ is the sum of the time required to read all the chapters and ‘M’ is the number of chapters.

# Because for all the possible values of answer from 1 - K, we are iterating through all the chapters that are to be studied.
# Space Complexity

# O(1).

'''
    Time Complexity: O(K * M)
    Space complexity: O(1),

    where 'K' is the sum of the time required to study all the chapters 
    and 'M' is the number of chapters.
'''

def ayushGivesNinjatest(n, m, time):
    
    s = sum(time)
    maxTime = max(time)
    
    # We will iterate through all the possible values of answer.
    for i in range (maxTime, s + 1):
        
        days = 1
        currentTime = 0
        
        for j in range (len(time)):
            currentTime += time[j]
            if currentTime > i:
                days += 1 # next day
                currentTime = time[j]
                
        # If the days required to study all the chaptes is less than or equal to n than answer is possible and we will return it.
        if days <= n:
            return i
        
    return -1

####################################################################################################################################

# Binary search

# We know that our answer could be between maximum of all available time and the sum of time required 
# to study all the chapters.
#  Now we will use binary search to find the answer. We will set 1 as the minimum possible answer and  
# sum as the maximum possible answer.
# Now we will find for some X equal to the mid value of maximum and minimum possible answer.
# Let's find out whether X is a possible answer or not or we can say whether there is sum allocation 
# where X is the maximum possible time of a day.
#     We want to allocate chapters sequentially so we will keep track of the chapters using currentChapter
#  variable which would 
#     be initialized with 1 as we are on the first chapter at the beginning.
#     Now we will iterate through all the days and try to allocate as many chapters in a day as possible
#  with the total time 
#     required to study them as less than or equal to X.
#     If we can cover all the chapters in N days using the above rule then we will say that it is possible 
# for X to be the answer.
# If X is a possible answer then we will compress our range to the right hand side i.e, we will search 
# on X - max possible answer.
# If X is not possible answer then we will compress our range to the left hand side i.e, we will search
#  on min possible answer - X.
# By doing this or range becomes smaller and smaller and when it becomes equal to 1 we will return that
#  as an answer.

 
# Time Complexity

# O(M * log(K)), where ‘M’ is the number of chapters and ‘K’ is the sum of time required to study all the chapters.

 

# Because by doing binary search we will calculate the possible answer only log(max) times and in each possible 
# answer we have to traverse all the chapters so the complexity is N * log(max).
# Space Complexity

# O(1).

'''
    Time Complexity: O(M * log(K))
    Space complexity: O(1),

    where 'K' is the sum of the time required to study all the chapters 
    and 'M' is the number of chapters.
'''

def ayushGivesNinjatest(n, m, time):
    
    s = sum(time)
    maxTime = max(time)
    
    # We will initialize the lower limit of binary search
    #  l with maxTime and the upper limit of binary search with sum.
    l = maxTime
    r = s
    answer = s
    
    while l <= r:
        mid = (l + r) // 2
        
        days = 1
        currentTime = 0
                
        for j in range (len(time)):
            currentTime += time[j]
            if currentTime > mid:
                days += 1
                currentTime = time[j]
                
        '''
            If the days required to study all the chaptes is greater than n than answer is not possible
            and we want more time to study in a given day so we will compress the range to the right hand side.
            Else we can study all the chapters and we will update the answer with mid.
        '''
        if days <= n:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1
        
    return answer