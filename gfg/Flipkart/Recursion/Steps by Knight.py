class Solution:

	#Function to find out minimum steps Knight needs to reach target position.
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
		#Code here
          
        pos = []
        pos.append(KnightPos)
        visited = [[0]*N for i in range(N)]
        
        if KnightPos==TargetPos:
            return 0
        
        ans=0
        while pos:
            ans+=1
            
            l = len(pos)
            for i in range(l):
                for j in [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]:
                    x,y = pos[0][0]+j[0], pos[0][1]+j[1]
                    
                    if x>=1 and x<=N and y>=1 and y<=N and visited[x-1][y-1]==0:
                        pos.append([x,y])
                        visited[x-1][y-1]=1
                        if [x,y]==TargetPos:
                            return ans
                pos.pop(0)