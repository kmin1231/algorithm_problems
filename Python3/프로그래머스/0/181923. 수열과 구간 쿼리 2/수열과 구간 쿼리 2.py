def solution(arr, queries):
    answer = []
    for elem in queries:
        [s, e, k] = elem
        temp = []
        for num in arr[s:e+1]:
            if (num <= k): continue
            else: temp.append(num)
        if len(temp) == 0: min = -1
        else:
            temp.sort()
            min=temp[0]
        answer.append(min)
    return answer
