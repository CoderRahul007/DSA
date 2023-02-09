# Recursive Approach

# The key idea is to follow the rules of roman numbers which are as follows:

# The roman digits I, X and C are repeated up to three times in succession to form the numbers.
# When a digit of lower value is written to the right or after a digit of higher value, the values of all the digits are added.
# When a digit of lower value is written to the left or before a digit of higher value, then the value of the lower digit is
# subtracted from the value of the digit of higher value.
# If we have to write the numbers beyond 10 we should write the number 10 or groups of number 10 and then number 1 or 5 as 
# the case may be. Then these numbers are used to change to the corresponding Roman numerals.
# Keeping the above example in mind, we can write the following recursive solution:
 
# We take a recursive approach to solve the problem.
# We make a hash map ‘conv’ which stores integer values of special roman numbers.
# Then, we take the first 2 characters and check if they are in the map, if yes we add their value and recursively call the rest of the string.
# If the first 2 characters are not there in the map, we add the value of 1 character and recursively call the rest of the string.
# The base case will be once we have a string of size 1 or an empty string. In that case, we return 0.

# Time Complexity

# O(N), Where ‘N’ denotes the length of the string.

# Since we traverse the string once to find the integer value.
# Space Complexity

# O(N), Where ‘N’ denotes the length of the string.

'''

    Time Complexity     :   O(N)
    Space Complexity    :   O(N)

    Where 'N' is the length of the string.
    
'''

def romanToIntHelper(s, conv):

    # If single character, return the integer value of that character.
    if(len(s) <= 1):
        return conv[s]

    # Take first 2 characters.
    firstTwo = s[0:2]

    # If the first 2 characters are in the dict 'conv', add their value and check rest of the string.
    if(firstTwo in conv):
        return conv[firstTwo] + romanToIntHelper(s[2:], conv)

    # Otherwise take one charecter and check its value.
    else:
        firstOne = s[0]
        return conv[firstOne] + romanToIntHelper(s[1:], conv)


def romanToInt(s):
    conv = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1,
            "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900, "": 0}
            
    return romanToIntHelper(s, conv)



###########################################################
# Iterative

# The key idea is to follow the rules of roman numbers which are as follows:

# The roman digits I, X and C are repeated up to three times in succession to form the numbers.
# When a digit of lower value is written to the right or after a digit of higher value, the values of all the digits are added.
# When a digit of lower value is written to the left or before a digit of higher value, then the value of the lower digit is
#  subtracted from the value of the digit of higher value.
# If we have to write the numbers beyond 10 we should write the number 10 or groups of number 10 and then number 1 or 5 as
#  the case may be. Then these numbers are used to change to the corresponding Roman numerals.

 

# Keeping the above example in mind, we can proceed in the following manner:
 
# We take a simple iterative approach to solve the problem.
# First, we define a function ‘romanToInt’ which takes a character and returns its integer representation.
# We make a variable ‘count’ to store the answer.
# Then, we simply traverse through the string, and if the current character value is more than the next character value we follow rule 2 and add the values.
# If the current character is less than the value of the next character, we subtract the value of the current character from the value of the next character.
# Finally, we return the variable ‘count’.

# Time Complexity

# O(N), Where ‘N’ denotes the length of the string.

 

# We traverse the string once to find the integer value.
# Space Complexity

# O(1).
 
# Since we are using constant space.

'''

    Time Complexity     :   O(N)
    Space Complexity    :   O(1)

    Where 'N' is the length of the string.
    
'''

def romanToInt(s):

    count = 0

    # To store previous char value.
    preInt = 0

    # Map for finding integer value for roman numerals.
    conv = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    # Loop from end to start of the string.
    for i in range(len(s)-1, -1, -1):
        ch = s[i]

        # Store current char integer value.
        curInt = conv[ch]

        '''
            If current value is greater or equal to previous value then increment count i.e., II means 1+1
            else in case of IV, V = 5 and I = 1 here 1 < 5 then else part will execute and update count as 5 - 1 = 4.
        '''
        if (curInt >= preInt):
            count += curInt
        else:
            count -= curInt

        # Update 'preInt' value with current value for next iteration.
        preInt = curInt

    return count    