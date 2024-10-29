def solution(strArr):
    count = len(strArr)
    list = [0 for i in range(count)]
    for elem in strArr:
        length = len(elem)
        list[length] += 1        
    answer = max(list)
    return answer