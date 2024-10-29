def solution(n):
    answer = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            answer[i][j] = 1 if i==j else 0
    return answer