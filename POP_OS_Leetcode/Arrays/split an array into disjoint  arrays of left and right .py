class Solution(object):
    def second(self,A):
        alength=1
        aMax=A[0]
        maxEnc=0
        for i in range(len(A)):
            maxEnc=max(maxEnc,A[i])           
            if A[i]<aMax:
                aMax=maxEnc
                alength+=1              
        return alength

    def partitionDisjoint(self, A):
        N = len(A)
        maxleft = [None] * N
        minright = [None] * N

        m = A[0]
        for i in range(N):
            m = max(m, A[i])
            maxleft[i] = m

        m = A[-1]
        for i in range(N-1, -1, -1):
            m = min(m, A[i])
            minright[i] = m
        print(maxleft)
        print(minright)

        for i in range(1, N):
            if maxleft[i-1] <= minright[i]:
                return i

# class Solution {

#     public int partitionDisjoint(int[] A) {
#         int aLength = 1;
#         int aMax = A[0];
#         int maxEncountered = 0;

#         for (int i = 0; i < A.length; i++) {
#             maxEncountered = Math.max(maxEncountered, A[i]);

#             if (A[i] < aMax) {
#                 aMax = maxEncountered;
#                 aLength = i + 1;
#             }
#         }

#         return aLength;
#     }
# }



s=Solution()
print(s.partitionDisjoint([5,0,3,8,6]))
print(s.second([5,0,3,8,6]))
