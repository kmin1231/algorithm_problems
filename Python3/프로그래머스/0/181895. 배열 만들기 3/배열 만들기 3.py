def solution(arr, intervals):
    answer = []
    
    [a, b] = intervals[0]
    [c, d] = intervals[1]

    intv1, intv2 = [], []
    for i in range(a, b+1):
        intv1.append(arr[i])
    for j in range(c, d+1):
        intv2.append(arr[j])

    answer = intv1 + intv2

    return answer