def solution(arr):
    rows = len(arr)
    cols = len(arr[0])
    max = rows if (rows > cols) else cols
    answer = [[0 for i in range(max)] for j in range(max)]
    for i in range(rows):
        for j in range(cols):
            answer[i][j] = arr[i][j]
    return answer