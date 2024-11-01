def solution(array):
    maximum = max(array)
    idx = array.index(maximum)
    answer = [maximum, idx]
    return answer