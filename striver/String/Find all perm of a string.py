"""

    Time Complexity: O(N*N!). Note that there are n! permutations and it requires O(n) time to print a permutation.
    Space Complexity: O(N).

    Where N is the length of the input string.

"""

def findPermutationsHelper(lst, i, n, ans):
    if (i >= n):
        # Storing the string in the vector ans.
        permutation = ""

        for k in range(len(lst)):
            permutation += (lst[k])  

        ans.append(permutation)
        return

    # Fixing a character at index i and then swapping with characters from index i to
    #  n and by this way building up permutation strings.
    for k in range(i,n+1):        
        lst[i] , lst[k] = lst[k] , lst[i]

        findPermutationsHelper(lst, i + 1, n, ans)
        
        lst[i] , lst[k] = lst[k] , lst[i]
    

def findPermutations(s):
    # Declaring a vector of string to store all the possible permutations of the string.
    ans = []
    lst = list(s)
    # Calling the user defined function which stores all the possible permutations of the string in the vector ans.
    findPermutationsHelper(lst, 0, len(lst) - 1, ans)
    return ans
