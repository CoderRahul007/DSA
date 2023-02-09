def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    
    nums.sort()
    res=[]
    quad=[]
    
    def K_Sum(start,K,target):
        
        if K!=2:
            for i in range(start,len(nums)-K+1):
                if nums[i]==nums[i-1] and i>start:
                    continue
                quad.append(nums[i])
                K_Sum(i+1,K-1,target-nums[i])
                quad.pop()
            return
        
        else:
            l,r=start,len(nums)-1
            while(l<r):
                two_sum=nums[l]+nums[r]
                if two_sum>target:
                    r-=1
                elif two_sum<target:
                    l+=1
                else:
                    res.append(quad+[nums[l],nums[r]])
                    l+=1
                    while(nums[l]==nums[l-1] and l<r):
                        l+=1
    K_Sum(0,4,target)
    return res