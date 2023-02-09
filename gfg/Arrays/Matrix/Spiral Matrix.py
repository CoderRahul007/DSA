def spirallyTraverse(matrix, r, c): 
    top = 0
    left = 0
    down = r-1
    right = c-1
    dir = 0
    l = []

    
    while top <= down and left <= right:
        
        if dir == 0:
            for i in range(left , right+1):
                l.append(matrix[top][i])
            top +=1

        elif dir == 1:
            for i in range(top , down+1):
                l.append(matrix[i][right])
            right -=1

        elif dir == 2:
            for i in range(right , left-1 , -1):
                l.append(matrix[down][i])
            down -=1

        elif dir == 3:
            for i in range(down , top-1 ,  -1):
                l.append(matrix[i][left])
            left +=1

        dir = (dir + 1) % 4
    return l