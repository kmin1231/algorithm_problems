def solution(n):
    answer = 0
    numList = list(str(n))
    for num in numList: answer += int(num)
    return answer