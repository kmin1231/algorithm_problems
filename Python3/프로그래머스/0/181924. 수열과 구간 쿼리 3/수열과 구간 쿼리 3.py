def solution(arr, queries):
    for elem in queries:
        [i, j] = elem
        arr[i], arr[j] = arr[j], arr[i]
    return arr