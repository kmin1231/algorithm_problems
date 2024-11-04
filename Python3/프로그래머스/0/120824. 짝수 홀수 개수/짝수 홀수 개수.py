def solution(num_list):
    even = 0
    for num in num_list:
        if num %2 == 0: even += 1
    odd = len(num_list) - even
    answer = [even, odd]
    return answer