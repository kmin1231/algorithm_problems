def solution(my_str, n):
    answer = []
    idx = []
    for i in range(len(my_str)):
        if i%n == 0: idx.append(i)
    for j in range(len(idx)-1):
        start, end = idx[j], idx[j+1]
        answer.append(my_str[start:end])
    answer.append(my_str[idx[-1]:])
    return answer