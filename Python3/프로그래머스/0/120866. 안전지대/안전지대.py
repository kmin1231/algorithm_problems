directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),            (0, 1),
    (1, -1),   (1, 0),  (1, 1)
]
    
def solution(board):
    answer = 0
    n = len(board)
    change = []  # to save locations to change value
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if (0 <= nx < n) and (0 <= ny < n):
                        change.append((nx, ny))
    for nx, ny in change:
        board[nx][ny] = 1
    
    answer = sum(row.count(0) for row in board)
    return answer