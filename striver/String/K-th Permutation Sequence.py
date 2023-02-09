# 60. Permutation Sequence

################################################################33333
# Naive
#  Naive Approach

# Naively we will generate all permutations of sequence 1 to ‘N’ and store them in an array.
#  We will use recursion to generate all permutations.
 
# Here is the algorithm:
 
# We will call a void function permutate. The permutate function will work as follows (here ‘s’ and ‘ans’ denotes the string we passed to the function and the string we are generating, respectively):
#     If s.length() == 0 (Base Case)
#         Push the string ‘ans’ into the array where all permutations will be stored.
#     We run a for loop from i = 0 to s.length():
#         Do a recursive call by removing i-th character from ‘s’ and adding it to ‘ans’.
# Finally, return the K-th element of the array.

# Time Complexity

# O(N!), where ‘N’ is the length of each string. 

 
# There are a total N! permutations and to generate them we need O(N!) time.
# Space Complexity

# O(N!), where ‘N’ is the length of each string.

# import java.util.*;
# public class Main {
#     static void swap(char s[], int i, int j) {
#         char ch = s[i];
#         s[i] = s[j];
#         s[j] = ch;
#     }
#     static void permutationHelper(char s[], int index, ArrayList < String > res) {
#         if (index == s.length) {
#             String str = new String(s);

#             res.add(str);
#             return;
#         }
#         for (int i = index; i < s.length; i++) {
#             swap(s, i, index);
#             permutationHelper(s, index + 1, res);
#             swap(s, i, index);
#         }
#     }

#     static String getPermutation(int n, int k) {
#         String s = "";
#         ArrayList < String > res = new ArrayList < > ();
#         for (int i = 1; i <= n; i++) {
#             s += i;
#         }
#         permutationHelper(s.toCharArray(), 0, res);
#         Collections.sort(res);

#         return res.get(k);

#     }
#     public static void main(String args[]) {
#         int n = 3, k = 3;
#         String ans = getPermutation(n, k);
#         System.out.println("The Kth permutation sequence is " + ans);
#     }
# }
# Output:

# The Kth permutation sequence is 213

# Time complexity: O(N! * N) +O(N! Log N!)

# Reason:  The recursion takes O(N!)  time because we generate every possible permutation and
#  another O(N)  time is required to make a deep copy and store every sequence in the data structure.
#  Also, O(N! Log N!)  time required to sort the data structure

# Space complexity: O(N) 

# Reason: Result stored in a vector, we are auxiliary space taken by recursion

'''
    Time Complexity: O(N!)
    Space Complexity: O(N!)

    where N is the given integer.
'''


def permutate(s, ans, res):

    # Base case.
    if(len(s) == 0):
        res.append(ans)
        return

    for i in range(len(s)):

        # Append character in the ans.
        ans += s[i]

        # Generate all permutation with remaining character.
        permutate(s[0 : i] + s[i + 1 :], ans, res)

        # Remove the last character from the ans.
        ans  = ans[:len(ans) - 1]

def kthPermutation(n, k):

    res = []
    s = ""

    # generate number from 1 to n eg n = 3 , 123
    for i in range(1, n + 1):
        s += str(i)

    permutate(s, "", res)

    return res[k - 1]

#######################################################################
#########################################################################
# Optimised Approach

# explanation 
# https://takeuforward.org/data-structure/find-k-th-permutation-sequence/

def getPermutation(self, n: int, k: int) -> str:
		#Function to compute factorial
        def factorial(z):
            y = 1
            for i in range(1,z+1):
                y *= i
            return y
			
        #list of numbers 1 to n that we pull from
        nums = [str(i) for i in range(1, n+1)] # n = 3 , 1 , 2 , 3     # generate number from 1 to n eg n = 3 , 123
		
		#set k to k-1 for 0 indexing
        k -= 1
		
		#initialize our result
        res = ''
        
		#repeat the process until there are no more digits remaining to use
        while nums:
		
			#calculate factorial of remaining len(nums) - 1
            f = factorial(len(nums)-1)
			
			#find index in nums to use as next digit
            idx = k//f
			
			#remove this digit from nums and add it to the result
            res += nums.pop(idx)
			
			#update k for the next loop through
            k = k % f
            
        return res

# Time Complexity: O(N) * O(N) = O(N^2)

# Reason: We are placing N numbers in N positions. This will take O(N) time. 
# For every number, we are reducing the search space by removing the element 
# already placed in the previous step. This takes another O(N) time.

# Space Complexity: O(N) 

# Reason: We are storing  the numbers in a data structure(here vector)

