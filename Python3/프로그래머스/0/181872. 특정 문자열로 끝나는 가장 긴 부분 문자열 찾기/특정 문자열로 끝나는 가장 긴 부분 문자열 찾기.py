def solution(myString, pat):
    answer = ''
    tempStr = ''
    for i in range(len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat: tempStr = myString[:i+len(pat)]
        if len(tempStr) > len(answer): answer = tempStr        
    return answer