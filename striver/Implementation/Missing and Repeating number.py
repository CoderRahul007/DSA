# https://takeuforward.org/data-structure/find-the-repeating-and-missing-numbers/

#  You are given a read-only array of N integers with values also in the range
#  [1,N] both inclusive. Each integer appears exactly once except A which appears
#  twice and B which is missing. The task is to find the repeating and missing
#  numbers A and B where A repeats twice and B is missing.

# Example 1:

# Input Format:  array[] = {3,1,2,5,3}

# Result: {3,4)

# Explanation: A = 3 , B = 4 
# Since 3 is appearing twice and 4 is missing

def findTwoElement( self,arr, n): 
    # code here
    l = [0]*(n+1)
    for i in arr:
        l[i] +=1
        
    re = 0
    mis = 0
    for i in range(len(l)):
        if l[i] > 1:
            re = i
        if l[i] == 0:
            mis = i
    return [re , mis]


# Now since the numbers are from 1 to N in the array arr[].
#  Let’s calculate sum of all integers from 1 to N and sum of
#  squares of all integers from 1 to N. These can easily be done 
# using mathematical formulae.

# Therefore,

# Sum of all elements from 1 to N:

# S = N*(N+1)/2 ---- equation 1

# And, Sum of squares of all elements from 1 to N:

# P = N(N+1)(2N+1)/6. ----- equation 2

# Similarly, find the sum of all elements of the array and sum of 
# squares of all elements of the array respectively.

#     s1 = Sum of all elements of the array. —– equation 3
#     P1 = Sum of squares of all elements of the array. ——– equation 4

# Now, if we subtract the sum of all elements of array from sum of 
# all elements from 1 to N, that should give us the value for (X – Y).

# Therefore,

# (X-Y) = s – s1 = s’

# Similarily,

# X^2 – Y^2 = P – P1 = P’

# or, (X + Y)(X – Y) = P’

# or, (X + Y)*s’ = P’

# or, X + Y = P’/s’

# Great,

# we have the two equations we needed:

# (X – Y) = s’

# (X + Y) = P’/s’

# X = (s’ + P’/s’)/2 (missing)
# Y = X - s’ (repeating)

# We can use the two equations to solve and find values for X and Y respectively.

# vector<int>missing_repeated_number(const vector<int> &A) {
#     long long int len = A.size();

#     long long int S = (len * (len+1) ) /2;
#     long long int P = (len * (len +1) *(2*len +1) )/6;
#     long long int missingNumber = 0, repeating = 0;
     
#     for(int i=0;i<A.size(); i++){
#        S -= (long long int)A[i];
#        P -= (long long int)A[i]*(long long int)A[i];
#     }
     
#     missingNumber = (S + P/S)/2;

#     repeating = missingNumber - S;

#     vector <int> ans;

#     ans.push_back(repeating);
#     ans.push_back(missingNumber);

#     return ans;
# }