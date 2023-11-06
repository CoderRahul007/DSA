from bisect import bisect_left
class Solution:
    def search(self,arr,x):
        l,r=0,len(arr)-1
        while l<=r:
            m=(l+r)//2
            if arr[m]==x:
                return m
            elif arr[m]>x:
                r=m-1
            else:
                l=m+1
        return l

    def findClosestElements(self, arr, k, x):
        if x<arr[0]:
            return arr[:k]
        if x>arr[-1]:
            return arr[len(arr)-k:]
        index=self.search(arr,x)
        print(index)
        lis=[(i,v) for i,v in enumerate(arr)]
        print(lis)
        l=index-1
        r=index
        while k>0:
            if l>=0 and r<len(arr):
                if (x-arr[l])>(arr[r]-x):
                    r+=1
                    print('r',r)
                else:
                    l-=1
                    print('l',l)
            elif l<0:
                    r+=1
                    print('r',r)
            elif r>=len(arr):
                l-=1
                print('l',l)
            k-=1
        return (arr[l+1:r],arr) # From l+1 to r-1
s=Solution()
print(s.findClosestElements([0,1,1,1,2,3,6,7,8,9],9,4))
                