def solution(arr, queries):
    answer = arr
    count = len(arr)
    for elem in queries:
        [a, b] = elem
        for i in range(count):
            if (i in range(a, b+1)): answer[i] += 1
            else : continue
    return answer