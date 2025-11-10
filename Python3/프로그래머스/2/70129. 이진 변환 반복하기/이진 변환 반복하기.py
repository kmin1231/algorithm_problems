def solution(s):
    count, zero_count = 0, 0

    while s != "1":
        zeros = s.count('0')
        zero_count += zeros

        s = s.replace('0', '')
        s = bin(len(s))[2:]
        count += 1

    answer = [count, zero_count]
    return answer