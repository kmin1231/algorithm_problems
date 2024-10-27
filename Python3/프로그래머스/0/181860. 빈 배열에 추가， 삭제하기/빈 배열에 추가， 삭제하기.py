def solution(arr, flag):
    answer = []
    count = len(arr)
    for i in range(count):
        if flag[i] == True:
            for j in range(arr[i] * 2):
                answer.append(arr[i])
        else:
            for j in range(arr[i]):
                answer.pop()
    return answer