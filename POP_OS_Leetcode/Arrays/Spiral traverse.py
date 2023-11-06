class Solution:
    def generateMatrix(self, n):
        sR,eR,sC,eC=(0,n,0,n)
        # start  Row sR
        # end Row eR
        # start column sC
        # end column eC
        res=[[0 for i in range(n)] for j in range(n)]
        k=1
        while sR<eR and sC<eC:
            # for going right
            for i in range(sC,eC):
                res[sR][i]=k
                k+=1
            sR+=1
            
            # for going down
            for i in range(sR,eR):
                res[i][eC-1]=k
                k+=1
            eC-=1
            
            # for going left
            if sR<eR:
                for i in range(eC-1,sC-1,-1):
                    res[eR-1][i]=k
                    k+=1
                eR-=1
            # for going up
            if sC<eC:
                for i in range(eR-1,sR-1,-1):
                    res[i][sC]=k
                    k+=1
                sC+=1
        return res
                
s=Solution()
print(s.generateMatrix(3))
print(s.generateMatrix(4))

# object Solution {
#     trait Direction
#     object UP extends Direction
#     object DOWN extends Direction
#     object RIGHT extends Direction
#     object LEFT extends Direction
    
#     def spiralOrderRecursion(dir: Direction, size: (Int, Int), col: Int, row: Int, level: Int, matrix: Array[Array[Int]], set: Set[String]): Unit = {
#         if(set.contains(s"${row}-${col}")) Nil
#         else {
#             dir match {
#                 case UP =>
#                     if(row == level + 1) {
#                         spiralOrderRecursion(RIGHT, size, col + 1, row, level + 1, matrix, set + s"${row}-${col}")
#                     } else if(row >= 0){
#                         spiralOrderRecursion(UP, size, col, row - 1, level, matrix, set + s"${row}-${col}")
#                     } else return
#                 case DOWN =>
#                     if(row == size._2 - level) {
#                         spiralOrderRecursion(LEFT, size, col - 1, row, level, matrix, set + s"${row}-${col}")
#                     } else if(row <= size._2){
#                         spiralOrderRecursion(DOWN, size, col, row + 1, level, matrix, set + s"${row}-${col}")
#                     } else return
#                 case RIGHT =>
#                     if(col == size._1 - level) {
#                         spiralOrderRecursion(DOWN, size, col, row + 1, level, matrix, set + s"${row}-${col}")
#                     } else if(col <= size._1){
#                         spiralOrderRecursion(RIGHT, size, col + 1, row, level, matrix, set + s"${row}-${col}")
#                     } else return
#                 case LEFT => 
#                     if(col == level) {
#                         spiralOrderRecursion(UP, size, col, row - 1, level, matrix, set + s"${row}-${col}")
#                     } else if(col > 0){
#                         spiralOrderRecursion(LEFT, size, col - 1, row, level, matrix, set + s"${row}-${col}")
#                     } else return
#             }
            
#             matrix(row)(col) = set.size + 1
#         }
#     }
    
#     def generateMatrix(n: Int): Array[Array[Int]] = {
#         if(n == 0) return Array()
#         val matrix = Array.ofDim[Int](n, n)
#         spiralOrderRecursion(RIGHT, (n-1, n-1), 0, 0, 0, matrix, Set())
#         matrix
#     }