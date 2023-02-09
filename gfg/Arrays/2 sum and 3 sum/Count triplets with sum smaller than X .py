class Solution:
    def countTriplets(self, arr, n, sumo):
        #code here
        c = 0
        arr.sort()
        
        for i in range(n-1):
            j = i+1
            k = n-1
            
            while j < k:
                if  arr[i] + arr[j] + arr[k] >= sumo:
                    k-=1
                else:
                     # This is important. For current i and j, there
                    # can be total k-j third elements.
                    c += (k-j)
                    j +=1
        return c
        