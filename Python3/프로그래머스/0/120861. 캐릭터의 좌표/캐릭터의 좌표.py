def solution(keyinput, board):
    x, y = 0, 0
    row, col = board[0], board[1]
    row, col = row//2, col//2
    print(row, col)

    for act in keyinput:    
        if act == "up": y = y + 1 if (-col <= y+1 <= col) else y
        elif act == "down": y = y - 1 if (-col <= y-1 <= col) else y
        elif act == "left": x = x - 1 if (-row <= x-1 <= row) else x
        else: x = x + 1 if (-row <= x+1 <= row) else x
    answer = [x, y]
    return answer