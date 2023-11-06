class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(arr,key,left):
            l ,r =0, len(arr)-1
            while l<=r:
                m=(l+r)//2
                if arr[m] < key:
                    l=m+1
                elif arr[m] >key:
                    r=m-1
                else:
                    if left:
                        if m==0 or arr[m-1] != key:
                            return m
                        else:
                            r=m-1
                    else:
                        if m==len(arr)-1 or arr[m+1] !=key:
                            return m
                        else:
                            l=m+1
            return -1
        return [search(nums,target,True), search(nums,target,False)]
                
            
       