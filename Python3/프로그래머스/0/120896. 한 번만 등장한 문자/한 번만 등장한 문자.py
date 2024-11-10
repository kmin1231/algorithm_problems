def solution(s):
    answer = ''
    numbers = []
    idx = []
    for char in s:
        numbers.append(s.count(char))
    for i in range(len(numbers)):
        if numbers[i] == 1: idx.append(i)
    for j in idx:
        answer += s[j]
    answer = ''.join(sorted(answer))
    return answer