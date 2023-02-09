# Power Set: Power set P(S) of a set S is the set of all subsets of S. 
# For example S = {a, b, c} then P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}.
# If S has n elements in it then P(s) will have 2n elements

# Example: 

# Set  = [a,b,c]
# power_set_size = pow(2, 3) = 8
# Run for binary counter = 000 to 111

# Value of Counter            Subset
#    000                    -> Empty set
#    001                    -> a
#    010                    -> b
#    011                    -> ab
#    100                    -> c
#    101                    -> ac
#    110                    -> bc
#    111                    -> abc

# Recommended PracticePower SetTry It!
# Algorithm: 

# Input: Set[], set_size
# 1. Get the size of power set
#       powet_set_size = pow(2, set_size)
# 2  Loop for counter from 0 to pow_set_size
#     (a) Loop for i = 0 to set_size
#          (i) If ith bit in counter is set
#                 Print ith element from set for this subset
#    (b) Print separator for subsets i.e., newline

# Method 1:
# For a given set[] S, the power set can be found by generating all binary numbers between 0 and 2n-1, where n is the size of the set. 
# For example, for the set S {x, y, z}, generate all binary numbers from 0 to 23-1 and for each generated number, the corresponding set can be found by considering set bits in the number.

# Below is the implementation of the above approach.


# python3 program for power set
 
import math;
 
def printPowerSet(set,set_size):
     
    # set_size of power set of a set
    # with set_size n is (2**n -1)
    pow_set_size = (int) (math.pow(2, set_size))
    counter = 0
    j = 0
     
    # Run from counter 000..0 to 111..1
    for counter in range(0, pow_set_size):
        for j in range(0, set_size):
             
            # Check if jth bit in the
            # counter is set If set then
            # print jth element from set
            if((counter & (1 << j)) > 0):
                print(set[j], end = "")
        print("")
 
# Driver program to test printPowerSet
set = ['a', 'b', 'c'];
printPowerSet(set, 3);
 
# This code is contributed by mits.
# Output
# a
# b
# ab
# c
# ac
# bc
# abc
# Time Complexity: O(n2n)
# Auxiliary Space: O(1)

# Method 2: (sorted by cardinality)

# In auxiliary array of bool set all elements to 0. 
# That represent an empty set. Set first element of auxiliary 
# array to 1 and generate all permutations to produce all subsets
#  with one element. Then set the second element to 1 which will 
#  produce all subsets with two elements, repeat until all elements are included.




# // C++ program for the above approach
# #include <bits/stdc++.h>
# using namespace std;
 
# // Function to print all the power set
# void printPowerSet(char set[], int n)
# {
#     bool *contain = new bool[n]{0};
     
#     // Empty subset
#     cout << "" << endl;
#     for(int i = 0; i < n; i++)
#     {
#         contain[i] = 1;
#         // All permutation
#         do
#         {
#             for(int j = 0; j < n; j++)
#                 if(contain[j])
#                     cout << set[j];
#             cout << endl;
#         } while(prev_permutation(contain, contain + n));
#     }
# }
 
# /*Driver code*/
# int main()
# {
#     char set[] = {'a','b','c'};
#     printPowerSet(set, 3);
#     return 0;
# }
 

# Output
# a
# b
# c
# ab
# ac
# bc
# abc
# Time Complexity: O(n2n)
# Auxiliary Space: O(n)

# Method 3: 
# This method is specific to the python programming language.
#  We can iterate a loop over 0 to the length of the set to
#   obtain and generate all possible combinations of that string 
#   with the iterable length. The program below will give the implementation of the above idea. 
 

# Below is the implementation of the above approach.


#Python program to find powerset
from itertools import combinations
def print_powerset(string):
    for i in range(0,len(string)+1):
        for element in combinations(string,i):
            print(''.join(element))
string=['a','b','c']
print_powerset(string)


#######################################################################################

# The problem is very similar to the 0/1 knapsack problem, where for each 
# element in set S, we have two options:

# Consider that element.
# Don’t consider that element.
# The following solution generates all combinations of subsets using the above
#  logic. To print only distinct subsets, initially sort the subset and exclude
#   all adjacent duplicate elements from the subset along with the current element
#    in case 2. This is demonstrated below in C++, Java, and Python:


from collections import deque
 
 
# Recursive function to print all distinct subsets of `S`.
# `S`   ——> input set
# `i`   ——> index of next element in set `S` to be processed
# `out` ——> list to store elements of a subset
def printPowerSet(S, i, out=deque()):
 
    # if all elements are processed, print the current subset
    if i < 0:
        print(list(out))
        return
 
    # include the current element in the current subset and recur
    out.append(S[i])
    printPowerSet(S, i - 1, out)
 
    # backtrack: exclude the current element from the current subset
    out.pop()
 
    # remove adjacent duplicate elements
    while i > 0 and S[i] == S[i - 1]:
        i = i - 1
 
    # exclude the current element from the current subset and recur
    printPowerSet(S, i - 1, out)
 
 
# Wrapper over `printPowerSet()` function
def findPowerSet(S):
 
    # sort the set
    S.sort()
 
    # print the power set
    printPowerSet(S, len(S) - 1)
 
 
if __name__ == '__main__':
 
    S = [1, 3, 1]
 
    findPowerSet(S)
 
# Download  Run Code

# Output:

# [3, 1, 1]
# [3, 1]
# [3]
# [1, 1]
# [1]
# []
# The time complexity of the above solution is O(n.2n), where n is the size of the given set.

# Approach 2
# For a given set S, the power set can be found by generating all binary numbers between 0 and 2n-1, where n is the size of the set. For example, for set S {x, y, z}, generate binary numbers from 0 to 23-1 and for each number generated, the corresponding set can be found by considering set bits in the number.


# 0 = 000 = {}
# 1 = 001 = {z}
# 2 = 010 = {y}
# 3 = 011 = {y, z}
# 4 = 100 = {x}
# 5 = 101 = {x, z}
# 6 = 110 = {x, y}
# 7 = 111 = {x, y, z}

# To avoid printing duplicates subsets, initially sort the set.
#  Also, insert each subset into the set. As the set maintains all 
#  distinct combinations, we will have unique subsets into the set. 
#  Following is the C++, Java, and Python program that demonstrates it:


# Iterative function to print all distinct subsets of `S`
def findPowerSet(S):
 
    # `N` stores the total number of subsets
    N = int(pow(2, len(S)))
    s = set()
 
    # sort the set
    S.sort()
 
    # generate each subset one by one
    for i in range(N):
        subset = []
        # check every bit of `i`
        for j in range(len(S)):
            # if j'th bit of `i` is set, append `S[j]` to the subset
            if i & (1 << j):
                subset.append(S[j])
 
        # insert the subset into the set
        s.add(tuple(subset))
 
    # print all subsets present in the set
    print(s)
 
 
if __name__ == '__main__':
 
    S = [1, 2, 1]
    findPowerSet(S)
 
