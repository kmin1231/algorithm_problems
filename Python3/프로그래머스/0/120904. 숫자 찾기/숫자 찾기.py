def solution(num, k):
    num_str = str(num)
    answer = num_str.index(str(k))+1 if (str(k) in num_str) else -1
    return answer