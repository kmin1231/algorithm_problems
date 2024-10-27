def solution(arr):
    indices = []
    for i in range(len(arr)):
        if arr[i] == 2: indices.append(i)
    if len(indices) == 0: answer = [-1]
    else:
        answer = arr[indices[0]:indices[-1]+1]
    return answer