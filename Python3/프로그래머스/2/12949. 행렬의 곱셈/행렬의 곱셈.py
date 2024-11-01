def solution(arr1, arr2):
    rows = len(arr1)
    count = len(arr1[0])
    cols = len(arr2[0])
    answer = [[0 for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            for k in range(count):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer