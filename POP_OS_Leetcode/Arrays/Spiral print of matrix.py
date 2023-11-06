class Solution:
    def spiralOrder(self, matrix):
        if len(matrix)==0:
            return []
        sr,er,sc,ec=(0,len(matrix),0,len(matrix[0]))
        k=1
        res=[]
        while sr<er and sc<ec:
            for i in range(sc,ec):
                res.append(matrix[sr][i])
            sr+=1
            
            for i in range(sr,er):
                 res.append(matrix[i][ec-1])
            ec-=1
            
            if sr<er:
                for i in range(ec-1,sc-1,-1):
                     res.append(matrix[er-1][i])                    
                er-=1
            if sc<ec:
                for i in range(er-1,sr-1,-1):
                     res.append(matrix[i][sc])                    
                sc+=1
        return res
            
s=Solution()
print(s.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))
print(s.spiralOrder([]))
print(s.spiralOrder([[]]))