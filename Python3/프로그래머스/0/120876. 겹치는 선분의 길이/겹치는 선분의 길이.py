def solution(lines):
    answer = 0
    temp = []
    for line in lines:
        a, b = line
        for i in range(b-a):
            temp.append(((a+i)+(a+1+i))/2)
    count = set(temp)
    for num in count:
        if temp.count(num) > 1: answer += 1
    return answer