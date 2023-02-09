class Solution:
	def pushZerosToEnd(self,arr, n):
    	# code here
    	idx = 0
    	for i in range(n):
    	    if arr[i] > 0:
    	        arr[idx] = arr[i]
    	        idx += 1
    	while idx < n:
    	    arr[idx] = 0
    	    idx +=1