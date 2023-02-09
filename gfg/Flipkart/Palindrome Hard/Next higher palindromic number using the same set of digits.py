# Approach: Following are the steps:

# If number of digits n <= 3, then print “Not Possible” and return.
# Calculate mid = n/2 – 1.
# Start traversing from the digit at index mid up to the 1st digit and 
# while traversing find the index i of the rightmost digit which is smaller than the digit on its right side.
# Now search for the smallest digit greater than the digit num[i] in the
#  index range i+1 to mid. Let the index of this digit be smallest.
# If no such smallest digit found, then print “Not Possible”.
# Else the swap the digits at index i and smallest and also swap the digits
#  at index n-i-1 and n-smallest-1. This step is done so as to maintain the palindromic property in num.
# Now reverse the digits in the index range i+1 to mid. Also If n is even
#  then reverse the digits in the index range mid+1 to n-i-2 else if n is 
# odd then reverse the digits in the index range mid+2 to n-i-2. This step
#  is done so as to maintain the palindromic property in num.
# Print the final modified number num.
