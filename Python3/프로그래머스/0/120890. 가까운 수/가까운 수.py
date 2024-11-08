def solution(array, n):
    answer = array[0]
    min_diff = abs(array[0] - n)
    for num in array:
        diff = abs(num - n)
        if diff < min_diff:
            answer = num
            min_diff = diff
            continue
        elif diff == min_diff:
            answer = num if (num < answer) else answer
    return answer