class Solution:


	def generateNextPalindrome(self,arr, n ) :
	    # code here
	    if n == 1:
	        if arr[0] == 9:
	            return [1 , 1]
	        arr[0] += 1
	        return arr
	    num = []
	    for i in range(n):
	        num.append(arr[i])
	    
	    # Find the index of mid digit
	    mid = n //2
	    
	    # A bool variable to check if copy of left
    #side to right is sufficient or not
	    leftSmaller = False
	    
	     # End of left side is always 'mid -1'
	    i = mid - 1
	    
	    
    # Beginning of right side depends
    # if n is odd or even
	    j = mid + 1 if n % 2 else mid
	    
	     # Initially, ignore the middle same digits 
	    while i >= 0 and num[i] == num[j] :
	        i-=1
	        j+=1
	    
	       # Find if the middle digit(s) need to be
        # incremented or not (or copying left 
    # side is not sufficient)
	    if i < 0 or num[i] < num[j]:
	        leftSmaller = True
	    
	     #  Copy the mirror of left to tight
	    while i >= 0:
	        num[j] = num[i]
	        j+=1
	        i-=1
	    
	      # Handle the case where middle digit(s) must
        # be incremented. This part of code is for 
        # CASE 1 and CASE 2.2
	    if leftSmaller :
	        carry = 1
	        i = mid -1
	        
	        #If there are odd digits, then increment
        #the middle digit and store the carry
	        if n % 2 == 1:
	            num[mid] += carry
	            carry = num[mid] // 10
	            num[mid] %= 10
	            j = mid + 1
	        else:
	            j = mid
	        
	        while i >= 0:
	            num[i] += carry
	            carry = num[i] //10
	            num[i] %= 10
	            
	            # Copy mirror to right
	            num[j] = num[i]
	            j+=1
	            i-=1
	    return num