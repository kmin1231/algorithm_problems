def solution(myString):
    answer = ''
    # count = len(myString)
    for char in myString:
        if (char < 'l'): answer += 'l'
        else : answer += char
    return answer