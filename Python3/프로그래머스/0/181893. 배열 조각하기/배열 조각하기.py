def solution(arr, query):
    answer = arr
    for i in range(len(query)):
        idx = query[i]
        if (i%2 == 0):
            answer = answer[:idx+1]
        else:
            answer = answer[idx:]        
    return answer