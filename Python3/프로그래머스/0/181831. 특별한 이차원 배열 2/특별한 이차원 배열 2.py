def solution(arr):
    answer = 1
    count = len(arr)
    for i in range(count):
        for j in range(count):
            if arr[i][j] == arr[j][i]: continue
            else :
                answer = 0
                break
    return answer