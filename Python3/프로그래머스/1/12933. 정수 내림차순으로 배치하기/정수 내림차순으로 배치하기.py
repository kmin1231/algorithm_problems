def solution(n):
    numString = str(n)
    numList = list(numString)
    numList.sort(reverse=True)
    answer = ''.join(numList)
    answer = int(answer)
    return answer