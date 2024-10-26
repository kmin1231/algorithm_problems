def solution(arr1, arr2):
    size1 = len(arr1)
    size2 = len(arr2)
    
    if (size1 < size2): answer = -1
    elif (size1 > size2): answer = 1
    else:
        sum1, sum2 = 0, 0
        for i in arr1:
            sum1 += i
        for i in arr2:
            sum2 += i
        if (sum1 < sum2): answer = -1
        elif (sum1 > sum2): answer = 1
        else: answer = 0  
    return answer