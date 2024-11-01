def solution(arr):
    answer = []
    count = 0
    length = len(arr)
    while length > 1:
        length /= 2
        count += 1
    answer = arr + [0] * (2**(count) - len(arr))
    return answer