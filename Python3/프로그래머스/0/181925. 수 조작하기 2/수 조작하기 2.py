def solution(numLog):
    answer = ''
    count = len(numLog)
    for i in range(1, count):
        diff = numLog[i] - numLog[i-1]
        if (diff == 1): answer += "w"
        elif (diff == -1): answer += "s"
        elif (diff == 10): answer += "d"
        else: answer += "a"        
    return answer