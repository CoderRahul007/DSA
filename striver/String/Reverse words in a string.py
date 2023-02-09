'''
    Time Complexity  = O(N)
    Space Complexity = O(N)

    Where N is the length of the string
'''

def reverseString(str):

    if (len(str)==0):
        return str

    ans=""

    # If the string is " " then return ""
    if (len(str) == 1 and str[0] == ' '):
        return ans

    start = len(str) - 1

    while (start >= 0):

        # Skip multiple spaces
        if (str[start] == ' '):
            start-=1

        else:

            # Add space between words
            if (len(ans) > 0):
                ans += " "

            j = start

            # Loop for extracting word
            while (j >= 0 and str[j] != ' '):
                j-=1

            # Add current word to ans
            ans += str[j + 1 : start + 1]
            start = j

    return ans
