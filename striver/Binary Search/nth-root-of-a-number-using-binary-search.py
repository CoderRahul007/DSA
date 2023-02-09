
def power(mid , n):
    ans = 1
    while n > 1:
        if n & 1: # odd
            ans *= mid
            n-=1
        m = mid * mid
        n = n/2
    return ans

def nthRoot( n , m):
    eps = 1e-7
    low = 1
    high = m
    while high -low > eps:
        mid = (low + high)/2
        if power(mid , n) > m:
            high = mid
        else:
            low = mid
    return low






# Time Complexity

# O( log(N) * log(M) ), Where ‘N’ and ‘M’ are input integers.

# In the above algorithm, the search space is ‘M’, and hence in ‘log(M)’ iterations we 
# will find the ‘N’th root, and in each iteration, we find the ‘N’th power of ‘MIDDLE’
#  using binary exponentiation which takes ‘log( N )’ iterations, thus in total ‘log(N)*log(M)’ iterations. 

# Hence the time complexity will be O( log(N) * log(M) )