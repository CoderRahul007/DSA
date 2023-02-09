# Aterp is the head nurse at a city hospital. City hospital contains R*C number of 
# wards and the structure of a hospital is in the form of a 2-D matrix.
# Given a matrix of dimension R*C where each cell in the matrix can have values
#  0, 1, or 2 which has the following meaning:
# 0: Empty ward
# 1: Cells have uninfected patients
# 2: Cells have infected patients

# An infected patient at ward [i,j] can infect other uninfected patient at 
# indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in 
# unit time. Help Aterp determine the minimum units of time after which there 
# won't remain any uninfected patient i.e all patients would be infected. 
# If all patients are not infected after infinite units of time then simply return -1.

 


# Example 1:

# Input:
# 3 5
# 2 1 0 2 1
# 1 0 1 2 1
# 1 0 0 2 1 
# Output:
# 2
# Explanation:
# Patients at positions {0,0}, {0, 3}, {1, 3}
# and {2, 3} will infect patient at {0, 1}, 
# {1, 0},{0, 4}, {1, 2}, {1, 4}, {2, 4} during 1st 
# unit time. And, during 2nd unit time, patient at 
# {1, 0} will get infected and will infect patient 
# at {2, 0}. Hence, total 2 unit of time is
# required to infect all patients.

# Example 2:

# Input:
# 3 5
# 2 1 0 2 1
# 0 0 1 2 1
# 1 0 0 2 1
# Output:
# -1
# Explanation:
# All patients will not be infected.
# BFS approach
class Solution:
    def helpaterp(self, hos):
        # code here
        q = []
        n , m = len(hos) , len(hos[0])
        
        for i in range(n):
            for j in range(m):
                if hos[i][j] == 2:
                    q.append([i , j])
        c = 0
        while q:
            loop = len(q)
            flag = 0
            for _ in range(loop):
                i , j = q.pop(0)
                if i-1 >= 0 and hos[i-1][j] == 1:
                    hos[i-1][j] = 2
                    q.append([i-1 , j])
                    flag = 1
                if i+1 < n and hos[i+1][j] == 1:
                    hos[i+1][j] = 2
                    q.append([i+1 , j])
                    flag = 1
                if j-1 >= 0 and hos[i][j-1]==1:
                    hos[i][j-1]=2
                    q.append([i,j-1])
                    flag=1
                if j+1 < m and hos[i][j+1]==1:
                    hos[i][j+1]=2
                    q.append([i,j+1])
                    flag=1
            if flag:
                c +=1
        for i in range(n):
            for j in range(m):
                if hos[i][j] == 1:
                    return -1
        return c
        