def solution(array):
    answer = 0
    for num in array:
        num_str = str(num)
        answer += num_str.count('7')
    return answer