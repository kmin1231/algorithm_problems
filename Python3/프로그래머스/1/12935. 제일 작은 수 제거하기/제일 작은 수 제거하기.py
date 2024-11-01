def solution(arr):
    minimum = min(arr)
    arr.remove(minimum)
    answer = arr
    if len(answer) == 0: answer = [-1]
    return answer