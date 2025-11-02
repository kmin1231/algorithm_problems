from collections import Counter

def solution(X, Y):
    count_X = Counter(X)
    count_Y = Counter(Y)

    result = []

    # iterate from 9 down to 0 to make the largest possible number
    for num in map(str, range(9, -1, -1)):
        if (num in count_X) and (num in count_Y):
            common_count = min(count_X[num], count_Y[num])
            result.append(num * common_count)   # 'str' type

    if not result: return "-1"   # NO common digits
    
    answer = ''.join(result)

    if answer[0] == '0': return "0"   # only ZEROs

    return answer