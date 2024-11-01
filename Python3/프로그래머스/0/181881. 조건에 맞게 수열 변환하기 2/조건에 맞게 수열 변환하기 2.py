def solution(arr):
    count = 0
    result = dict()
    result[0] = arr
    while True:
        count += 1
        result[count] = []
        for num in result[count-1]: 
            if (num >= 50) and (num %2 == 0): num = int(num/2)
            elif (num < 50) and (num%2 == 1): num = num * 2 + 1
            result[count].append(num)
        if result[count] == result[count-1]:
            break
    return count - 1