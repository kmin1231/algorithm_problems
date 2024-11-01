def solution(n):
    answer = [[0 for j in range(n)] for i in range(n)]
    count = 1
    
    startRow, endRow = 0, n-1
    startCol, endCol = 0, n-1
    
    while count <= n*n:
        for i in range(startCol, endCol+1):
            answer[startRow][i] = count
            count += 1
        startRow += 1
        
        for i in range(startRow, endRow+1):
            answer[i][endCol] = count
            count += 1
        endCol -= 1
        
        for i in range(endCol, startCol-1, -1):
            answer[endRow][i] = count
            count += 1
        endRow -= 1
        
        for i in range(endRow, startRow-1, -1):
            answer[i][startCol] = count
            count += 1
        startCol += 1

    return answer