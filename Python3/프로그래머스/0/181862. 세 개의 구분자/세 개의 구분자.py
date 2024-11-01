def solution(myStr):
    answer = []
    start = 0
    found = False
    
    for i in range(len(myStr)):
        if myStr[i] in "abc":
            if start < i:
                answer.append(myStr[start:i])
                found = True
            start = i + 1

    if start < len(myStr): answer.append(myStr[start:])
        
    if answer == []: answer = ["EMPTY"]
    return answer