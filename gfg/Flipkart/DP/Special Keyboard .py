# Imagine you have a special keyboard with the following keys: 

# Key 1:  Prints 'A' on screen
# Key 2: (Ctrl-A): Select screen
# Key 3: (Ctrl-C): Copy selection to buffer
# Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

# Find maximum numbers of A's that can be produced by pressing keys on the special keyboard N times. 


# Example 1:

# Input: N = 3
# Output: 3
# Explaination: Press key 1 three times.


# Example 2:

# Input: N = 7
# Output: 9
# Explaination: The best key sequence is 
# key 1, key 1, key 1, key 2, key 3,
# key4, key 4.

# https://www.youtube.com/watch?v=nyR8K63F2KY
# F(N) = { F(N) if N <= 6
#         ,
#         max( 2F(N-3) , 3F(N-4) , 4F(N-5) , 5F(N-6)  , ... F(1))
#         }

class Solution:
    def optimalKeys(self, N):
        # code here
        if N <= 6:
           return N
        dp = [i if i<=6 else 0 for i in range(N+1)]
        for i in range(7, N+1):
            c = 2
            for j in range(i-3, 0, -1):
                if dp[j]*c >= dp[i]:
                    dp[i] = dp[j]*c
                else:
                    break
                c += 1
        return dp[N]