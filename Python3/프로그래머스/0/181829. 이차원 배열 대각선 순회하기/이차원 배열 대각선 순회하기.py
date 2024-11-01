def solution(board, k):
    answer = 0
    rows = len(board)
    cols = len(board[0])

    for i in range(min(rows, k+1)):
        max_j = min(k-i, cols-1)
        for j in range(max_j+1):
            if (i + j <= k): answer += board[i][j]
            else : break
    return answer